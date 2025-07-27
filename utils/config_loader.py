import yaml
import os

def load_config(config_path: str = "config\config.yaml") -> dict:  # type: ignore
    """
    Loads a YAML configuration file.
    It constructs an absolute path to 'config/config.yaml' from the project root.
    """
    if config_path is None:
        # Get the directory of the current script (.../utils)
        script_dir = os.path.dirname(__file__)
        # Go up one level to the project root (.../document_portal) and join with the config file path
        config_path = os.path.abspath(os.path.join(script_dir, "..", "config", "config.yaml"))

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

# Example of how to run it
if __name__ == "__main__":
    try:
        # When run directly, it will use the default path logic
        config_data = load_config()
        print("Configuration loaded successfully:")
        print(config_data)
    except FileNotFoundError:
        print(f"Error: The configuration file could not be found.")
    except Exception as e:
        print(f"An error occurred while loading the config file: {e}")