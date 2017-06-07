import pathlib

# path: pathlib.Path - directory to remove
def removeDirectory(path):
  for i in path.glob('*'):
    if i.is_dir():
       removeDirectory(i)
    else:
      i.unlink()
  path.rmdir()
