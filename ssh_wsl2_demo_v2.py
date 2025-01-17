import paramiko
import threading
import time
from utilities.configurations import *

# Get configuration information
win_user = get_config()['WSL2']['win_user']
wsl2_ip = get_config()['WSL2']['wsl2_ip']
wsl2_user = get_config()['WSL2']['wsl2_user']
wsl2_password = get_config()['WSL2']['wsl2_password']

# Initialize `client` and `shell` to avoid warnings
client = None
shell = None

def read_from_shell(remote_shell):
    """Read and print output from the remote shell."""
    try:
        while True:
            if remote_shell.recv_ready():
                output = remote_shell.recv(1024).decode("utf-8")
                if output:
                    print(output, end="")
    except KeyboardInterrupt:
        print("\nRead thread interrupted.")
    except Exception as err:
        print(f"\nUnexpected error in read thread: {err}")

def write_to_shell(remote_shell):
    """Send user input to the remote shell."""
    try:
        while True:
            user_input = input()  # This will be interrupted by Ctrl+C
            if user_input.strip().lower() == "exit":
                remote_shell.send("exit\n")
                break
            # Disable echo command from Terminal
            elif user_input.strip().lower() == "enable-echo":
                remote_shell.send("stty echo\n")
            elif user_input.strip().lower() == "disable-echo":
                remote_shell.send("stty -echo\n")
            else:
                remote_shell.send(user_input + "\n")
    except KeyboardInterrupt:
        print("\nWrite thread interrupted.")
        remote_shell.send("exit\n")  # Gracefully exit remote shell
    except Exception as err:
        print(f"\nUnexpected error in write thread: {err}")

try:
    # Initialize the SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the WSL2 SSH server
    print(f"Connecting to {wsl2_user}@{wsl2_ip}...")
    client.connect(hostname=wsl2_ip, username=wsl2_user, password=wsl2_password)
    print("\nConnected successfully to WSL2.")
    print("\nEntering full terminal mode. Type 'exit' to quit or press Ctrl+C to interrupt.")

    # Open an interactive shell session
    shell = client.invoke_shell()

    # Disable command echo
    shell.send("stty -echo\n")
    time.sleep(1)  # Allow the command to take effect

    # Start threads for reading and writing
    read_thread = threading.Thread(target=read_from_shell, args=(shell,), daemon=True)
    read_thread.start()

    write_to_shell(shell)  # Write user input in the main thread

except paramiko.ssh_exception.AuthenticationException:
    print("\nAuthentication failed. Check your username or private key.")
except FileNotFoundError as e:
    print(f"\nPrivate key not found: {e}")
except KeyboardInterrupt:
    print("\nSSH session interrupted by user.")
finally:
    # Cleanup: Ensure `shell` and `client` are closed
    if shell is not None and not shell.closed:
        shell.close()
    if client is not None:
        client.close()
    print("\nSSH session terminated.")
