import pathlib

# source: pathlib.Path - source file to get contents of
# dest: pathlib.Path - destination file to put contents in
def copyFile(source, dest):
  with source.open() as i:
    with dest.open(mode='w') as o:
      o.write(i.read())
