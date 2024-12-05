import os
import shutil
import sys
import time

file_to_path = {

    ".txt": "Documents",
    ".csv": "Documents",
    ".pptx": "Documents",
    ".docx": "Documents",
    ".py": "Downloads",
    ".zip": "Downloads",
    ".pdf": "Downloads",
    ".jpg": "Pictures",
    ".png": "Pictures",
    ".mp4": "Media"
}

restricted_files = ["organize_script.py", "file_creator.py", "README.md"]

def make_directory(path, name):
    final_directory = os.path.join(path, name)
    if os.path.isdir(final_directory):
        return final_directory
    os.mkdir(final_directory)
    return final_directory

def get_time(file_path):
    c_time = os.path.getctime(file_path)
    c_time = time.ctime(c_time)
    month = c_time.split()[1]
    year = c_time.split()[-1]
    return month, year


def main(text, target_dir, source):

    if text != None:
        file_to_path[text] = target_dir

    changes = []

    for root, dirs, files in os.walk(source):
        for file in files:
            if file in restricted_files:
                continue
            extension = os.path.splitext(file)[1]
            try:
                changes.append([file, file_to_path[extension]])
            except KeyError:
                print(f"{file} has an unknown extension(will not be sorted)")
                continue

    print("Proposed Changes: ")
    for file, target in changes:
        print(f"{file} ---> {target}")

    approval = input("Approve these changes?(y/n) ").lower()

    if approval != "y":
        print("Operation terminated.")
        return
    for file, target in changes:
        target = make_directory(source, target)
        file_path = os.path.join(source, file)
        month, year = get_time(file_path)
        target = make_directory(target,f"{month}-{year}")
        shutil.move(file_path, target)
        print(f"{file} ---> {target}")
    print("Files Successfuly Moved.")

if __name__=="__main__":
    if sys.argv[1]=="auto":
        if len(sys.argv)!=2:
            raise Exception("if auto, must be only command line input")
    elif sys.argv[1] == "custom":
        if len(sys.argv)!=5:
            raise Exception("if custom, must provide extension, target folder, and specified directory - only")
    else:
        raise Exception("invalid organization type")
    
    try:
        extension = sys.argv[2]
        target = sys.argv[3]
        directory = sys.argv[4]
    except IndexError:
        extension = None
        target = None
        directory = os.getcwd()

    main(extension, target, directory)