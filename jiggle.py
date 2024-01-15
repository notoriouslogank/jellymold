from pathlib import Path
import os


def sanitize(directory: str):
    sanitized_dir = Path(directory)
    return sanitized_dir


def get_dir():
    user_input = Path(input(f"Directory [defaults to cwd]:"))
    default_directory = Path(os.getcwd())
    if user_input == "":
        return default_directory
    elif Path.is_absolute(user_input):
        user_directory = Path(user_input)
        return user_directory
    else:
        user_directory = Path.joinpath(default_directory, Path(user_input))
        return user_directory


def get_season():
    season = int(input("Season: "))
    return season


def get_files(directory):
    file_list = []
    files = os.listdir(directory)
    for file in files:
        file_list.append(file)
    print(file_list)
    return file_list


def rename(files, directory, season, episode: int, amount):
    for file in files:
        infile = Path(os.path.join(directory, file))
        name, extension = os.path.splitext(file[amount:])
        template = f"{name} S{season:02d}E{episode:02d}{extension}"
        print(f"{infile} ->")
        outfile = Path(os.path.join(directory, template))
        os.rename(infile, outfile)
        print(f"{outfile}\n---")
        episode += 1


def main():
    directory = get_dir()
    episode = 1
    files = get_files(directory)
    amount = int(input("Truncate: "))
    rename(files, directory, get_season(), episode, amount)


main()
