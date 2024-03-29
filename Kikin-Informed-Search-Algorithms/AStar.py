"""
From Map to Graph
Universidad Panamericana Campus Mixcoac
Inteligencia Artificial
Enrique Ulises Báez Gómez Tagle
Iván Cruz Ledesma
Mauricio Pérez Aguirre
April 26 2023
v 1.0
R: Iván Cruz Ledesma
"""
import time

from queue import PriorityQueue


def AStarSearch(graph, heuristics, origin, destination):
    # initialize the priority queue with the origin node
    # and its priority based on the heuristic function
    start_time = time.time()
    frontier = PriorityQueue()
    frontier.put(origin, heuristics.get_weight(origin, destination))

    # initialize the dictionaries to keep track of the parent nodes
    # and the total cost of each visited node
    came_from = {}
    cost_so_far = {origin: 0}

    while not frontier.empty():
        # select the node with the lowest priority from the priority queue
        current = frontier.get()

        # if the destination node has been reached, break the loop
        if current == destination:
            break

        # expand the current node by visiting its neighboring nodes
        for next_node in graph.get_neighbors(current):
            # calculate the cost of reaching the next node from the current node
            new_cost = cost_so_far[current] + \
                int(graph.get_weight(current, next_node))

            # if the next node has not been visited or the new cost is lower than the previous cost,
            # update the cost of the next node and its priority in the priority queue
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + \
                    float(heuristics.get_weight(next_node, destination))
                frontier.put(next_node, priority)

                # keep track of the parent node to reconstruct the path later
                came_from[next_node] = current

    # reconstruct the shortest path from the destination node to the origin node
    path = [destination]
    while path[-1] != origin:
        path.append(came_from[path[-1]])
    path.reverse()

    # print the cost of the path and return the path as a list of nodes
    print(f"Cost: {cost_so_far[destination]}")
    end_time = time.time()
    print("Exec time: ", end_time - start_time, "segundos")

    return path
