# batch convert svg files to png files
# requirements
# inkscape software installed
# python 3 system installed
# instruction
# run this script in the target folder

import subprocess
from pathlib import Path

base_dir = Path(__file__)

path = base_dir

path_list = [file for file in path.iterdir() if file.is_file()]

print(path_list)

for file in path_list:
    print(f"converting: {file}")

    # shell command
    result = subprocess.run(
        [
            "inkscape",  # means use inkscape core
            "--export-type=png",
            "--export-background-opacity=0.0",  # transparent background
            file,
        ],
        capture_output=True,
        text=True,
    )
    print("done.")
print(result.stdout)
