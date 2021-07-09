# Project-File Structure

```text
Project.nb
+ files
| + a.md
| | + a-child.tktext
| | | + file   (file of 'a-child.tktext')
| | | + config   (config of 'a-child.tktext')
| | + file   (file of 'a.md')
| | + config   (config of 'a.md')
+ filepath   (contains the path to the project-file | only when opened)
+ 507ecc30-d063-4ba2-97dc-214b074dc677   (example | unique project-id)
```

to open a file in the project:
a: 
```python
with open('files/a.md/file', 'r', encoding='utf-16') as file:
    content = file.read()
...
```
b:
```python
file = open('files/a.md/file', 'r', encoding='utf-16')
content = file.read()
file.close()
```
