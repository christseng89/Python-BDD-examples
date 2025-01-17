import subprocess
from utilities.configurations import *

# Get configuration information
win_user = get_config()['WSL2']['win_user']
wsl2_user = get_config()['WSL2']['wsl2_user']
wsl2_ip = get_config()['WSL2']['wsl2_ip']

# Define the SSH command
ssh_command = [
    "ssh",
    "-tt",  # Force pseudo-terminal allocation
    "-i", f"C:\\Users\\{win_user}\\.ssh\\id_rsa",
    f"{wsl2_user}@{wsl2_ip}"
]

process = None  # Initialize the process variable

try:
    # Start the SSH process
    process = subprocess.Popen(ssh_command, text=True)

    # Wait for the process to complete
    process.wait()
    print("\nSSH session completed successfully.")

except KeyboardInterrupt:
    # print("SSH session interrupted. Cleaning up...")
    # Check if the process was started before attempting to terminate it
    if process:
        process.terminate()
        process.wait()
        print("\nSSH session interrupt terminated.")

except subprocess.CalledProcessError as e:
    print(f"Error occurred during SSH: {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")