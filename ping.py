import subprocess
import platform

def is_network_connection_ok():
    # Define the target host to ping (can change this to the desired host)
    target_host = "www.google.com" 

    # Define the command based on the operating system
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", target_host]
    else:
        command = ["ping", "-c", "1", target_host]

    try:
        # Run the ping command
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Network connection is OK!")
        return True
    except subprocess.CalledProcessError:
        print("Network connection is not OK.")
        return False

# Check the network connection
is_network_connection_ok()

# Ask the user to input 1 to exit
print()
user_input = input("Enter '1' to exit the program: ")
while user_input != '1':
    user_input = input("Invalid input. Please enter '1' to exit the program: ")

print("Exiting the program.")
