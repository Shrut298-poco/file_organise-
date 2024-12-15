import os
import shutil

# Specify the directory to organize
directory_to_organize = input("Enter the full path of the folder to organize: ")

# Categories and their corresponding file extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
}

def create_folders(base_dir, category_names):
    """Create folders for categories if not already present."""
    for category in category_names:
        folder_path = os.path.join(base_dir, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(base_dir):
    """Organize files into corresponding category folders."""
    for file_name in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine file category based on extension
        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                dest_folder = os.path.join(base_dir, category)
                shutil.move(file_path, dest_folder)
                print(f"Moved '{file_name}' to '{category}' folder.")
                moved = True
                break
        
        # Move files that don't fit into any category
        if not moved:
            other_folder = os.path.join(base_dir, "Others")
            shutil.move(file_path, other_folder)
            print(f"Moved '{file_name}' to 'Others' folder.")

# Create necessary folders
create_folders(directory_to_organize, list(categories.keys()) + ["Others"])

# Organize the files
organize_files(directory_to_organize)

print("File organization complete!")
