#! python 3

import os, sys, subprocess
from Bio.Align.Applications import MuscleCommandline, ClustalOmegaCommandline
from math import ceil

loc = input('Target: ')
tod = input('protein or dna?: ')
if tod == 'dna':
    ask = input('first word after species name: ')
os.chdir(loc)

for file in os.listdir('.'): # merge files
    if file.endswith('.fa' or '.fasta' or '.fas'):
        fasta = open(file, 'r')
        lines = fasta.readlines()
        lines = ''.join(lines) + '\n'
        nfile = open('combined.fas', 'a')
        nfile.write(lines)
        nfile.close()

def subp(a):
    child = subprocess.Popen(str(a),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            shell=(sys.platform!="win32"))
    child.communicate()

# MUSCLE alignment
def Muscle():
    muscle_exe = 'C://Windows//System32//muscle3.8.31_i86win32.exe'
    muscle_cline = MuscleCommandline(muscle_exe, input="combined.fas", out='aligned.fas')
    subp(muscle_cline)

# ClustalO alignment
def ClustalO():
    clustalO_exe = 'C://clustal-omega-1.2.2-win64//clustalo.exe'
    clustalO_cline = ClustalOmegaCommandline(clustalO_exe, infile='combined.fas', outfile='aligned.fas')
    subp(clustalO_cline)

ask_align = input('ClustalO or Muscle?(c/m): ')
Muscle() if ask_align.lower() == 'm' else ClustalO()

# Recombines align file

recombine = open('aligned.fas', 'r+')
lines = recombine.readlines()
recombine.truncate(0)

def frag(i): # finds species names
    if tod.lower() == 'protein':
        fr = i[i.find('[')+1 : i.find(']')]
    elif tod.lower() == 'dna':
        i = i.replace('PREDICTED: ', '')
        fr = i[i.find(' ')+1 : i.find(ask)-1]
    fr = fr.replace(' ', '_')
    return fr

tag_list = []
for i in lines:
    if i.startswith('>'):
        fr = frag(i)
        tag_list.append(fr)
tag_max = len(max(tag_list, key=len))

ne = '' # data for nexus
ne2 = '' # taxalist for nexus
for i in lines:
    recombine = open('aligned.fas', 'a')
    if i.startswith('>'):
        li = lines.index(i)
        fr = frag(i)        
        if li == 0:            
            e = '>' + fr + '\n' # recombine for fasta
            e2 = fr + ' '*(tag_max-len(fr)) + '\t' # recombine for nexus data
            ne += e2      
        else:
            e = '\n' +'>' +  fr + '\n'
            e2 = '\n' + fr + ' '*(tag_max-len(fr)) + '\t'
            ne += e2
        e3 = '\t\t' + fr + '\n' # recombine for nexus taxalist
        ne2 += e3
        recombine.write(e)
    else:
        i = i.strip() # sequences
        ne += i
        recombine.write(i)
    recombine.close()

# Creates Nexus file

PNex = open('aligned.nex', 'w')
PNex.write(ne)
PNex.close()
PNex = open('aligned.nex', 'r+')
lines = PNex.readlines()
PNex.truncate(0)
PNex.close()

ntax = len(lines)
fr = lines[0][lines[0].find('\t')+1:]
nchar = len(fr)-1
interleave = input('Interleave (yes/no): ') if nchar > 100 else 'no'
top = f'#NEXUS\n\nbegin taxa;\n\tdimensions ntax={ntax};\n\ttaxlabels\n{ne2};\nend;\
\nbegin characters;\n\tdimensions nchar={nchar};\n\tformat missing=? gap=- datatype={tod}\
 interleave={interleave.lower()};\n\tmatrix\n\n'
bttm = '\n;\nend;'
Nex = open('aligned.nex', 'a')
Nex.write(top)

if interleave.lower() == 'yes' and nchar > 100:
    tags = {}
    for i in lines:
        e = i[:i.find('\t')+1]
        r = i[i.find('\t')+1:]
        r = r.strip('\n')
        chunks, chunks_size = len(r), 100
        r1 = [ r[j:j+chunks_size] for j in range(0, chunks, chunks_size) ]
        r1 = [a for a in r1 if a not in ('')]
        tags.setdefault(e, r1)
    for t in range(0, ceil(chunks/chunks_size)):
        for y in range(0, len(lines)):
            Nex.write((list(tags)[y] + ''.join(list(tags.values())[y][t]) + '\n'))
        Nex.write('\n')
else:
    Nex.writelines(lines) 
Nex.write(bttm)
Nex.close()