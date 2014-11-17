#!/usr/bin/env python
import re
import sys

def min_indent(lines):
    a = len(lines[0])
    for l in lines:
        if l.rstrip() == "":
            continue
        m = re.match("^ *", l).group()
        a = min(a, len(m))
    return a

for line in sys.stdin:
    if line.startswith("#include"):
        _, path, _, _i, _, _j = line.strip().split(" ")
        i = int(_i) - 1
        j = int(_j) - 1
        with open(path) as f:
            lines = f.readlines()
            indent = min_indent(lines[i:j+1])
            while i <= j:
                l = lines[i].rstrip()
                if l != "":
                    l = l[indent:]
                print "    %d  %s" % (i+1, l)
                i += 1
    else:
        sys.stdout.write(line)
