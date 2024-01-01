# Ignite Builder - App Runner

## Project Overview
This project comprises a Python application designed to manage and run multiple smaller Python scripts. It includes functionalities for handling applications configurations, executing Python scripts, and managing file operations.

## Modules
- `main.py`: The main entry point for the application.
- `app_loader.py`: Handles loading application configurations from a JSON file.
- `app_runner.py`: Manages the execution of individual applications, including cloning from GitHub and handling requirements.
- `file_handler.py`: Responsible for file operations like displaying file contents, managing log files, and handling output files.

## Configuration
The application uses a JSON file (`applications.json`) for configuration. This file includes details of each application and global settings.

## Running the Application
To run the application, execute the `main.py` script in a Python environment. Ensure all dependencies are installed and the configuration file is set up correctly.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
