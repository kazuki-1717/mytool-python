# from lazy_import import *

import subprocess

class lazy_import:
    """lazy_import 1.0.0"""

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
                raise Exception("move to except part.")

            self.module = __import__(self.module_name)
        except:
            # == install module if not found ==

            # convert types
            if (self.install_names == None):
                self.install_names = [self.module_name];
            
            elif (type(self.install_names) == str):
                self.install_names = [self.install_names];
            
            # install
            for name in self.install_names:
                subprocess.run(
                    ["py", "-m", "pip", "install", name, "--quiet"] + (["--upgrade"] if self.upgrade else []),
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
        return f"lazy_import({self.module_name}, {self.install_names})"



__all__ = ["lazy_import"]
