# explanations for these functions are provided in requirements.py
import random
from collections import deque

from graph import Graph

def get_diameter(graph: Graph) -> int:
	node = random.randint(0, graph.get_num_nodes())
	print(node)
	max = 0
	for i in range(0, 5):
		furthest_tuple = get_furthest_node(graph, node)
		if furthest_tuple[1] > max:
			max = furthest_tuple[1]
		node = furthest_tuple[0]
		print(f'iteration {i}, max: {max}, node: {node}')

	return max
	#raise NotImplementedError

def get_furthest_node(g: Graph, node: int) -> tuple[int, int]:
	q = deque()
	q.append(node)
	#print()
	distance = 0
	explored = {node}
	furthest = node
	while len(q) > 0:
		#distance += 1
		#print(explored)
		v = q.popleft()
		incremented = False
		for w in g.get_neighbors(v):
			if w not in explored:
				#print(explored)
				#print(f'{w} not in explored')
				if incremented == False:
					distance += 1
					#print(f'incremented is False, and distance is {distance}')
					incremented = True
					furthest = w
				
				explored.add(w)
				#print(explored)
				q.append(w)
	return (furthest, distance)

# 6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  w.parent := v
# 13                  Q.enqueue(w)

def get_clustering_coefficient(graph: Graph) -> float:
	raise NotImplementedError


def get_degree_distribution(graph: Graph) -> dict[int, int]:
	raise NotImplementedError


g = Graph(7, {(0, 1), (1, 2), (0, 2), (2,3), (0,3), (3,4), (4,5), (0,6), (6,7)})

#for edge in g.edges:
	#print(edge)
#neigh = g.get_neighbors(0)
print(g.get_neighbors(1))

print(get_diameter(g))