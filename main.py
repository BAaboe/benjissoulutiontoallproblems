#!/usr/bin/env python

import os

files = os.listdir(os.getcwdb())

for file in files:
    if os.path(os.path.abspath(file)):
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

