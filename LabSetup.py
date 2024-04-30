import os
from Utilities import log_message, create_directory, check_internet_connection, download_file

def setup_lab_environment():
    """
    Sets up a dedicated lab environment for testing and development.
    """
    log_message("Starting setup of the lab environment.")

    # Check internet connection before proceeding
    if not check_internet_connection():
        log_message("Setup cannot proceed without an internet connection.")
        return

    # Create main lab directory
    lab_dir = "/path/to/lab/environment"
    create_directory(lab_dir)

    # Create subdirectories for different tools and projects
    subdirectories = [
        "Recon", "Exploitation", "Anonymity", "Research", "Logs"
    ]
    for subdir in subdirectories:
        create_directory(os.path.join(lab_dir, subdir))

    # Download necessary tools and resources
    tools = {
        "AFL": "http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz",
        "VirtualBox": "https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-Win.exe"
    }
    for tool_name, tool_url in tools.items():
        dest_path = os.path.join(lab_dir, f"{tool_name}.tgz")
        download_file(tool_url, dest_path)

    log_message("Lab environment setup is complete.")

if __name__ == "__main__":
    setup_lab_environment()
