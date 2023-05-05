#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

COUNT_FILE = os.path.join('../data/cycle', '.myprog.count')
if not os.path.exists(COUNT_FILE):
    num = 0
else:
    f = open(COUNT_FILE, 'r')
    num = int(f.read())
    f.close()

if num+1 > 2:
    print >>sys.stderr, "You have exceeded your %d uses"%(num,)
    sys.exit(0)

num += 1
f = open(COUNT_FILE, 'w')
f.write(str(num))
f.close()