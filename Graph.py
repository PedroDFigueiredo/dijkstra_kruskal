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
	ant = {}
	queue = set()
	notVisited = {}
	inf = 999999

	def __init__(self, direct=True):
		self.isDirected = direct
		print("%s nodesraph Created!"%("Directed" if direct else "Undirected"))

	def addNode(self, ori, dest, weight):

		if ori not in self.nodes:
			self.nodes.update({ori: {dest:weight}})
		elif dest not in self.nodes[ori]:
			self.nodes[ori].update({dest:weight})
		else:
			self.nodes[ori].update({dest:self.nodes[ori][dest] + 1})

		if dest not in self.nodes:
			self.nodes.update({dest: {}})

		if ori not in self.queue:
			self.queue.add(ori)

		if dest not in self.queue:
			self.queue.add(dest)

	
	def weight(self, u, v):
		return self.nodes[u][v]


	def relax(self, u, v):
		#print("relax:")
		#print("%s->%d %d %s->%d "%(u,self.d[u], self.weight(u, v), v,self.d[v]))
		if self.d[u] + self.weight(u, v) <  self.d[v]:
			self.d.update({v:self.d[u] + self.weight(u, v)})
			self.notVisited.update({v:self.d[v]})
			self.pred.update({v:u})
			self.ant.update({u:v})


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

		return self.d, self.createPath()


	def buildGraphFromFile(self, filepath):

		file = open(filepath, "r")

		n, m = file.readline().split("\n")[0].split(" ")

		self.nEdges = m = int(m)
		self.nVertices = n = int(n)
		
		for i in range(0, m):
			line  = file.readline()
			ori, dest, weight = line.split("\n")[0].split(" ")

			ori = ori
			dest = dest

			self.addNode(ori, dest, int(weight))

		file.close()

	
		return self.nodes

	def createPath(self):

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

