from tkinter import *
from main import *
import random

authorized_employees = {"Joe": "5893023", "Beaman": "1938472", "Faraz": "3948353", "Chris": "395593"}
x = input("Enter your id number: ")
if (x not in list(authorized_employees.values())):
    print("Invalid User ID")
    print("NO ACCESS")
    quit()
else:
    paths = {
        'a': {'b': 3, 'c': 4, 'd': 7},
        'b': {'c': 1, 'f': 5},
        'c': {'f': 6, 'd': 2},
        'd': {'e': 3, 'g': 6},
        'e': {'g': 3, 'h': 4},
        'f': {'e': 1, 'h': 8},
        'g': {'h': 2},
        'h': {'g': 2}
    }
    p = random.randint(1, 103)
    listofKeys = list(paths.keys())
    if (p == 1):
        num = random.randint(0, len(paths))
        while (num >= 0):
            num -= 1
            paths.pop(listofKeys[random.randint(0, len(paths) - 1)])


graph = {
    'a': {'b':3,'c':4, 'd':7},
    'b': {'c':1,'f':5},
    'c': {'f':6,'d':2},
    'd': {'e':3,'g':6},
    'e': {'g':3,'h':4},
    'f': {'e':1,'h':8},
    'g': {'h':2},
    'h': {'g':2},
}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
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

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            newDistance = 0
            newPath = ['N/A']
            return newDistance, newPath

    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))

    return shortest_distance[goal], path

dijkstra(graph, 'a', 'h')