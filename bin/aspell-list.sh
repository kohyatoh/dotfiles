#!/bin/bash

for f in $*; do
  echo "$f:"
  aspell -l en -t list < $f | sort | uniq 
  echo ""
done
