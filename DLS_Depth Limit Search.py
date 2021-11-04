#!/usr/bin/env pytho# Submitted By : Shiam Prodhan (181014123)

import collections

graph = {
    1 : [2,3],
    2 : [4, 5, 6, 7],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : []
}

# Function for the Depth Limit Search
def Depth_Limit_Search(start,Destination,path,level,maximumDepth):
  print("\nCurrent level : ",level)
  print("Destination node testing for : ",start)
  path.append(start)
  if start == Destination: # Cheking if the start node is same as the Destintaion or not
    print("Successful!")
    return path
  print("Testing failed!") 
  if level==maximumDepth:# Cheking if the level is same as the maximumDepth or not
    return False
  print("\nExpanding the current node",start)
    
  # This loop is used for returing the path if the any path is available  
  for child in graph[start]:
    if Depth_Limit_Search(child,Destination,path,level+1,maximumDepth):
      return path
    path.pop()
  return False
  
  
  
start = 1 # Starting with node 1
Destination = input("Enter the Destination node : ") #Taking the destination node
maximumDepth = int(input("Enter the maximum depth limit : ")) # Set up the maximum depth limit
print() # printing a blank line
path = list() #initializing the path in a list
result = Depth_Limit_Search(start,Destination,path,0,maximumDepth)  # storing the value of the vertex by calling the function and storing it in a variable
if(result):  #Cheking if result is true
    print()
    print("--------------------------------------")
    print("Path to Destination node is available")
    print("Path is : ",path)
    print("--------------------------------------")
else:
    print()
    print("--------------------------")
    print("Sorry, No path available!")
    print("--------------------------")


# In[ ]:




