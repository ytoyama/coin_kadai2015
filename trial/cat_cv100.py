#!/usr/bin/env python3

import os
import os.path
import re

for currentFile in [fileInDir for fileInDir in os.listdir(".")
    if os.path.isfile(fileInDir) and re.match("cv000", fileInDir)]:
  with open(currentFile) as openedFile:
    print(openedFile.read())
