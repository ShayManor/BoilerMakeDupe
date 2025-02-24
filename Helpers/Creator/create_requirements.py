import os


def create_requirements(path, name):
    # pip install pipreqs
    # pipreqs /path/to/project
    before = os.getcwd()
    os.chdir(os.path.join(os.getcwd(), path))
    os.system(f"cd {path}")
    os.system("pip install pipreqs")
    os.system(f"pipreqs .")
    os.system(f"mv ../requirements.txt {name}/requirements.txt")
    os.chdir(before)
    return True
