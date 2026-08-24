import sys

from A_lecture_my_library import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
else:
    sys.exit()