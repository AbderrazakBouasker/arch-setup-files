#!/usr/bin/env python3
"""
File Organizer Script
Automatically organizes files in the Downloads folder into categorized subdirectories.
Creates folders automatically based on file types.
"""

import os
import shutil
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get the user's Downloads folder
DOWNLOADS_FOLDER = Path.home() / "Downloads"

# Define file categories and their extensions
FILE_CATEGORIES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", 
        ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".ods", 
        ".odp", ".tex", ".md"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", 
        ".webp", ".ico", ".tiff", ".tif", ".raw", ".heic"
    ],
    "Videos": [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", 
        ".webm", ".m4v", ".mpg", ".mpeg", ".3gp"
    ],
    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", 
        ".m4a", ".opus", ".alac"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", 
        ".xz", ".tar.gz", ".tar.bz2", ".tar.xz", ".tgz"
    ],
    "Programs": [
        ".exe", ".msi", ".deb", ".rpm", ".AppImage", 
        ".dmg", ".pkg", ".apk"
    ],
    "Scripts": [
        ".py", ".sh", ".bash", ".js", ".rb", ".pl", 
        ".php", ".java", ".c", ".cpp", ".h", ".hpp"
    ],
    "Others": []  # Catch-all for unrecognized file types
}


def create_category_folders():
    """Create category folders in the Downloads directory if they don't exist."""
    for category in FILE_CATEGORIES.keys():
        if category == "Others":
            continue  # Don't create Others folder unless needed
        
        category_path = DOWNLOADS_FOLDER / category
        if not category_path.exists():
            try:
                category_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created folder: {category_path}")
            except Exception as e:
                logger.error(f"Error creating folder {category_path}: {e}")


def get_file_category(file_extension):
    """Determine the category of a file based on its extension."""
    file_extension = file_extension.lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    return "Others"


def organize_files():
    """Organize files in the Downloads folder into their respective categories."""
    if not DOWNLOADS_FOLDER.exists():
        logger.error(f"Downloads folder not found: {DOWNLOADS_FOLDER}")
        return
    
    logger.info(f"Starting file organization in: {DOWNLOADS_FOLDER}")
    
    # Create category folders first
    create_category_folders()
    
    files_moved = 0
    files_skipped = 0
    
    # Iterate through all files in the Downloads folder
    for item in DOWNLOADS_FOLDER.iterdir():
        # Skip if it's a directory or if it's one of our category folders
        if item.is_dir():
            continue
        
        # Get file extension
        file_extension = item.suffix
        
        # Determine category
        category = get_file_category(file_extension)
        
        # Create Others folder only if needed
        if category == "Others" and file_extension:
            category_path = DOWNLOADS_FOLDER / category
            category_path.mkdir(exist_ok=True)
        
        # Skip files without extensions (might be system files)
        if not file_extension and category == "Others":
            logger.debug(f"Skipping file without extension: {item.name}")
            files_skipped += 1
            continue
        
        # Construct destination path
        destination_folder = DOWNLOADS_FOLDER / category
        destination_path = destination_folder / item.name
        
        # Handle duplicate filenames
        if destination_path.exists():
            base_name = item.stem
            extension = item.suffix
            counter = 1
            
            while destination_path.exists():
                new_name = f"{base_name}_{counter}{extension}"
                destination_path = destination_folder / new_name
                counter += 1
        
        # Move the file
        try:
            shutil.move(str(item), str(destination_path))
            logger.info(f"Moved: {item.name} -> {category}/")
            files_moved += 1
        except Exception as e:
            logger.error(f"Error moving {item.name}: {e}")
            files_skipped += 1
    
    logger.info(f"Organization complete. Files moved: {files_moved}, Files skipped: {files_skipped}")


def main():
    """Main function to run the file organizer."""
    try:
        organize_files()
    except Exception as e:
        logger.error(f"An error occurred during file organization: {e}")
        raise


if __name__ == "__main__":
    main()
