import os
import shutil
from datetime import datetime

# --- SETTINGS ---
folder_to_clean = r"C:\Users\User\Desktop\messy_folder"

# --- FILE CATEGORIES ---
file_types = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents":  [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":      [".mp3", ".wav", ".aac"],
    "Excel_CSV":  [".csv", ".xlsx", ".xls"],
    "Code":       [".py", ".js", ".html", ".css", ".json", ".sql", ".cpp"],
    "Archives":   [".zip", ".rar", ".tar", ".gz"],
}

# --- MAIN LOGIC ---
def organize_folder(folder):
    files_moved = 0

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isdir(filepath):
            continue

        ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(folder, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} → {folder_name}/")

                # ✅ encoding fix here
                with open("organizer_log.txt", "a", encoding="utf-8") as log:
                    log.write(f"{datetime.now()} | Moved: {filename} → {folder_name}/\n")

                files_moved += 1
                moved = True
                break

        if not moved:
            dest_folder = os.path.join(folder, "Others")
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved: {filename} → Others/")

            # ✅ encoding fix here
            with open("organizer_log.txt", "a", encoding="utf-8") as log:
                log.write(f"{datetime.now()} | Moved: {filename} → Others/\n")

            files_moved += 1

    print(f"\n✅ Done! {files_moved} files organized.")

# --- RUN ---
organize_folder(folder_to_clean)