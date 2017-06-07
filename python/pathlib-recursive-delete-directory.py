import pathlib

# path: pathlib.Path - directory to remove
def deleteDirectory(path):
  # NOTE: can replace five lines below with `deleteConents(path)` scrap form pathlib-recursive-remove-contents
  for i in path.glob('*'):
    if i.is_dir():
       deleteDirectory(i)
    else:
      i.unlink()
  path.rmdir()
