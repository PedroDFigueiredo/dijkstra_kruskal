
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

graph = Graph.Graph(True)



a = time.time()
graph.buildGraphFromFile(filepath)
b = time.time()

# for w in S:
# 	print(w)
# 	print(S[w])
print(graph.G)
print("build time: %f "%(b-a))
k = 10
p = 0.05
