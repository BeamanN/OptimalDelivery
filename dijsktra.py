#Program uses dijkstra's algorithm to find the shortest distance between points
 #For Function to work, have 3 parameters:
     #1: Graph - The Routes one can take to get from one point to another
     #2: Start - The starting point (Producer Location)
     #3: Goal - The destination/end point (Consumer Location)

def dijkstra(graph, start, end):
     #Records cost to reach node. Gets updated as you move along the graph
     shortest_distance = {} 

     #keeps track of the path that has led us to that specific node
     predecessor = {} 

     #Iterates throughout the entire graph 
     unseenNodes = graph 

     #Any Large Number will do for infintiy 
     infinity = float('inf')

     #Traces the journey back to the source node, is the optimal route(shortest distance)
     optimalPath = []

     for node in unseenNodes:
         shortest_distance[node] = infinity
     shortest_distance[start] = 0

     while unseenNodes:
         minNode = None
         for node in unseenNodes:
             if minNode is None:
                 minNode = node
             elif shortest_distance[node] < shortest_distance[minNode]:
                 minNode = node

         for childNode, weight in graph[minNode].items():
             if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                 shortest_distance[childNode] = weight + shortest_distance[minNode]
                 predecessor[childNode] = minNode
         unseenNodes.pop(minNode)

     currentNode = end
     while currentNode != start:
         try:
             optimalPath.insert(0, currentNode)
             currentNode = predecessor[currentNode]
         except KeyError:
             return 'Path not reachable'
     optimalPath.insert(0, start)
     if shortest_distance[end] != infinity:
         x = shortest_distance[end]
         y = optimalPath
         return f"Shortest distance is {x} with the path, {y}".format(x = shortest_distance[end], y = optimalPath)