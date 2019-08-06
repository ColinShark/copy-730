import os
from distutils.dir_util import copy_tree

src = "458696672"
sub = "730"

for folder in next(os.walk('.'))[1]:
    if folder != src:
        print(copy_tree(f"{src}/{sub}", f"{folder}/{sub}"))

input("Press <enter> to quit...")
quit(0)
