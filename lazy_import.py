# from lazy_import import *

import subprocess
import sys
import importlib

class lazy_import:
    """lazy_import 1.0.0

import module when use, also install library if module not installed

usage:
```
module = lazy_import(
    "module_name",              # import module by this
    ["install_option1", ...],   # if "module_name" not exist, installs modules by this list (default: refer to module_name)
    /,
    upgrade = False              # always upgrade module before import (default: false)
)
```


samples:
```python
# there are only lazy_import in lazy_import.__all__
from lazy_import import lazy_import

# import numpy. install numpy if not existed
numpy = lazy_import("numpy")

# import cv2. install opencv2-python if not existed
cv2 = lazy_import("cv2", "opencv2-python")

# import matplotlib.pyplot as plt. install matplotlib if not existed
plt = lazy_import("matplotlib.pyplot", "matplotlib")

# import pydub. install ffmpeg and pydub if not existed
pydub = lazy_import("pydub", ["ffmpeg", "pydub"])

# always upgrade pytube before import pytube**
pytube = lazy_import("pytube", upgrade = True)
```
"""

    registered = []

    def __init__(self, module_name: str|None, install_names: list|str|None = None, /, upgrade = False):
        if (module_name == None):
            raise Exception("error: module name cannot be None")
        
        self.registered.append(module_name)
        
        self.module_name = module_name
        self.install_names = install_names
        self.module = None
        self.upgrade = upgrade

    def _import(self):
        # exit if module already imported
        if (self.module != None):
            return;
    
        try:
            # == try to import module ==

            if (self.upgrade):
                raise ImportError("move to except part.")

            self.module = importlib.import_module(self.module_name)
        except (ImportError, ModuleNotFoundError):
            # == install module if not found ==

            # convert types
            if (self.install_names == None):
                self.install_names = [self.module_name];
            
            elif (type(self.install_names) == str):
                self.install_names = [self.install_names];
            
            # install
            for name in self.install_names:
                subprocess.run(
                    [sys.execuatable, "-m", "pip", "install", name, "--quiet"] + (["--upgrade"] if self.upgrade else []),
                    stdout = subprocess.DEVNULL,
                    stderr = subprocess.DEVNULL
                );

            self.module = importlib.import_module(self.module_name);

    def __getattr__(self, attr_name):
        self._import();
        return getattr(self.module, attr_name);

    def __dir__(self):
        self._import();
        return dir(self.module);

    def __repr__(self):
        return "lazy_import(%s, %s%s)" % (
            self.module_name, self.install_names, " upgrade = true" if self.upgrade else ""
        )



__all__ = ["lazy_import"]
