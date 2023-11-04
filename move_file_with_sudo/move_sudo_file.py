import subprocess

source_file = '/Users/evgeniy/HDD\ in\ orico\ case.png'
destination_directory = '/usr/local/bin'

# Prompt the user for the sudo password
sudo_password = input("Enter your sudo password: ")

# Construct the sudo command
sudo_command = f'echo {sudo_password} | sudo -S mv {source_file} {destination_directory}'

# Execute the sudo command using subprocess
subprocess.run(sudo_command, shell=True)