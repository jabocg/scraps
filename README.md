# scraps
[Lil' Bits](https://www.youtube.com/watch?v=Gj4-E5Hs3Kc) of code that I might want to reuse. Feel free to steal them(with credit).

## Table of Contents
### Python
* [list comprehension building a string incrementally](#incremental-string-builder-link)
* [copy file using pathlib](#file-copy-via-pathlib-link)
* [recursively delete directory contents using pathlib](#delete-contents-via-pathlib-link)
* [recursively delete directory(and its contents)](#delete-directory-and-contents-via-pathlib-link)
* [compare simple versions](#compare-simple-versions-link)
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
  # NOTE: can replace five lines below with `deleteConents(path)` scrap form pathlib-recursive-remove-contents
  for i in path.glob('*'):
    if i.is_dir():
       deleteDirectory(i)
    else:
      i.unlink()
  path.rmdir()
```


#### Compare Simple Versions [[link]](https://github.com/jabocg/scraps/blob/master/python/compare-simple-versions.py)

Only works on numeric, dot separated versions(i.e. 1.0 vs 2.3.1.53). Will work
for any number of dots(given the recursion limit is high enough).

```python
def compare_ver(ver1, ver2):
    u"""Compare two versions.

    Assumes a x.y.z version structure, but can handle x.y vs x.y.z.
    Returns:
        -1 if ver1 < ver2
        0 if ver1 == ver2
        1 if ver1 > ver2

    """
    ver1_parts = [int(p) for p in ver1.split(u'.') if p is not u'']
    ver2_parts = [int(p) for p in ver2.split(u'.') if p is not u'']
    return comp_ver_rec(ver1_parts, ver2_parts)


def comp_ver_rec(v1, v2):
    u"""Recursively compare two pre-split versions."""
    if v1 == []:
        if v2[0] == 0:
            if len(v2) > 1:
                # ver2 has more parts than ver1, but they might be all 0's, so
                # we have to check the rest
                return comp_ver_rec(v1, v2[1:])
            # ver2 has more parts than ver1, but they are all 0's, so they're
            # the same
            return 0
        # ver2 has more parts than ver1, and they aren't 0's, so ver2 is newer
        return -1
    if v2 == []:
        if v1[0] == 0:
            if len(v1) > 1:
                # ver1 has more parts than ver2, but they might be all 0's, so
                # we have to check the rest
                return comp_ver_rec(v1[1:], v2)
            # ver1 has more parts than ver2, but they are all 0's, so they're
            # the same
            return 0
        # ver1 has more parts than ver2, and they aren't 0's, so ver1 is newer
        return 1
    if v1[0] > v2[0]:
        # ver1 has a newer part
        return 1
    if v1[0] < v2[0]:
        # ver2 has a newer part
        return -1
    if v1[0] == v2[0]:
        if len(v1) == 1 and len(v2) == 1:
            # ver1 and ver2 have the same part, and neither have more parts
            return 0
        # ver1 and ver2 have the same part, but they have more, so we check
        return comp_ver_rec(v1[1:], v2[1:])
```
