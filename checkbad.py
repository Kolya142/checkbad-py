#!/bin/python3
import os
files_list = []
cbignore = open("cbignore", 'r').read().replace('\n', '').replace(' ', '').split(';')

def rsearch(path: str):
    files = os.listdir(path)
    for file in files:
        if file in cbignore or file == "cbignore":
            continue
        _file = os.path.join(path, file)
        if os.path.isfile(_file):
            files_list.append(_file)
        else:
            rsearch(_file)

rsearch(os.getcwd())

for file in files_list:
    with open(file) as f:
        lines = f.read().split('\n')
        for index, line in enumerate(lines):
            _line = line.upper().replace(' ', '')
            if ("#BAD" in _line) or ("//BAD" in _line) or ("--BAD" in _line):
                print(f"warning: you MUST fix {file}:{index}")
