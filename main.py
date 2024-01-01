# Python Main Application with Dynamic Navigation and GitHub Integration - INDEVotion
# main_app.py
# URL of this conversation

import json
import os

def load_applications():
    with open('applications.json', 'r') as file:
        return json.load(file)["applications"]

def display_app_info(app):
    print(f"\n{app['name']}")
    print(f"Description: {app['description']}")
    print(f"Root Path: {app['root_path']}")
    print(f"Config Path: {app['config_path']}")
    # Display other paths as needed

def clone_from_github(github_url, root_path):
    # Placeholder for GitHub cloning functionality
    print(f"Cloning from {github_url} to {root_path}")
    # Implement actual cloning here

def run_application(app):
    if not os.path.exists(app['root_path']):
        clone_from_github(app['github'], app['root_path'])
    else:
        print(f"Application {app['name']} already exists at {app['root_path']}")

    display_app_info(app)
    # Placeholder for actual application functionality

def main_menu(applications):
    while True:
        print("\nMain Menu:")
        for app in applications:
            print(f"{app['id']}. {app['name']}")
        print("exit. Exit")

        choice = input("Enter your choice: ")

        if choice == 'exit':
            print("Exiting the main application.")
            break

        selected_app = next((app for app in applications if app['id'] == choice), None)
        if selected_app:
            run_application(selected_app)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    applications = load_applications()
    main_menu(applications)
