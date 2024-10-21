#  File Organizer: Create a script to automatically sort and organize files in a folder based on their extensions (e.g., images, documents).

import os
import shutil

# Define the categories for file organisation

file_categories = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv' ],
    'Music': ['mp3', '.wav', '.aac', '.flac'],
    'Archieves':['.zip', '.rar','.7zip', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html','.css'],
}

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_file(file_path, target_directory):
    # Create directory if it doesn't exist
    create_directory(target_directory)

    # Move the file to the target directory
    shutil.move(file_path, target_directory)

def get_category(extension):
    # Check the file extension against categories
    for category, extensions in file_categories.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organised_files(directory):
    # List all files in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Check if the item is a file
        if os.path.isfile(item_path):
            # Get the file extension
            file_extension = os.path.splitext(item)[1]
            category = get_category(file_extension)

            # Define the target directory based on the category
            target_directory = os.path.join(directory, category)

            # Move the file to its corresponding category folder
            move_file(item_path, target_directory)

def file_organiser():
    print("Welcome to the File Organiser!")

    # Ask the directory to organise
    directory = input("Enter the path of the directory to organise( leave blank to organise the current directory): ")

    if not directory:
        # Get the current working directory if no input is given
        directory = os.getcwd()

    # Start Organising the files
    organised_files(directory)
    print(f"Files in {directory} have been organised successfully!")

    # Run the file organiser
if __name__ == "__main__":
    file_organiser()