# scraps
[Lil' Bits](https://www.youtube.com/watch?v=Gj4-E5Hs3Kc) of code that I might want to reuse. Feel free to steal them(with credit).

## Table of Contents
### Python
* [list comprehension building a string incrementally](#incremental-string-builder-link)
* [copy file using pathlib](#file-copy-via-pathlib-link)
* [recursively delete directory contents using pathlib](#delete-contents-via-pathlib-link)
* [recursively delete directory(and its contents)](#delete-directory-and-contents-via-pathlib-link)
### Java
### C#

<br>
<hr>
<br>


## Python

#### Incremental String Builder [[link]](https://github.com/jabocg/scraps/blob/master/python/incremental-string-builder.py)
```python
[string[:i] for i in range(1, len(string))]
```

#### File Copy via `pathlib` [[link]](https://github.com/jabocg/scraps/blob/master/python/pathlib-copy-file.py)
```python
import pathlib

# source: pathlib.Path - source file to get contents of
# dest: pathlib.Path - destination file to put contents in
def copyFile(source, dest):
  with source.open() as i:
    with dest.open(mode='w') as o:
      o.write(i.read())
```

#### Delete Contents via `pathlib` [[link]](https://github.com/jabocg/scraps/blob/master/python/pathlib-recursive-delete-contents.py)
```python
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
```

#### Delete Directory (and contents) via `pathlib` [[link]](https://github.com/jabocg/scraps/blob/master/python/pathlib-recursive-delete-directory.py)
```python
mport pathlib

# path: pathlib.Path - directory to remove
def deleteDirectory(path):
  # NOTE: can replace five lines below with `removeConents(path)` scrap form pathlib-recursive-remove-contents
  for i in path.glob('*'):
    if i.is_dir():
       deleteDirectory(i)
    else:
      i.unlink()
  path.rmdir()
```
