from pathlib import Path
import os
print(str(Path('1','2','3')))
print(Path('spam')/'bacon'/'eggs.tht')
print(Path.cwd())
#FileNotFoundError
print(Path.home())
# Path(r'\Programming and Excel\Pyton\TestDir\Level1').mkdir()
# #os.makedirs(r'D:\Programming and Excel\Pyton\TestDir\Level1\Leve2\Level3')

# >>> p = Path('C:/Users/Al/spam.txt')
# >>> p.anchor
# 'C:\\'
# >>> p.parent # This is a Path object, not a string.
# WindowsPath('C:/Users/Al')
# >>> p.name
# 'spam.txt'
# >>> p.stem
# 'spam'
# >>> p.suffix
# '.txt'
# >>> p.drive
# 'C:'

# >>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
# >>> os.path.basename(calcFilePath)
# 'calc.exe'
# >>> os.path.dirname(calcFilePath)
# 'C:\\Windows\\System32'

# os.path.getsize('C:\\Windows\\System32\\calc.exe')
# 27648
# >>> os.listdir('C:\\Windows\\System32')
p = Path('./')
# >>> p.glob('*')
# <generator object Path.glob at 0x000002A6E389DED0>
print(list(p.glob('*'))) # Make a list from the generator.

# >>> winDir = Path('C:/Windows')
# >>> notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
# >>> calcFile = Path('C:/Windows
# /System32/calc.exe')
# >>> winDir.exists()
# True
# >>> winDir.is_dir()
# True
# >>> notExistsDir.exists()
# False
# >>> calcFile.is_file()
# True
# >>> calcFile.is_dir()
# False