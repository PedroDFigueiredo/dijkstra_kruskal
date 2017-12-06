
#T0 = 10, 000, 000, 
#q = 1, 000,
#ΔT = 2, 000, 
#Tf = 1, 000, 000.

import time 
import sys
import numpy as np
import Graph


filepath = sys.argv[1]

directed = False

# if len(sys.argv) >= 3:
# 	directed = True if sys.argv[2] == "d" else False

G = Graph.Graph(True)


a = time.time()
G.buildGraphFromFile(filepath)
b = time.time()
S = G.nodes


for w in S:
	print(w)
	print(S[w])

print("\n::::::::::::::\n")
path = G.Dijkstra("A")

print(path[0])
print(path[1])

print("\nbuild time: %f "%(b-a))

