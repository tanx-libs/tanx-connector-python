import subprocess

# Specify the path to your shell script
script_path = './script.sh'

# Run the shell script using subprocess
try:
    subprocess.run(['bash', script_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
