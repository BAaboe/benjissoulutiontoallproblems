#!/usr/bin/env python

import os
import glob

files = glob.glob("")

for file in files:
    old = file
    extension = file.split(".")[-1]
    new = ""  
    if file.contains("-"):
        file = file.split("-")[-1]
    file = file.replace("\n", "")
    ep = file.split(".")
    try:
        ep = int(ep)
        if str(ep).startswith("0"):
            new = f"{str(ep)}.{extension}"
        elif ep < 10:
            new = f"0{ep}.{extension}"
        os.rename(old, new)
    except ValueError:
        print("dont knwo ep")

