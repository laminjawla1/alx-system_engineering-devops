#!/usr/bin/env python3
import sys
import re


message = sys.argv[1]

pattern = r'\[from:([^]]+)] \[to:([^]]+)] \[flags:([^]]+)]'

match = re.search(pattern, message)

if match:
    _from = match.group(1)
    _to = match.group(2);
    _flags = match.group(3)
    print(f"{_from},{_to},{_flags}")
else:
  print()
