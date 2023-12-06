#!/bin/python3
import subprocess

a=subprocess.check_output(["make","pass"]).decode().split("\n")[1].split(" ")[2]
print(a)
