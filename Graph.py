import numpy as np
import random
import math
#import matplotlib.pyplot as plt

class Graph:
	nEdges = 0
	nVertices = 0
	G = {}
	followers = {}
	isDirected = False
	coolingRate = 0.003
	temperature = 10000
	finalTemperature = 1
	connectionWeight = 20
	propagationProbability = 0.05

	k = 0

	def __init__(self, direct=True):
		self.isDirected = direct
		print("%s Network Created!"%("Directed" if direct else "Undirected"))


	def addNode(self, ori, dest, weight):

		if ori not in self.G:
			self.G.update({ori: {dest:weight}})
		elif dest not in self.G[ori]:
			self.G[ori].update({dest:weight})
		else:
			self.G[ori].update({dest:self.G[ori][dest] + 1})

		#if not self.isDirected:	
		if dest not in self.followers:
			self.followers.update({dest: {ori:weight}})
		elif ori not in self.followers[dest]:
			self.followers[dest].update({ori:weight})
		else:
			self.followers[dest].update({ori:self.followers[dest][ori] + 1})


	def getTopKHighestDregree(self, k=100):
		self.k = k
		count = 1
		# initialize the aux vector v with the first elem of de graph
		v = [list(self.G)[0]]
		k = k - 1
		for x in self.G:

			i = 0
			temp = 0
			while i < count and i < k:
				#print("lens: x:%d i:%d "%((len(self.G[x]["aavec"])), len(self.G[v[i]]["aavec"])))
				if len(self.G[x]) > len(self.G[v[i]]):
					e = k if (count + 1) > k else count
					j = e
					while j > i:
						#print("i:%d j:%d "%(i,j))
						if len(v) == j:
							#print("append")
							v.append(v[j-1])
						else:
							v[j] = v[j-1]

						j=j-1

					v[i] = x
					count = count + 1
					break

				i = i + 1

		S = {}	
		for w in v:
			S.update({w: self.G[w]})

		return S

	def getKNodesRandomly(self, k=100):
		self.k = k
		S = {}

		keys = list(self.G.keys())

		random.shuffle(keys)

		S = {}

		for i in range(k): 
			S.update({keys[i]:self.G[keys[i]]})

		return S

	def setPropagationProbability(self, prop):
		self.propagationProbability = prop
		for v in self.G:
			for follower in self.G[v]:
				self.G[v][follower] = prop

	def generatePropagationProbability(self):
		total = 0
		quant = 0
		for v in self.G:
			for follower in self.G[v]:

				count = 0 # number of nodes that follower follow
				for i in self.followers[follower]:	
					count = count + self.followers[follower][i]

				prop1 = ((100*self.G[v][follower])/count) # percent - conection between follower and v
			
				aux = (100*self.G[v][follower]/self.connectionWeight)
			
				prop = prop1 + aux # plus 
			
				self.G[v][follower] = float('{0:.3f}'.format(prop/100))

		# 		print()
		# 		print(v)
		# 		print(self.G[v])
		# 		print(follower)
		# 		print(self.followers[follower])
				
				#print("count:%d conect:%d prop:%f %s"%(v, follower, prop, self.G[v][follower]))

		# print(self.G)
		return prop

	def getPropagationProbability(self, node, next):
		count = 0
		if self.G[node][next] > random.random():
			return True
		else:
			return False


	def difusionFunction(self, seeds):

		target = [] #store active nodes
		active = [] #store unprocessed nodes intermediate time
		failedActivation = [] #only one chance to actiate a node
		result = {} 
		
		rand = random.random() * 0.1 

		for s in seeds:
			active.append(s)
		
		for s in seeds:
			target.append(s)
		
			aux = 0
		
			# while there are followers to influence
			while len(target) > 0:
				influencer = target.pop() # pick a influencer to check his followers, and active him
				if influencer not in active:
					active.append(influencer)

				if influencer in self.G:
					
					for follower in self.G[influencer]:
						
						# check the probability to influence a follower, and make him as active
						#aux = self.G[influencer][follower]

						#if self.connectionWeight <= aux:
						if self.getPropagationProbability(influencer, follower):
							if follower not in active and follower not in failedActivation:
								target.append(follower)

						else :
							failedActivation.append(follower)

			#result.update({s:{len(result):len(active)}})

		return  len(active)

	def buildGraphFromFile(self, filepath):

		file = open(filepath, "r")

		n, m = file.readline().split("\n")[0].split(" ")

		m = int(m)
		n = int(n)
		
		for i in range(0, m):
			line  = file.readline()
			ori, dest, weight = line.split("\n")[0].split(" ")

			ori = ori
			dest = dest

			self.addNode(ori, dest, int(weight))

		file.close()

		return self.G


	def F(self, G):
		S = G.copy()
		#print(list(S))

		keys = list(S.keys())

		random.shuffle(keys)

		S.pop(keys[0])

		keysg = list(self.G.keys())

		random.shuffle(keysg)

		count = 0
		key = keysg[count]
		count = 1
		while key in S:
			key = keysg[count]
			count = count +1

		S.update({key: self.G[key]})		
		#print(list(G))
		#print(list(S))
		return S

	def acceptanceProbability(self, energy, newEnergy, temperature) :
        # If the new solution is better, accept it
		if newEnergy > energy:
			return 1.0
		# If the new solution is worse, calculate an acceptance probability
		return math.exp((newEnergy - energy) / temperature)
    

	def simulatedAnnealing(self, S):

		bestG = S
		bestD = self.difusionFunction(S)

		temp = self.temperature
		t = 0
		A = S
		limit = 0
		d = 0
		count = 0
		while(temp > self.finalTemperature):
			Al = self.F(A)
			count = count + 1
			newEnergy = self.difusionFunction(Al)
			energy = self.difusionFunction(A)

			fitness = newEnergy - energy
			#print("f:%d  dl:%d d:%d"%(fitness, newEnergy, energy))
			rand = random.random()
			acept = self.acceptanceProbability(energy, newEnergy, temp)
			if acept  > rand :
				A = Al
			
			if bestD < newEnergy:
				bestD = newEnergy
				bestG = Al
		
			if count > limit:
				temp *= 1-self.coolingRate
				t = t + 1
				count = 0
			
			# print()
			# print(Al.keys())
			print("t:%d temp:%.6f ne:%d e:%d best:%d p:%f k:%d"%(t, temp, newEnergy, energy,  bestD, self.propagationProbability, self.k))

		return (bestG, bestD)




