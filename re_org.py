import os
import shutil
import glob

def collect_and_rename_images(source_dir, destination_dir, new_prefix="image_"):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created destination directory: {destination_dir}")
    else:
        print(f"Destination directory already exists: {destination_dir}")

    # Supported image extensions (add more if needed)
    image_extensions = ('*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp')
    
    count = 1
    # Recursively find all files matching the extensions
    for ext in image_extensions:
        # Use glob.glob with recursive=True (requires Python 3.5+)
        # If using older Python, you could use os.walk as an alternative
        for file_path in glob.glob(os.path.join(source_dir, '**', ext), recursive=True):
            if os.path.isfile(file_path):
                # Get the original file extension
                _, file_extension = os.path.splitext(file_path)
                dir_name=os.path.dirname(file_path)
                dir_name="_"+os.path.basename(dir_name)
                # Create a new sequential filename (e.g., image_001_category.jpg)
                new_filename = f"{new_prefix}{count:04d}{dir_name}{file_extension.lower()}"
                destination_path = os.path.join(destination_dir, new_filename)
                
                # Copy the file to the new destination
                try:
                    shutil.copy2(file_path, destination_path) # copy2 preserves metadata
                    print(f"Copied and renamed: {os.path.basename(file_path)} -> {new_filename}")
                    count += 1
                except shutil.SameFileError:
                    print(f"Skipping: Source and destination are the same file {new_filename}")
                except Exception as e:
                    print(f"Error copying file {file_path}: {e}")

    print(f"\nDone. Total images processed: {count - 1}")

# --- Example Usage ---
# Define your source and destination paths
# Make sure to use appropriate paths for your system
source_folder = "./data/koala_kangaroo_images_small" # Folder containing subfolders of images
destination_folder = "./data/koala_kangaroo_images_small_renamed" # The single target folder

collect_and_rename_images(source_folder, destination_folder)
