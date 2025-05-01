#Sorts the files of a directory into folders by year
from pathlib import Path
import datetime

#What directory to sort
#Directory = Path("c:/", "Users", "matth", "Downloads")
InputDirectory = str(input("Input the directory to sort: "))
Directory = Path(f"{InputDirectory}")
#If the directory does not exist, throw an error
assert Directory.exists(), "Error: Not a valid directory"
for child in Directory.iterdir():
    ModifiedDate = datetime.date.fromtimestamp(child.stat().st_mtime)
    Folder = Path(f"{Directory}" + r"\\" + f"{ModifiedDate.year}")
    try: Folder.mkdir()
    except: pass
    child.rename(Folder / child.name)