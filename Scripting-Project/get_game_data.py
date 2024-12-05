import os #used for getting paths
import shutil#used to copy directories
import sys #used for inline arguments

source_pattern = "game"

def make_dir(target_path):
    if os.path.exists(target_path):
        pass
    else:
        os.mkdir(target_path)
    
def get_targetfile_path(source_path):
    elgible_dirs = []
    for root, dirs, files in os.walk(source_path):
        for directory in dirs:
            if source_pattern in directory.lower():
                dir_path = os.path.join(root,directory)
                elgible_dirs.append(dir_path)
        break #bc os.walk is recursive and we only need one iteration to get all game directories
    return elgible_dirs

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd,target)

    game_dirs = get_targetfile_path(source_path)

    make_dir(target_path)

    changing_path = target_path

    for directory in game_dirs:
        current_name = os.path.basename(directory)
        new_name = current_name.replace("_game","")
        changing_path = os.path.join(changing_path, new_name)
        shutil.copytree(directory, changing_path)
        changing_path = target_path

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:#it's 3 bc to run the file it is a default one arg
        raise Exception('Only a source and target directory must be provided')
    source_dir = args[1]
    target_dir = args[2]
    main(source_dir, target_dir)