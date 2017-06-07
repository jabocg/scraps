import pathlib

# path: pathlib.Path - directory to remove
def removeDirectory(path):
  for i in path.glob('*'):
    if i.is_dir():
       removeDirectory(i)
    else:
      i.unlink()
  # NOTE: can replace above lines with `removeConents(path)` scrap form pathlib-recursive-remove-contents 
  path.rmdir()
