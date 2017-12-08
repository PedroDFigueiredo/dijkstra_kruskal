import numpy as np
import random
import math
import collections
#import matplotlib.pyplot as plt

class Graph:
	nEdges = 0
	nVertices = 0
	nodes = {}
	d = {}   #distances
	pred = {}
	queue = set()
	notVisited = {}
	inf = 999999

	def __init__(self, direct=True):
		self.isDirected = direct
		print("%s graph Created!"%("Directed" if direct else "Undirected"))

	
	
	def weight(self, u, v):
		return self.nodes[u][v]


	def relax(self, u, v):
		#print("\nrelax:")
		#print(self.notVisited)
		#print("%s->%d %d %s->%d "%(u,self.d[u], self.weight(u, v), v,self.d[v]))
		if self.d[u] + self.weight(u, v) <  self.d[v]:
			self.d.update({v:self.d[u] + self.weight(u, v)})
			self.notVisited.update({v:self.d[v]})
			self.pred.update({v:u})


	def Dijkstra(self, startV):
		print("Start vertex: %s\n"%startV)
		S = self.nodes
		
		for i in S:
			self.d.update({i:self.inf})

		self.notVisited = dict(self.d)

		self.d.update({startV:0})
		self.notVisited.update({startV:0})

		while self.notVisited:
			v  = min(self.notVisited, key=self.notVisited.get)

			for u in self.nodes[v]:
				self.relax(v , u)

			del self.notVisited[v]

		return self.d, self.createDijkPath()


	def buildGraphFromFile(self, filepath):

		file = open(filepath, "r")

		for line in file.readlines():
			aux = line.split(" ")
			if len(aux) < 3:
				self.addNode_(aux[0].replace("\n", ""))
			else:
				self.addNode(aux[0], aux[1], int(aux[2].replace("\n", ""))	)

		file.close()
		
		return self.nodes

	def addNode_(self, ori):
		if ori not in self.nodes:
			self.nodes.update({ori: {}})

	def addNode(self, ori, dest, weight):
		print("%s %s %s"%(ori, dest, weight))
		if ori not in self.nodes:
			self.nodes.update({ori: {dest:weight}})
		else:
			self.nodes[ori].update({dest:weight})

		if dest not in self.nodes:
			self.nodes.update({dest:{}})

		if ori not in self.queue:
			self.queue.add(ori)

		if dest not in self.queue:
			self.queue.add(dest)

		print(self.nodes)

	def createDijkPath(self):

		self.notVisited = dict(self.d)
		temp = {}

		for i in self.pred:
			if self.pred[i] not in temp:
				temp.update({self.pred[i]: [i]})
			else:
				temp[self.pred[i]].append(i)

		aux = []

		while temp:
			v  = min(self.notVisited, key=self.notVisited.get)

			del self.notVisited[v]
			if v in temp:
				for i in temp[v]:
					aux.append(("%s -> %s"%(v,i)))

				del temp[v]
		
		return aux

	def Kruskal(self):
		parent = dict()
		rank = dict()
		sortedEdges = list()
		
		def findSet(v):
			if parent[v] != v:
				parent[v] = findSet(parent[v])
			return parent[v]

		def union(u, v):
			root1 = findSet(u)
			root2 = findSet(v)
			if root1 != root2:
				if rank[root1] > rank[root2]:
					parent[root2] = root1
				else:
					parent[root1] = root2
			if rank[root1] == rank[root2]: 
				rank[root2] += 1

		
		for v in self.nodes:
			for u in self.nodes[v]:
				sortedEdges.append((self.nodes[v][u], v, u))
				rank[v] = 0
			rank[u] = 0
			parent[v] = v

		sortedEdges.sort()
		
		print("edges")
		print(sortedEdges)
		print("\nparent ")
		print(parent)
		print("\nrank ")
		print(rank)
		print("\njoe1 ")
		
		self.mst = set()
		for edge in sortedEdges:
			w, u, v = edge
			
			if findSet(u) != findSet(v):
				union(u, v)
				self.mst.add(edge)
		
		return sorted(self.mst)

		