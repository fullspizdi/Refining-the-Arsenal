import random
from Utilities import log_message, create_directory

# List of potential low-key targets for testing tools
potential_targets = [
    "example.com",
    "testsite.org",
    "demo.net",
    "sampledomain.edu",
    "localtest.co"
]

def select_random_target():
    """
    Selects a random target from the list of potential targets.
    """
    target = random.choice(potential_targets)
    log_message(f"Randomly selected target: {target}")
    return target

def setup_target_environment():
    """
    Sets up a directory to store information about the targets.
    """
    target_dir = "/path/to/lab/environment/Targets"
    create_directory(target_dir)
    log_message("Target environment setup complete.")

if __name__ == "__main__":
    setup_target_environment()
    selected_target = select_random_target()
    log_message(f"Selected target for testing: {selected_target}")
