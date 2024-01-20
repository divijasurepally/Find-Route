# Find-Route
 
Project Purpose: To calculate the shortest route from a starting city to a destination city.
Key Features: Supports both standard pathfinding and heuristic-based searches.
Key Components
Priority Queue (PQClass):

A custom class used for managing the nodes (cities) during the search process.
Functions include adding nodes and fetching the closest node based on the path cost.
Graph Construction (get_text_file_data):

Reads data from a text file to construct a graph.
The graph is represented as a dictionary where each city and its connected cities are mapped with their respective distances.
Supports loading heuristic values for heuristic-based searches.
Pathfinding Algorithms:

searching_path_normal: Implements a Uniform Cost Search (UCS), a type of graph traversal that explores nodes in order of their path cost from the start node.
heuristic_search: Extends the UCS by adding heuristic values (estimated cost from the current city to the destination) for each city, likely implementing an A* search algorithm.
Algorithm Execution:

The script takes command-line arguments to specify the input file, start city, destination city, and (optionally) a heuristic file.
Based on the provided arguments, it executes either the standard pathfinding or the heuristic-based search.
Detailed Functionality
Initialization: The graph is initialized from the input file. In heuristic mode, heuristic values are also loaded.
Search Process:
The search begins from the start city.
Cities are explored based on their path cost (and heuristic cost in heuristic mode).
The search continues until the destination is reached or all possible paths are explored.
Output:
The script prints the total distance of the found route, the number of nodes expanded, generated, and popped during the search.
It also prints the actual route taken from the start city to the destination.
Practical Application
This script can be used in scenarios like route planning for logistics, navigation systems, or even in games where pathfinding is essential.
