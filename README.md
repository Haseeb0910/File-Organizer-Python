# 🗂️ File Organizer — Python Automation

A Python script that automatically organizes messy folders by sorting 
files into categorized subfolders by file type.

## 🚀 What It Does
- Scans any folder you give it
- Sorts files into: Images, Documents, Videos, Audio, Code, Archives, Others
- Creates a log file with timestamp of every file moved

## 📁 Folder Structure After Running
messy_folder/
├── Images/       → .jpg, .png, .gif ...
├── Documents/    → .pdf, .docx, .txt ...
├── Videos/       → .mp4, .mov, .avi ...
├── Audio/        → .mp3, .wav, .aac ...
├── Code/         → .py, .js, .html, .cpp ...
├── Archives/     → .zip, .rar, .tar ...
└── Others/       → everything else

## 🛠️ How To Use
1. Clone this repo or download the script
2. Open `file_organizer.py`
3. Change this line to your folder path:
```python
   folder_to_clean = r"C:\Your\Folder\Path"
```
4. Run:
python file_organizer.py

## 📋 Requirements
- Python 3.x
- No external libraries needed (uses built-in os, shutil)

## 👨‍💻 Author
Built by M.Haseeb ur Rehman — Data Science Student from Pakistan
