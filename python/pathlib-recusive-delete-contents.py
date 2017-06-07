import pathlib

# path: pathlib.Path - directory to remove contents of
def removeContents(path):
  for i in path.glob('*'):
    if i.is_dir():
      # NOTE: can replace both lines with `removeDirectory(i)` from pathlib-recusive-rmdir scrap
      removeContents(i)
      i.rmdir()
    else:
      i.unlink()
