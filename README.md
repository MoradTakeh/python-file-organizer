# Python File Organizer

A Python script that automatically organizes files into folders based on their file extensions.

## Features

- Automatically categorizes files by extension.
- Creates destination folders when needed.
- Prevents overwriting existing files by generating unique filenames.
- Tracks the number of moved, skipped, and renamed files.
- Displays a summary of files organized by category.
- Uses Python's `pathlib` and `shutil` modules.

## Supported Categories

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.tif`, `.png`, `.jfif` |
| Videos | `.mp4` |
| Music | `.mp3`, `.aac` |
| Documents | `.pdf`, `.srt`, `.docx`, `.xlsx`, `.csv` |
| Python | `.py` |
| Archives | `.zip`, `.rar`, `.vsix` |
| PowerPoint | `.ppt`, `.pptx` |

## Requirements

- Python 3.13 or a compatible Python 3 version
- No external packages required

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

4. Enter the path of the folder you want to organize when prompted.

**Tip:** Test the script on a sample folder before using it on important files.

## Technologies

- Python
- pathlib
- shutil
- Git and GitHub

## Project Status
## Example Output

```text
Folder exists.
Images: 3 files
PowerPoint: 8 files
Files moved: 11
Skipped: 11
Renamed: 3
```

*Example output from a test run. Results depend on the files in the selected folder.*

First portfolio project — built and tested with file categorization, duplicate filename handling, and processing statistics.
