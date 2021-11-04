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

visited = set() # visited nodes are stored here

# Function for the Depth First Search
def Depth_First_Search(visited, graph, node):
    if node not in visited: # checking if the node is in visited or not
        print (node, end = " ") # if the node is not in visited then print it
        visited.add(node) # node added to the visited
        
        # If the vertex is not visited, mark it as visited
        for neighbour in graph[node]:
            Depth_First_Search(visited, graph, neighbour)

print("Depth First Traversal is : ", end = " ")
Depth_First_Search(visited, graph, 1)




