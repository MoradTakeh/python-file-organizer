import shutil
from pathlib import Path


def get_unique_path(destination, item):
    target = destination / item.name
    if not target.exists():
        return target, False

    base_name = item.stem
    counter = 1
    target = destination / f"{base_name}_{counter}{item.suffix}"

    while target.exists():
        counter += 1
        target = destination / f"{base_name}_{counter}{item.suffix}"

    return target, True


def process_file(item, file_categories, folder):
    category = file_categories.get(item.suffix.lower())
    if category is None:
        return None
    destination = folder / category
    destination.mkdir(exist_ok=True)
    target, renamed = get_unique_path(destination, item)
    shutil.move(item, target)
    return category, renamed


def organize_files(folder, file_categories):
    """Organize files into folders based on their extensions."""
    if not folder.exists() or not folder.is_dir():
        print("Folder does not exist.")
        return 0, 0, 0, {}

    print("Folder exists.")
    moved_count = 0
    skipped_count = 0
    renamed_count = 0
    category_counts = {}

    for item in folder.iterdir():
        if not item.is_file():
            continue

        result = process_file(item, file_categories, folder)

        if result is None:
            skipped_count += 1
            continue

        category, renamed = result

        if renamed:
            renamed_count += 1

        category_counts.setdefault(category, 0)
        category_counts[category] += 1
        moved_count += 1

    return moved_count, skipped_count, renamed_count, category_counts


folder_path = input("Enter folder path: ")
folder = Path(folder_path)
file_categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".tif": "Images",
    ".png": "Images",
    ".jfif": "Images",
    ".mp4": "Videos",
    ".mp3": "Music",
    ".aac": "Music",
    ".pdf": "Documents",
    ".srt": "Documents",
    ".docx": "Documents",
    ".py": "Python",
    ".zip": "Archives",
    ".rar": "Archives",
    ".vsix": "Archives",
    ".ppt": "PowerPoint",
    ".pptx": "PowerPoint",
    ".xlsx": "Documents",
    ".csv": "Documents",
}

moved_files, skipped_files, renamed_files, category_counts = organize_files(
    folder, file_categories
)
for category, count in category_counts.items():
    print(f"{category}: {count} files")
print(f"Files moved: {moved_files}")
print(f"Skipped:     {skipped_files}")
print(f"Renamed:     {renamed_files}")
