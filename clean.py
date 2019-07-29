import multiprocessing as mp
from tqdm import tqdm
import sys
import os

def filt(x):
    if len(x) == 0:
        return ""
    return os.popen("c++filt " + x).read()[0:-1]

log = open(sys.argv[1]).read().split("\n")

def process_row(row):
    if len(row) == 0:
        return ("", [""])
    if row[0] != "[":
        return ("", [""])
    r = row.split(": ")
    r[0] = filt(r[0][1:-1])
    r[1] = [filt(x[1:-1]) for x in r[1].split(", ")]
    return (r[0], r[1])

pool = mp.Pool()
calls = dict(list(tqdm(pool.imap(process_row, log), total=len(log))))

for caller in calls.keys():
    for callee in calls[caller]:
        print('"' + caller + '" -> "' + callee + '"')
