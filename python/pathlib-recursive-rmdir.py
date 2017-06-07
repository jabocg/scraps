import pathlib

path = Path(...)

for i in path.glob('*'):
  if i.is_dir():
     removeDirectory(i)
  else:
    i.unlink()
path.rmdir()
