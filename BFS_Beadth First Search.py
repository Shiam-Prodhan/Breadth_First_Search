# Submitted By : Shiam Prodhan (181014123)

import collections #import packages

#Initializing the graph
graph = {
    1 : [2,3],
    2 : [4, 5, 6, 7],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : []
}

visited = [] # visited nodes are stored here
queue = []   # this queue is used to queue and deque the vertexes

# Function for the Breadth First Search
def Breadth_First_Search(visited, graph, node):
  visited.append(node) 
  queue.append(node)

  # Dequeue a vertex from queue
  while queue:
    s = queue.pop(0)   # dequeing the vertex
    print (s, end = " ") # printing the vertex
    
    # If the vertex is not visited, mark it as visited, and enqueue it in the queue
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        
print("Breadth First Traversal is : ", end = " ")
Breadth_First_Search(visited, graph, 1)

