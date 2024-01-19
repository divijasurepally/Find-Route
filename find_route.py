#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys

class PQClass():
    def __init__(self):
        self.list = []

    def isempty(self):
        return len(self.list) == 0

    def add_node(self, data):
        self.list.append(data)

    def fetch_closest(self):
        min = 0
        for i in range(len(self.list)):
            if self.list[i] < self.list[min]:
                min = i
        item = self.list[min]
        del self.list[min]
        return item


def get_text_file_data(fname, heuristic=False):

    f1 = open(fname, 'r')
    file_text = f1.readlines()
    f1.close()
    
    if not heuristic:
        Graph = dict()
        for temp_line in file_text[:-1]:
            line = temp_line.split()
            if 'END OF INPUT' in line:
                return Graph
            
            if line[0] in Graph:
                Graph[line[0]][line[1]] = float(line[2])
            else:
                Graph[line[0]] = {line[1]: float(line[2])}

            if line[1] in Graph:
                Graph[line[1]][line[0]] = float(line[2])
            else:
                Graph[line[1]] = {line[0]: float(line[2])}
        return Graph

    else:
        heuristic_values = dict()
        for temp_line in file_text[:-1]:
            line = temp_line.split()
            if 'END OF INPUT' in line:
                return heuristic_values
            
            heuristic_values[line[0]] = float(line[1])

        return heuristic_values


def is_destination_reached(current_city, city):
    return current_city == city


def searching_path_normal(Graph, origin, dest): # Implements a G based uniform cost search

    queue = PQClass()
    queue.add_node((0, origin))
    visited_cities= {origin:("", 0)}

    generated_count = 0
    popped = 0
    city_proc = []
    

    while not queue.isempty():
        item = queue.fetch_closest()
        city_name, city_pos = item
        popped += 1
        
        if is_destination_reached(city_pos, dest):
            break

        if city_pos in city_proc:
            continue
        else:
            city_proc.append(city_pos)

        for i in Graph[city_pos]:
            generated_count += 1
            queue.add_node((Graph[city_pos][i]+visited_cities[city_pos][1], i))
            if i not in visited_cities:
                visited_cities[i] = (city_pos, Graph[city_pos][i]+visited_cities[city_pos][1])

    travel_route = []
    distance = 0
    if dest in visited_cities:
        distance = 0
        city_pos = dest
        while city_pos != origin:
            distance += Graph[visited_cities[city_pos][0]][city_pos]
            travel_route.append(city_pos)
            city_pos = visited_cities[city_pos][0]

    return travel_route, len(city_proc), generated_count+1, distance, popped


def heuristic_search(Graph, origin, dest, val):
    queue = PQClass()
    queue.add_node((0, origin))
    visited_cities= {origin:("", 0)}

    generated_count = 0
    popped = 0
    city_proc = []
    
    while not queue.isempty():
        item = queue.fetch_closest()
        city_name, city_pos = item
        popped += 1

        if is_destination_reached(city_pos, dest):
            break

        if city_pos in city_proc:
            continue
        else:
            city_proc.append(city_pos)

        for i in Graph[city_pos]:
            generated_count += 1
            if i not in visited_cities:
                visited_cities[i] = (city_pos, Graph[city_pos][i] + visited_cities[city_pos][1])
            queue.add_node((Graph[city_pos][i] + visited_cities[city_pos][1] + val[i], i))

    travel_route = []
    distance = 0
    if dest in visited_cities:
        distance = 0
        city_pos = dest
        while city_pos != origin:
            distance += Graph[visited_cities[city_pos][0]][city_pos]
            travel_route.append(city_pos)
            city_pos = visited_cities[city_pos][0]
  
    return travel_route, len(city_proc), generated_count+1, distance, popped


if len(sys.argv) == 4:
    file_name = sys.argv[1]
    starting = sys.argv[2]
    ending_goal = sys.argv[3]

    Graph = get_text_file_data(file_name)

    op = searching_path_normal(Graph, starting, ending_goal)
    travel_route, expanded, generated_count, distance, popped = op

    print("\nNodes popped: "+ str(popped))
    print("Nodes expanded: "+ str(expanded))
    print("Nodes generated: "+ str(generated_count))
    
    if distance > 0:
        print("Distance: "+ str(float(distance)) +"km")
    else:
        print("Distance: infinity")

    print("Route:")
    city_position = starting
    if len(travel_route) == 0:
        print("None")
    else:
        for route in travel_route[::-1]:
            print(str(city_position)+"to"+str(route)+str(Graph[city_position][route])+"km")
            city_position = route

elif len(sys.argv) == 5: #Heuristic Mode
    fname = sys.argv[1]
    starting = sys.argv[2]
    ending_goal = sys.argv[3]
    fname_heuristic = sys.argv[4]
    Graph = get_text_file_data(fname)
    heuristic_value = get_text_file_data(fname_heuristic, heuristic=True)

    op = heuristic_search(Graph, starting, ending_goal, heuristic_value)
    travel_route, expanded, generated_count, distance, popped = op

    print("\nNodes popped: "+ str(popped))
    print("Nodes expanded: "+ str(expanded))
    print("Nodes generated: "+ str(generated_count))

    if distance > 0:
        print("Distance: "+str(float(distance))+"km")
    else:
        print("Distance: infinity")

    print("Route:")
    city_position = starting
    if len(travel_route) == 0:
        print("None")
    else:
        for route in travel_route[::-1]:
            print(str(city_position)+"to"+str(route)+str(Graph[city_position][route])+"km")
            city_position = route


# In[ ]:




