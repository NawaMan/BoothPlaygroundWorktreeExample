import sys

from greeter import greet

print(greet(sys.argv[1] if len(sys.argv) > 1 else "world"))
