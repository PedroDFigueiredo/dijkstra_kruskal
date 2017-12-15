
#T0 = 10, 000, 000, 
#q = 1, 000,
#ΔT = 2, 000, 
#Tf = 1, 000, 000.

import time 
import sys
import numpy as np
import Graph


filepath = sys.argv[1]

alg = int(sys.argv[2])

# if len(sys.argv) >= 3:
# 	directed = True if sys.argv[2] == "d" else False
print(filepath)

G = Graph.Graph()


G.buildGraphFromFile(filepath)

S = G.nodes


print(S)

print("\n::::::::::::::\n")

# for w in S:
# 	print(w)
# 	print(S[w])

if alg == 1:
	path = G.Dijkstra("a")
	print("Dijikstra")
	

	print(path[0])
	print(path[1])

else:
	print("Kruskal")
	print(G.Kruskal())

