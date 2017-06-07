import pathlib

# path: pathlib.Path - directory to remove contents of
def deleteContents(path):
  for i in path.glob('*'):
    if i.is_dir():
      # NOTE: can replace two lines below with `deleteDirectory(i)` from pathlib-recusive-delete-directory scrap
      deleteContents(i)
      i.rmdir()
    else:
      i.unlink()
