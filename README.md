# mytool

some useful methods for python interpreter, this install require library dynamically

| mytool | python 4.0.0 |
| ------ | ------------ |
| update | 2026-06-10   |

## How to install

```
git clone https://github.com/kazuki1717/mytool-python
py mytool-python/add_to_library.py
```

## import

```python
from mytool import *
```

---

## Methods

### lazy_import

| method                                | usage                                                               |
| ------------------------------------- | ------------------------------------------------------------------- |
| `module = lazy_import(module_name)` | import module when use, and install library if module not installed |

### objects methods

| method                 | usage                                  |
| ---------------------- | -------------------------------------- |
| object_methods(object) | show `object`  methods              |
| object_details(object) | show `object` translated description |

### OS methods

| method        | alias       | usage                                                           |
| ------------- | ----------- | --------------------------------------------------------------- |
| cd(path)      | chdir(path) | change currently directory                                      |
| clear         | cls         | clear terminal, no () needed                                    |
| listdir(path) | ls          | list items in path, no () needed if looking currectly directory |
| touch(file)   |             | create file                                                     |

### video methods

a cv2.VideoCapture extend, not directly extend from VideoCapture since lazy import

| method                                    | alias      | usage                                                 |
| ----------------------------------------- | ---------- | ----------------------------------------------------- |
| video = video_t(source)                   |            | load video from file, default asking file in explorer |
| video.width                               |            |                                                       |
| video.height                              |            |                                                       |
| video.fps                                 |            |                                                       |
| video.duration                            | video.rate |                                                       |
| video.set_pos(pos)                        |            |                                                       |
| video.play(window_name, fullscreen, loop) |            | play video in new window                              |
| video.to_cv2_images()                     |            | convert frames to cv2 images list                     |
| video.to_pil_images()                     |            | convert frames to pil image list                      |
| video.write_mp4(output,fps,width,height)  |            | write mp4                                             |
| video.write_gif(output,loop)              |            | write gif                                             |

## ライセンス

MIT License
