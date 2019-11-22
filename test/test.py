#!/usr/bin/env python
import sys
import os

print(sys.path)
print(sys.executable)
print(os.path.join('foo', 'bar.py'))

import util

if __name__ == "__main__":
   print("hello")
