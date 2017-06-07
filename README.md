# scraps
[Lil' Bits](https://www.youtube.com/watch?v=Gj4-E5Hs3Kc) of code that I might want to reuse. Feel free to steal them(with credit).

## Table of Contents
### Python
* [list comprehension building a string incrementally](#incremental-string-builder)
### Java
### C#

<br>
<hr>
<br>


## Python

#### Incremental String Builder [*](https://github.com/jabocg/scraps/blob/master/python/incremental-string-builder.py)
```python
[string[:i] for i in range(1, len(string))]
```

#### File copy via `pathlib` [*](https://github.com/jabocg/scraps/blob/master/python/pathlib-copy-file.py)
```python
import pathlib

# source: pathlib.Path - source file to get contents of
# dest: pathlib.Path - destination file to put contents in
def copyFile(source, dest):
  with source.open() as i:
    with dest.open(mode='w') as o:
      o.write(i.read())
```
