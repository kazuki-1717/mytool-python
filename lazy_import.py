# from lazy_import import *

import subprocess

class lazy_import:
    def __init__(self, module_name: str|None, install_name: str|None = None):
        if (module_name == None):
            raise Exception("error: module name cannot be None")
        
        self.module_name = module_name
        self.install_name = install_name
        self.module = None

    def _import(self):
        try:
            # == try to import module ==

            self.module = __import__(self.module_name)
        except:
            # == install module if not found ==

            if (install_name == None):
                install_name = self.module_name;
            
            subprocess.run(
                ["py", "-m", "pip", "install", install_name, "--quiet"],
                stdout = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL
            );

            self.module = __import__(self.module_name);

    def __getattr__(self, attr_name):
        self._import();
        return getattr(self.module, attr_name);

    def __dir__(self):
        self._import();
        return dir(self.module);

    def __repr__(self):
        return f"lazy_import({self.module_name})"


__all__ = ["lazy_import"]
