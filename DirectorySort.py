#Sorts the files of a directory into folders by year
from pathlib import Path
import datetime

#What directory to sort
InputDirectory = str(input("Input the directory to sort: "))
Directory = Path(f"{InputDirectory}")
#If the directory does not exist, throw an error
assert Directory.exists(), "Error: Not a valid directory"
for child in Directory.iterdir():
    ModifiedDate = datetime.date.fromtimestamp(child.stat().st_mtime)
    Folder = Path(f"{Directory}" + r"\\" + f"{ModifiedDate.year}")
    try:
        Folder.mkdir()
        child.rename(Folder / child.name)
    except: pass
    #If is a file and sorted directory exists, move to it
    if child.is_file():
        child.rename(Folder / child.name)
