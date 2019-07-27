import sys
import os

def filt(x):
    if len(x) == 0:
        return ""
    return os.popen("c++filt " + x).read()[0:-1]

log = open(sys.argv[1]).read().split("\n")

calls = {}
for row in log:
    if len(row) == 0:
        continue
    if row[0] != "[":
        continue
    r = row.split(": ")
    r[0] = filt(r[0][1:-1])
    r[1] = [filt(x[1:-1]) for x in r[1].split(", ")]
    calls[r[0]] = r[1]

for caller in calls.keys():
    for callee in calls[caller]:
        print('"' + caller + '" -> "' + callee + '"')
