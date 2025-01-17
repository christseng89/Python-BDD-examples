import paramiko
import csv
import os
from utilities.configurations import *

# Initialize the client to ensure it's defined
client = None

try:
    # Fetch connection details from configuration
    config = get_config()
    win_user = config['WSL2']['win_user']
    wsl2_user = config['WSL2']['wsl2_user']
    wsl2_ip = config['WSL2']['wsl2_ip']
    wsl2_password = config['WSL2']['wsl2_password']

    # Initialize SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    python_file = "script.py"
    csv_file = "loanasa.csv"

    print("Connecting to the server...")
    try:
        client.connect(hostname=wsl2_ip, username=wsl2_user, password=wsl2_password)
        print("Connected successfully!")
    except paramiko.AuthenticationException:
        raise Exception("Authentication failed. Check username or password.")
    except paramiko.SSHException as e:
        raise Exception(f"SSH connection error: {e}")
    except Exception as e:
        raise Exception(f"Failed to connect to {wsl2_ip}: {e}")

    # File transfer using SFTP
    try:
        sftp = client.open_sftp()

        # Upload files
        files_to_upload = {
            f"batchFiles/{python_file}": f"{python_file}",
            f"batchFiles/{csv_file}": f"{csv_file}"
        }
        for local_path, remote_path in files_to_upload.items():
            if not os.path.exists(local_path):
                raise FileNotFoundError(f"Local file not found: {local_path}")
            print(f"Uploading {local_path} to {remote_path}...")
            sftp.put(local_path, remote_path)
        print("Files uploaded successfully.")
    except FileNotFoundError as e:
        raise Exception(f"File error: {e}")
    except Exception as e:
        raise Exception(f"Error during file upload: {e}")

    # Trigger batch commands
    try:
        print("Executing remote script...")
        stdin, stdout, stderr = client.exec_command(f"python3 {python_file}")
        exit_status = stdout.channel.recv_exit_status()
        if exit_status != 0:
            error_message = stderr.read().decode('utf-8')
            raise Exception(f"Remote script execution failed with exit status {exit_status}: {error_message}")
        print("Remote script executed successfully.")
    except Exception as e:
        raise Exception(f"Error executing remote script: {e}")

    # Download output file
    try:
        remote_output_file = f"{csv_file}"
        local_output_file = f"outputFiles/{csv_file}"
        print(f"Downloading {remote_output_file} to {local_output_file}...")
        sftp.get(remote_output_file, local_output_file)
        print("File downloaded successfully.")
    except FileNotFoundError as e:
        raise Exception(f"File not found on server: {e}")
    except Exception as e:
        raise Exception(f"Error during file download: {e}")

    # Parse the output CSV
    try:
        print(f"Parsing CSV file: {local_output_file}...")
        with open(local_output_file, newline='') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            for row in csvReader:
                if row[0] == "32321":
                    assert row[1] == "approved", f"\n\tRow assertion failed for ID 32321. Expected 'approved', got '{row[1]}'."
        print("CSV parsed successfully, and assertions passed.")
    except FileNotFoundError:
        raise Exception(f"Output file not found: {local_output_file}")
    except AssertionError as e:
        raise Exception(f"\nAssertion error: {e}")
    except Exception as e:
        raise Exception(f"Error parsing CSV: {e}")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Clean up resources
    try:
        if client:
            print("Closing SSH connection...")
            client.close()
            print("SSH connection closed.")
    except Exception as e:
        print(f"Error while closing SSH connection: {e}")
