# add mytool3.py to your python library

import os;

FILE_NAME = "mytool3.py";

code_file = open(FILE_NAME, "r");
dest_file = open(os.__file__.rsplit(os.sep, 1)[0] + os.sep + FILE_NAME, "w");

dest_file.write(code_file.read());

dest_file.close();
code_file.close();
