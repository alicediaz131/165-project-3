
from collections.abc import Iterable

class Graph:
	num_nodes: int
	edges: set[tuple[int,int]]
	neighbors: list[set]
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.num_nodes = num_nodes
		self.edges = edges
		self.neighbors = [set() for _ in range(num_nodes)]
		for edge in edges:
			#if edge[0] == node:
			self.neighbors[edge[0]].add(edge[1])
			self.neighbors[edge[1]].add(edge[0])

			

	def get_num_nodes(self) -> int:
		return self.num_nodes

	def get_num_edges(self) -> int:
		return len(self.edges)

	def get_degree(self, v: int) -> int:
		return len(self.neighbors[v])
				
	def get_neighbors(self, node: int) -> Iterable[int]:
		return self.neighbors[node]
	
	def insert_edge(self, edge: tuple[int, int]):
		self.edges.extend(edge)
		return
	
	def are_neighbors(self, u, w):
		return w in self.neighbors[u]
