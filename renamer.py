import os
import csv
import os.path
from os import path
def renameDirectories(sort):
    r = csv.reader(open(sort+'_labeled_studies.csv')) # Here your csv file
    lines = list(r)
    for (line, label) in lines:
        if not path.exists(line):
            dest = line.replace('MURA-v1.1/','')
            source = dest.replace('positive','negative')
            os.rename(source,dest)
renameDirectories('valid')
renameDirectories('train')