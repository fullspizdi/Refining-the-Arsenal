import webbrowser
from Utilities import log_message, check_internet_connection, download_file

def open_maltego_website():
    """
    Opens the Maltego official website in the default web browser.
    """
    url = "https://www.maltego.com/"
    try:
        webbrowser.open(url)
        log_message("Opened Maltego website successfully.")
    except Exception as e:
        log_message(f"Failed to open Maltego website: {str(e)}")

def download_maltego():
    """
    Downloads the Maltego installation file.
    """
    url = "https://www.maltego.com/downloads/"
    dest_path = "downloads/maltego_setup.exe"
    download_file(url, dest_path)

def setup_maltego():
    """
    Sets up Maltego by downloading and opening the website for further instructions.
    """
    if check_internet_connection():
        log_message("Setting up Maltego...")
        download_maltego()
        open_maltego_website()
    else:
        log_message("Internet connection is required to set up Maltego.")

if __name__ == "__main__":
    setup_maltego()
