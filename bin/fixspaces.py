#!/usr/bin/env python
import re, shutil, sys

def fix(path):
    shutil.copy(path, path + ".bak")
    fixed = []
    with open(path) as f:
        for line in f:
            line = line.rstrip()
            l = re.match(r"^[ \t]*", line).group()
            k = l.count(' ') + l.count('\t') * 4
            line = " " * k + line[len(l):]
            fixed.append(line)
    with open(path, 'w') as f:
        print >>f, "\n".join(fixed)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        fix(path)
