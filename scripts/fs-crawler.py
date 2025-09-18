# creates a file structure of children from current directory
from pathlib import Path


def write_directory_structure(base_path, file, prefix=""):
    items = list(base_path.iterdir())
    total_items = len(items)

    for index, item in enumerate(items):
        connector = "├── " if index < total_items - 1 else "└── "
        file.write(f"{prefix}{connector}{item.name}{'/' if item.is_dir() else ''}\n")

        if item.is_dir():
            # Create a new prefix for the next level
            new_prefix = prefix + ("│   " if index < total_items - 1 else "    ")
            write_directory_structure(item, file, new_prefix)


def main():
    # current_directory = Path(__file__) # use this to run script on where the file currently is
    current_directory = Path.home() / "Documents"  # Test directory
    output_file_path = f"{current_directory.name}_fs.txt"

    try:
        with open(output_file_path, "w", encoding="UTF-8") as file:
            write_directory_structure(current_directory, file)
    except IOError:
        pass


if __name__ == "__main__":
    main()
