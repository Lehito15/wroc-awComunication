import graph
from queue import PriorityQueue
import time
import heapq


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def print_path(prev, arrival_times, start, end):
    lines = 0
    current_line = None
    shortest_path = []
    current_vertex = end
    while prev[current_vertex] is not None:
        # print(prev[current_vertex])
        shortest_path.append(current_vertex)
        current_vertex = prev[current_vertex]

    shortest_path.append(start)
    shortest_path.reverse()
    l_v, l_departure_time, l_arrival_time, l_line = arrival_times[shortest_path[1]]
    for vertex in shortest_path:

        if vertex != start:

            v, departure_time, arrival_time, line = arrival_times[vertex]
            if v != start:
                v1, departure_time1, arrival_time1, line1 = arrival_times[v]

            if current_line != line:

                if current_line != None:
                    print("Przystanek:", l_v, "- Czas wsiadam:", l_departure_time, " docieram o  ", arrival_time1,
                          " do ", v,
                          " - Linia:", l_line)
                    l_v, l_departure_time, l_arrival_time, l_line = arrival_times[vertex]
                current_line = line
                lines += 1
            if vertex == end:
                print("Przystanek:", l_v, "- Czas wsiadam:", l_departure_time, " docieram o  ", arrival_time, " do ",
                      vertex,
                      " - Linia:", line)
    print('Liczba lini ', lines)
    # return arrival_times[shortest_path[-1]][2]
    return lines


def heuristic(graph, current, end, value):
    h = ((graph.vertices[current].position1 - graph.vertices[end].position1) ** 2 +
         (graph.vertices[current].position2 - graph.vertices[end].position2) ** 2) ** 0.5
    return h * value


def find_best_edge(graph, start, end, time, line, parametr='t'):
    min_edge = None
    min_weight = 1111111110

    for edge in graph.vertices[start].neighbours[end]:
        if time_to_minutes(edge.departure_time) >= time_to_minutes(time):
            cost = time_to_minutes(edge.arrival_time)
            # if line != edge.line:
            #     cost += 1
            if parametr == 'p':
                if line != edge.line:
                    cost += 10
            if parametr == 't' and line != edge.line:
                cost += 1
            if cost < min_weight:
                min_edge = edge
                min_weight = cost

    return min_edge


def time_to_minutes(time):
    dep_hour, dep_min, dep_sec = map(int, time.split(':'))
    return dep_hour * 60 + dep_min


def dikstra(graph, start, end, time):
    distances = {}
    prev = {}
    arrival_times = {}
    visited = set()
    start_time_minutes = time_to_minutes(time)
    for vertex in graph.vertices:
        distances[vertex] = float('inf')
        prev[vertex] = None
        arrival_times[vertex] = (None, None, None, None)
    distances[start] = 0
    priority_queue = [(0, start, time)]
    visited.add(start)
    current_line = None
    while priority_queue:
        current_distance, current_vertex, time_at_stop = heapq.heappop(priority_queue)
        if current_vertex == end:
            break
        for neighbor, edges in graph.vertices[current_vertex].neighbours.items():
            edge = find_best_edge(graph, current_vertex, neighbor, time_at_stop, current_line)
            if edge is not None:
                distance = time_to_minutes(edge.arrival_time) - start_time_minutes
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    prev[neighbor] = current_vertex
                    arrival_times[neighbor] = (
                        current_vertex, edge.departure_time, edge.arrival_time, edge.line)
                    current_line = edge.line
                    heapq.heappush(priority_queue, (distance, neighbor, edge.arrival_time))

    if end not in prev or prev[end] is None:
        print("Nie znaleziono trasy do końcowego przystanku:", end)
        return None
    return print_path(prev, arrival_times, start, end)
    # return


def astar(graph, start, end, time, parametr):
    start_time_minutes = time_to_minutes(time)
    open1 = [(0, start, time, None)]
    prev = {start: None}
    arrival_times = {}
    distances = {start: 0}
    current_line = None
    visited = set()
    while open1:
        # print(open.get())
        current_cost, current_vertex, current_time, current_line = heapq.heappop(open1)

        if current_vertex == end:
            break
        visited.add(current_vertex)

        for neighbor in graph.vertices[current_vertex].neighbours:
            if neighbor not in visited:
                best_edge = find_best_edge(graph, current_vertex, neighbor, current_time, current_line, parametr)
                if best_edge is not None:
                    distance = time_to_minutes(best_edge.arrival_time) - start_time_minutes
                    if neighbor not in distances or distance < distances[neighbor]:
                        distances[neighbor] = distance

                        prev[neighbor] = current_vertex

                        arrival_times[neighbor] = (
                            current_vertex, best_edge.departure_time, best_edge.arrival_time, best_edge.line)

                        priority = distance + heuristic(graph, current_vertex, end, 2100)
                        if parametr == 'p':
                            if current_line != best_edge.line:
                                priority = current_cost + best_edge.weight + 10
                                # priority = distance + best_edge.weight + value
                            else:
                                priority = current_cost + best_edge.weight
                                # priority = distance + best_edge.weight
                        heapq.heappush(open1, (priority, neighbor, best_edge.arrival_time, best_edge.line))
    if end not in prev or prev[end] is None:
        print("Nie znaleziono trasy do końcowego przystanku:", end)
        return None
    return print_path(prev, arrival_times, start, end)


if __name__ == "__main__":
    g = graph.Graph()
    g.make_graph('unique_edges.csv')
    # print(heuristic(g, 'Tramwajowa', 'PL. GRUNWALDZKI'))
    # print(heuristic(g, 'BISKUPIN', 'PL. GRUNWALDZKI'))
    # print(g.vertices['Tramwajowa'].neighbours['ZOO'][0])
    # frontier = PriorityQueue()
    # frontier.put((2, 'elo'))
    # frontier.put((1, 'elo1', '56'))
    # print(frontier.get())
    # print(frontier.get())
    # find_best_edge(g, 'Babimojska', 'Park Biznesu', '16:58:00', None , 't')
    # test(g)
    # print(time_to_minutes('17:30:00'))
    # find_best_edge(g, 'Tramwajowa', 'ZOO', '17:03:00', 10)
    # start = input("Podaj start")
    # end = input("Podaj koniec")
    # time = str(input("Podaj czas w formaci hh:mm:ss"))
    result_astar, time_astar = measure_time(astar, g,'Brzezia Łąka - Główna', 'Arkady (Capitol)', '11:15:00' , 't')
    print("Czas wykonania algorytmu A*: ", time_astar)
    #
    result_astar, time_astar = measure_time(astar, g, 'Brzezia Łąka - Główna', 'Arkady (Capitol)', '11:15:00', 'p')
    print("Czas wykonania algorytmu A*  z p: ", time_astar)
    # #
    # # #
    # # Pomiar czasu dla funkcji dijkstra
    result_dijkstra, time_dijkstra = measure_time(dikstra, g, 'Brzezia Łąka - Główna', 'Arkady (Capitol)', '11:15:00')
    print("Czas wykonania algorytmu Dijkstry: ", time_dijkstra)
    # print(dikstra(g, 'Bukowina', 'Widna', '22:33:00'))

# 'Gajowicka', 'Wallenroda', '14:38:00'
# 'Brzezia Łąka - Główna', 'Arkady (Capitol)', '11:15:00
