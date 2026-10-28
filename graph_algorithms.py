# explanations for these functions are provided in requirements.py
import random
from collections import deque

from graph import Graph

def get_diameter(graph: Graph) -> int:
	node = random.randint(0, graph.get_num_nodes()-1)
	#print(f'random is {node}')
	max = 0
	for i in range(0, 10):
		furthest_tuple = get_furthest_node(graph, node)
		if furthest_tuple[1] > max:
			max = furthest_tuple[1]
		node = furthest_tuple[0]
		##print(f'iteration {i}, max: {max}, node: {node}')

	return max
	#raise NotImplementedError

def get_furthest_node(g: Graph, node: int) -> tuple[int, int]:
	q = deque()
	q.append(node)
	###print()
	distance = -1
	explored = set()
	explored.add(node)
	furthest = node
	layer_end = 1
	layer_counter = 0
	while len(q) > 0:
		#distance += 1
		##print(explored)
		
		v = q.popleft()
		layer_end = layer_end - 1
		##print(f'v is now {v}')
		#incremented = False
		
		for w in g.get_neighbors(v):
			if w not in explored:
				##print(explored)
				##print(f'{w} not in explored')
				# if incremented == False:
				# 	distance += 1
				# 	#print(f'incremented is False, {w} not in explored, for v:{v} and distance is {distance}')
				# 	incremented = True
				# 	furthest = w
				
				explored.add(w)
				##print(explored)
				q.append(w)
				layer_counter = layer_counter+1
				furthest = w
		if layer_end == 0:
			##print(f"layer_end is 0, layer_counter is {layer_counter}")
			layer_end = layer_counter
			layer_counter = 0
			distance += 1
		
	return (furthest, distance)


def get_clustering_coefficient(graph: Graph) -> float:
	#C = 3*number of triangles / number of 2-edge paths
	triangles = 0
	L, N = get_degen_ordering(graph)
	##print(L)
	##print(N)
	for v in reversed(L):
		#For each pair of vertices, u and w, adjacent to v and earlier in the ordering, 
		# i.e., u and v are in the list Nv from the degeneracy algorithm:
		##print(f"v: {v}")
		for i in range (len(N[v])):
			for j in range (i+1, len(N[v])):
				u = N[v][i]
				w = N[v][j]
				if graph.are_neighbors(u,w):
					triangles = triangles+1
					##print("u and w are neighbors and u != w")
	paths = 0
	for v in range (graph.get_num_nodes()):
		degv = graph.get_degree(v)
		paths = paths + (degv*(degv-1)/2)
	return float(3*triangles/paths)

def get_degen_ordering(g: Graph):
	n = g.get_num_nodes() #n is number of vertices

	L = [] #ordering of vertices we return
	HL = set() #hash set for L
	d = [0]*n #compute a number d[v] for each vertex v in G which is the number of neighbors that are not yet in L. Initially just the degrees of v.
	D = [set() for _ in range(n)] # D[i] contains a list of the vertices v that are not already in L for which dv = i.
	#set it to equal n-1 empty lists just in case. could probably do better in terms of space efficiency... 
	#this assumes a node could have as many neighbors as possible
	for v in range (n):
		d[v] = g.get_degree(v)#len(g.get_neighbors(v))
		D[d[v]].add(v) #place vertex a at degree equal to it's calculated neighbors. do this for all nodes.

	
	N = [[] for _ in range(n)] #Initially, Nv is empty for every vertex v.
	

	k = 0
	i = 0

	for ind in range (0, n):
		#Let i be the smallest index such that D[i] is nonempty.
		#i = -1
		while i < n and not D[i]:
			i += 1
		
		if i == n:
			break
		#i = smallest_index
		k = max(k,i)
		#Select a vertex v from D[i]. 
		if i == -1:
			break
		v = D[i].pop()

		#Add v to the beginning of L and remove it from D[i]. 
		L.append(v) #instead of adding to the beginning of L, add to the end so that you don't have to push the entire list up 1. just remember to use it in reverse later...
		#Mark v as being in L (e.g., using a hash table, HL).
		HL.add(v)
		
		#For each neighbor w of v not already in L

		neighbors = [w for w in g.get_neighbors(v) if w not in HL]
		for w in neighbors:

			D[d[w]].remove(w)

			d[w] = d[w] - 1
			if d[w] < i:
   				i = d[w]
			D[d[w]].add(w)
			N[v].append(w)

	return L, N
	
	

def get_degree_distribution(graph: Graph) -> dict[int, int]:
	n = graph.get_num_nodes() #n is number of vertices
	H = dict()
	for v in range (n):
		dv = graph.get_degree(v)#len(graph.get_neighbors(v))
		if dv not in H:
			H.update({dv: 1})
		else:
			H.update({dv: H[dv] + 1})
	return H 
