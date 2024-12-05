# File Organizer Script

## Overview
This Python script automates the organization of files by moving them into categorized folders based on their extensions. The tool supports both **automatic sorting** and **custom folder mapping** for extensions. It also organizes files by creation month and year.

---

## Features
- Automatically sorts files into predefined categories such as Documents, Downloads, Pictures, and Media.
- Supports custom extensions and target folders with user input.
- Organizes files by their creation date (e.g., `Documents/Mar-2024`).
- Provides a preview of changes before execution for user approval.
- Skips restricted files to avoid unintended operations.

---

## Usage

### 1. Automatic Organization
Run the script in **auto** mode to use predefined mappings:
python organize_script.py auto

### 2. Custom Organization
Run the script in **custom** mode to use custom mappings:
python organize_script.py custom <extension> <target_folder> <source_directory>


## Restrictions

- Restricted files (organize_script.py, file_creator.py, README.md) are skipped.
- Unknown extensions are ignored with a notification.

This version is clean, structured, and ready for direct use in your repository.