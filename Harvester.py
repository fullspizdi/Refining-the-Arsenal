import os
from Utilities import log_message, download_file, create_directory

def setup_harvester():
    """
    Sets up the Harvester tool for gathering information such as email addresses and subdomains.
    """
    log_message("Starting setup of the Harvester tool.")

    # Define the directory for Harvester
    harvester_dir = "/path/to/lab/environment/Recon/Harvester"
    create_directory(harvester_dir)

    # URL to download theHarvester
    harvester_url = "https://github.com/laramies/theHarvester/archive/refs/heads/master.zip"
    harvester_zip_path = os.path.join(harvester_dir, "theHarvester-master.zip")

    # Download theHarvester
    download_file(harvester_url, harvester_zip_path)

    log_message("Harvester setup is complete.")

def run_harvester(domain):
    """
    Runs the Harvester tool to collect information on the specified domain.
    """
    harvester_dir = "/path/to/lab/environment/Recon/Harvester"
    harvester_script_path = os.path.join(harvester_dir, "theHarvester-master/theHarvester.py")

    # Command to run theHarvester
    command = f"python3 {harvester_script_path} -d {domain} -b all"

    log_message(f"Running Harvester on domain: {domain}")
    os.system(command)

if __name__ == "__main__":
    setup_harvester()
    # Example domain to test
    run_harvester("example.com")
