import os
import subprocess
import requests
from datetime import datetime

def log_message(message):
    """
    Logs a message with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def run_command(command):
    """
    Executes a shell command and returns the output.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        log_message(f"Error executing command: {e.output.decode('utf-8')}")
        return None

def download_file(url, dest_path):
    """
    Downloads a file from a given URL to a specified destination path.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(dest_path, 'wb') as f:
            f.write(response.content)
        log_message(f"File downloaded successfully from {url} to {dest_path}")
    except requests.RequestException as e:
        log_message(f"Failed to download file from {url}: {e}")

def create_directory(path):
    """
    Creates a directory if it does not exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        log_message(f"Directory created: {path}")
    else:
        log_message(f"Directory already exists: {path}")

def check_internet_connection():
    """
    Checks for an active internet connection.
    """
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            log_message("Internet connection is active.")
            return True
    except requests.ConnectionError:
        log_message("No internet connection.")
    return False
