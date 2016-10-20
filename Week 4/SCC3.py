# -*- coding: utf-8 -*-
import time
from itertools import groupby
from collections import defaultdict

def dfs(input_graph,order,step):
    # Depth-First Search
    leader=dict()
    time=0
    finish_time=dict()
    visited=set()
    track=[]
    N=0
    for node in order:
        N+=1
        # if step==1:
        #     print("%.5f%% -- DFS for reverse graph"%(N/float(len(order))*100))
        # else:
        #     print("%.5f%% -- DFS for graph"%(N/float(len(order))*100))
        if node not in visited:
            current_source=node
            visited.add(node)
            leader[node]=current_source
            track.extend(list(set(input_graph[node])-visited))
            while track:
                p=track[-1]
                visited.add(p)
                leader[p]=current_source
                if not set(input_graph[p])-visited:
                    track.pop()
                    time+=1
                    finish_time[p]=time
                else:
                    track.extend(list(set(input_graph[p])-visited))
            time+=1
            finish_time[node]=time
    return finish_time,leader



def readgraph(lines):
    # Generate graph
    graph=defaultdict(list)
    N=0
    for line in lines:
        N+=1
        # print("%.5f%% -- Read graph"%(N/float(len(lines))*100))
        line=line.split()
        if line[0]!=line[1]:
            graph[int(line[0])].append(int(line[1]))
            # graph[line[1]]
    return graph

def reversegraph(lines):
    # Generate reverse graph
    regraph=defaultdict(list)
    N=0
    for line in lines:
        N+=1
        # print("%.5f%% -- Generate reverse graph"%(N/float(len(lines))*100))
        line=line.split()
        if line[0]!=line[1]:
            regraph[int(line[1])].append(int(line[0]))
            # regraph[line[0]]
    return regraph

def leader2SCC(leader_dict):
    # Obtain length of SCC (reverse order) and SCC
    SCC=defaultdict(list)
    for i,k in groupby(leader_dict.keys(),leader_dict.get):
        SCC[i].extend(list(k))
    SCC_len=sorted([len(SCC[x]) for x in SCC.keys()],reverse=True)
    while len(SCC_len)<5:
        SCC_len.append(0)
    return SCC,SCC_len


file=["SCC.txt"]
for file_name in file:
    # Record time
    t1=time.clock()
    # Read file
    f=open(file_name)
    lines=f.readlines()
    f.close()
    # Generate graph and reverse graph
    graph=readgraph(lines)
    regraph=reversegraph(lines)
    # DFS for reverse graph and count finish time
    finish_time_regraph,leader_regraph=dfs(regraph,sorted(regraph.keys(),reverse=True),1)
    # reorder finish time
    finishtime=[0]*len(finish_time_regraph)
    finishtime=sorted(finish_time_regraph,key=finish_time_regraph.get,reverse=True)
    # DFS for graph based on finish time to get SCC
    finish_time_graph,leader_graph=dfs(graph,finishtime,2)
    SCC,SCC_len=leader2SCC(leader_graph)
    t2=time.clock()
    # print and store result
    print(file_name+" result:")
    if len(SCC_len)>5:
        SCC_len=SCC_len[0:5]
    print(SCC_len)
    print("time: %.3f CPU seconds"%(t2-t1))
    f=open('result.txt','w')
    f.write('''
    "%s" results: %s
    time: %.3f CPU seconds
    '''%(file_name,SCC_len,t2-t1))
    f.close()
