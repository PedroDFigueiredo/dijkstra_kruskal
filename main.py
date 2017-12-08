
#T0 = 10, 000, 000, 
#q = 1, 000,
#ΔT = 2, 000, 
#Tf = 1, 000, 000.

import time 
import sys
import numpy as np
import Graph


filepath = sys.argv[1]


# if len(sys.argv) >= 3:
# 	directed = True if sys.argv[2] == "d" else False
print(filepath)

G = Graph.Graph()


G.buildGraphFromFile(filepath)

S = G.nodes

print("\n::::::::::::::\n")


print(S)

# for w in S:
# 	print(w)
# 	print(S[w])

print("\n::::::::::::::\n")

# path = G.Dijkstra("A")

# print(path[0])
# print(path[1])

print(G.Kruskal())

