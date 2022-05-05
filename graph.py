from heapq import heapify,heappop,heappush,heapreplace


from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.neighors=defaultdict(list)
    def addEdge(self,initialNode,node):
        self.neighors[initialNode].append(node)
        self.neighors[node].append(initialNode)
node=Graph()
node.addEdge(0,1)
node.addEdge(0,2)
node.addEdge(0,7)
node.addEdge(1,8)
node.addEdge(1,4)
node.addEdge(1,3)
node.addEdge(3,6)
node.addEdge(5,3)
print(node.neighors)
        


