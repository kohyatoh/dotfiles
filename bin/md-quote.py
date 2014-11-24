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

def cut(path, i, j):
    with open(path) as f:
        lines = f.readlines()
        if j == -1:
            j = len(lines) - 1
        indent = min_indent(lines[i:j+1])
        while i <= j:
            l = lines[i].rstrip()
            if l != "":
                l = l[indent:]
            print "    %02d  %s" % (i+1, l)
            i += 1

path = sys.argv[1]
begin = int(sys.argv[2]) - 1 if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) - 1 if len(sys.argv) > 3 else -1

print "    %s" % path
cut(path, begin, end)
