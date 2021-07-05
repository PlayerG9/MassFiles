# MassFiles
 Editor to manage a complex Project
 [View Website](https://playerg9.github.io/MassFiles/)

![Python](README.assets/Python.png)


# FileStructure
## file.zip  
```text
+ images
| + image.png
+ files
| + hello_world.tktxt
| + hello_world
| | + hello_world_child.tktxt
+ configs
| + settings.json
```

## file.tktxt (pickle)
```text
(key, value, index)
(key, value, index)
(key, value, index)
```
Possible keys:
- tagon / tagoff
  - followed by tag-data as pydict  
    example: `{'foreground': 'blue'}`
- mark
- text
- image
  - followed by pydict  
    `{'filename': 'image.png', 'size': [X, X], 'rotation': int, 'data': bytes}`