# -*- coding: utf-8 -*-
import networkx as nx
from itertools import combinations    
from networkx.readwrite import json_graph
import community
import json
import sys

def searchBin(initYear, size, year):
    s = ''
    k = 0
    while s=='':
        if int(year) <= initYear+size*(k+1) and int(year)>initYear+size*(k): 
            s = str(initYear+size*(k))+'-'+str(initYear+size*(k+1)-1)
            return s
        else:
            k+=1
if len(sys.argv)==1:
    fileName = 'networksociocomplex.txt'
    outputName = 'networksociocomplex.json'
else:
    fileName = sys.argv[1]
    point = fileName[::-1].find('.')+1
    if point==0:
        outputName = fileName+'.json'
    else:
        outputName = fileName[:-point]+'.json'


f = open('./input_file/'+fileName,'r')
ArtInv = {}
for line in f:
    L = line.split('§')
    try:
        ArtInv[L[1]] = ArtInv.get(L[1],[])+[L[0]]
    except IndexError:
        print(L)
Gt = nx.Graph()

'''
for i in L:
    print i[:-1]+':  '+str(A[i])
print len(set(A))
'''

K = []
K2 = []
T = []
maxis_arts = 0
print(len(ArtInv))
for art in ArtInv:
    invs = ArtInv[art]
    if len(invs) == 1:
        if invs[0] not in Gt.nodes():
            Gt.add_node(invs[0],degree = 1.0)
            Gt.node[invs[0]]['Articles'] = [art]
        else:
            Gt.node[invs[0]]['degree'] = Gt.node[invs[0]].get('degree',0.0)+1.0
            Gt.node[invs[0]]['Articles'] = Gt.node[invs[0]].get('Articles',[])+[art] 
    for c in combinations(invs,2):
        if (c[0], c[1]) in Gt.edges():
            data = Gt.get_edge_data(c[0], c[1])
            Gt.add_edge(c[0], c[1], weight=data['weight']+1)
        else:
            Gt.add_edge(c[0], c[1], weight=1)
    for inv in invs:
        try:
            Gt.node[inv]['degree'] = Gt.node[inv].get('degree',0.0)+1.0
            Gt.node[inv]['Articles'] = Gt.node[inv].get('Articles',[])+[art] 
        except KeyError:
            print(Gt.edges(),'wfwfwfwr')

partition = community.best_partition(Gt)

for node in Gt:
    Gt.node[node]['Articles'] = list(set(Gt.node[node]['Articles']))
    print(node,partition[node])
    Gt.node[node]['Comunitat'] = partition[node]
#nx.set_node_attributes(Gt, 'Comunitat', partition)
Gt = json_graph.node_link_data(Gt)
json.dump(Gt, open('./output_json/'+outputName,'w'))
print(maxis_arts)

