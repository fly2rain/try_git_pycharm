from pathlib import Path

path_1 = Path("/Users/f0z00qt/fyzhu_all/pycharm")
text_filename = path_1 / "try_git_pycharm" / "try_pathlib" / "foxnews.txt"

print(f"path_1 is: {path_1}")
print(f"text_filename is: {text_filename}")

print(f"Content of text_filename is:")
print(len(text_filename.read_text().split("\n")))
print(text_filename.read_text().split("\n"))

print("**********************************")
path_1 = Path("~/fyzhu_all/pycharm/try_git_pycharm")
path_2 = path_1 / "try_pathlib" / "foxnews.txt"
text_filename = path_2.expanduser()
print(f"path_2: {path_2}")
print(f"text_filename: {text_filename}")
print("---------------------------------")

print(text_filename.stem)
print(text_filename.suffix)
print(text_filename.name)
print(text_filename.parent)
print(text_filename.exists())
print(text_filename.absolute())
print(text_filename.home())
print(text_filename.is_dir())
print(text_filename.anchor)
print(text_filename.expanduser())
print(text_filename.owner())
# print(text_filename.rename("foxnews.txt"))
# Path.touch("tmp.txt", exist_ok=True)
# print(text_filename.suffixes)

import os.path
file_to_open = os.path.join("source_data", "text_files", "raw_data.txt")
print(file_to_open)





