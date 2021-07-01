import os
import csv
import os.path
from os import path
def renameDirectories(sort):
    r = csv.reader(open(sort+'_labeled_studies.csv'))
    lines = list(r)
    for (line, label) in lines:
        dest = line.replace('MURA-v1.1/','')
        if not path.exists(dest):
            source = dest.replace('positive','negative')
            os.rename(source,dest)
renameDirectories('valid')
renameDirectories('train')
