#!/usr/bin/env python
import csv
from collections import defaultdict

infile = file("/Users/alexaheekes/Masters/Files/MHCGeneList_biomaRt.txt",'r')
outfile= open("/Users/alexaheekes/Masters/Files/MHCGeneList.txt",'w')
f_in = csv.reader(infile,delimiter="\t")
f_out = csv.writer(outfile,delimiter="\t")

header = infile.readline().strip("\n")
colnames = header.split("\t")
n = 8

id_annot = defaultdict(list)
id_go = defaultdict(list)
ids = set()
for row in f_in:
    id = row[0]
    go = row[n]
    id_annot[id].append([row[i] for i in range(n)])
    id_go[id].append(go)
    ids.add(id)  
#print len(ids), len(id_go),len(id_annot)
f_out.writerows([colnames])
for i in id_annot:
    annotations = id_annot[i][0]
    go_terms = filter(None,id_go[i])
    annotations.append(go_terms)
    f_out.writerows([annotations])
	