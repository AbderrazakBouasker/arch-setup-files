# Files Organizer

A Python script that automatically organizes files in your Downloads folder into categorized subdirectories based on file types.

## Features

- **Automatic Folder Creation**: Creates category folders (Documents, Images, Videos, Audio, Archives, Programs, Scripts) as needed
- **Smart File Categorization**: Organizes files based on their extensions
- **Duplicate Handling**: Automatically renames files if a file with the same name already exists in the destination folder
- **Logging**: Provides detailed logs of all file operations
- **Systemd Integration**: Can be set up as a systemd service to run periodically

## File Categories

The script organizes files into the following categories:

- **Documents**: PDF, DOC, DOCX, TXT, RTF, ODT, XLS, XLSX, PPT, PPTX, CSV, etc.
- **Images**: JPG, PNG, GIF, BMP, SVG, WEBP, ICO, TIFF, RAW, HEIC, etc.
- **Videos**: MP4, AVI, MKV, MOV, WMV, FLV, WEBM, M4V, MPG, etc.
- **Audio**: MP3, WAV, FLAC, AAC, OGG, WMA, M4A, OPUS, etc.
- **Archives**: ZIP, RAR, 7Z, TAR, GZ, BZ2, XZ, TGZ, etc.
- **Programs**: EXE, MSI, DEB, RPM, AppImage, DMG, PKG, APK, etc.
- **Scripts**: PY, SH, BASH, JS, RB, PL, PHP, JAVA, C, CPP, etc.
- **Others**: Any file type not matching the above categories

## Installation

### Manual Installation

1. Copy the script to `/usr/local/Files-Organizer/`:

```bash
sudo mkdir -p /usr/local/Files-Organizer
sudo cp Files-Organizer/organizer.py /usr/local/Files-Organizer/
sudo chmod +x /usr/local/Files-Organizer/organizer.py
```

2. Test the script:

```bash
python3 /usr/local/Files-Organizer/organizer.py
```

### Systemd Service Installation

To run the organizer automatically every 2 hours:

1. Copy the systemd service and timer files:

```bash
sudo cp 'systemd_services/files organisation/files-organizer.service' /etc/systemd/system/
sudo cp 'systemd_services/files organisation/files-organizer.timer' /etc/systemd/system/
```

2. Enable and start the timer:

```bash
sudo systemctl daemon-reload
sudo systemctl enable files-organizer.timer
sudo systemctl start files-organizer.timer
```

3. Check the timer status:

```bash
sudo systemctl status files-organizer.timer
```

4. Check when the timer will run next:

```bash
systemctl list-timers files-organizer.timer
```

## Usage

### Manual Execution

Simply run the script:

```bash
python3 /usr/local/Files-Organizer/organizer.py
```

Or if you've installed it system-wide:

```bash
/usr/local/Files-Organizer/organizer.py
```

### Run as Systemd Service

Trigger the service manually:

```bash
sudo systemctl start files-organizer.service
```

View the service logs:

```bash
sudo journalctl -u files-organizer.service -f
```

## How It Works

1. **Scans** the Downloads folder (`~/Downloads`)
2. **Creates** category folders if they don't exist
3. **Identifies** each file's type based on its extension
4. **Moves** files to their appropriate category folder
5. **Handles duplicates** by appending numbers to filenames (e.g., `file_1.pdf`, `file_2.pdf`)
6. **Logs** all operations for transparency

## Customization

You can customize the file categories and extensions by editing the `FILE_CATEGORIES` dictionary in `organizer.py`:

```python
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ...],
    "Images": [".jpg", ".png", ...],
    # Add or modify categories as needed
}
```

## Requirements

- Python 3.6 or higher
- Standard Python libraries (os, shutil, pathlib, logging)
- Linux system with systemd (for automatic scheduling)

## Troubleshooting

### Script doesn't run automatically

Check the timer status:
```bash
sudo systemctl status files-organizer.timer
```

Check the service status:
```bash
sudo systemctl status files-organizer.service
```

View recent logs:
```bash
sudo journalctl -u files-organizer.service -n 50
```

### Permission errors

Make sure the script has execute permissions:
```bash
sudo chmod +x /usr/local/Files-Organizer/organizer.py
```

### Files not being moved

Check if the Downloads folder path is correct. The script uses `~/Downloads` by default. You can modify the `DOWNLOADS_FOLDER` variable in the script if your Downloads folder is in a different location.

## License

This script is provided as-is for personal use.
