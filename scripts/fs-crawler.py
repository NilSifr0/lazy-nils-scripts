"""
This script finds all sub dir and files under the current directory, extracts their name, and appends them in a text file. The initial idea for creating this is to create a tree like documentation of file and folder structures.
"""

from pathlib import Path


def crawl_directory():
    current_directory = Path(".")

    for item in current_directory.iterdir():
        try:
            if item.is_dir():
                with open("dir_tree.txt", "a+", encoding="UTF-8") as file:
                    file.write(f"{item.name}")
            elif item.is_file():
                with open("dir_tree.txt", "a+", encoding="UTF-8") as file:
                    file.write(f"{item.name}")

        except FileExistsError:
            print("file exists")

        else:
            print("op successful")

        finally:
            print("script terminated")


def main():
    pass


if __name__ == "__main__":
    main()
