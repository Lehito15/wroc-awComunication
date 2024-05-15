from algoritms import astar

from algoritms import dikstra
from algoritms import time_to_minutes
import random
from graph import Graph
import time


def random_time():
    hour = random.randint(0, 23)
    minut = random.randint(0, 59)
    sec = 00
    return f"{hour:02d}:{minut:02d}:{sec:02d}"


def optimalization_time():
    graph = Graph()
    stops = list(graph.make_graph('unique_edges.csv'))

    with open('a_vs_d.csv', 'w') as file:
        # file.write("Iteration,Execution Time\n")
        for i in range(50):
            start = random.choice(stops)
            end = random.choice(stops)
            time_str = random_time()
            print(start)
            print(end)
            print(time_str)
            print(i)

            # for j in range(0, 10000, 10):
            # print(j)
            start_time = time.time()
            astar(graph, start, end, time_str, 't', 1)
            end_time = time.time()
            execution_time = end_time - start_time
            file.write(f"{i},{execution_time}\n")


def optimalization_quality():
    graph = Graph()
    stops = list(graph.make_graph('unique_edges.csv'))

    with open('optimalization_quality_results.csv', 'w') as file:
        file.write("Iteration,Execution Time\n")
        for i in range(50):
            start, end = random.sample(stops, 2)
            time_str = random_time()
            best = dikstra(graph, start, end, time_str)
            # print(best)
            print(i)
            if best is None:
                continue

            best_minutes = time_to_minutes(best)

            for j in range(0, 10000, 10):
                # print(j)

                end_time = astar(graph, start, end, time_str, 't', j)
                minutes = time_to_minutes(end_time)
                diffrence = minutes - best_minutes

                file.write(f"{j},{diffrence}\n")


def a_vs_d():
    graph = Graph()
    stops = list(graph.make_graph('unique_edges.csv'))

    with open('a_vs_d.csv', 'w') as file:
        # file.write("Iteration,Execution Time\n")
        for i in range(50):
            start = random.choice(stops)
            end = random.choice(stops)
            time_str = random_time()
            print(start)
            print(end)
            print(time_str)
            print(i)

            # for j in range(0, 10000, 10):
            # print(j)
            start_time = time.time()
            dikstra(graph, start, end, time_str)
            end_time = time.time()
            d_time = end_time - start_time

            start_time = time.time()
            astar(graph, start, end, time_str, 't', 1)
            end_time = time.time()
            a_time = end_time - start_time
            diffrence = d_time - a_time
            file.write(f"{i},{d_time},{a_time},{diffrence}\n")


def aStops_vs_d():
    graph = Graph()
    stops = list(graph.make_graph('unique_edges.csv'))

    with open('astops_vs_d.csv', 'w') as file:
        # file.write("Iteration,Execution Time\n")
        for i in range(50):
            start = random.choice(stops)
            end = random.choice(stops)
            time_str = random_time()
            print(start)
            print(end)
            print(time_str)
            print(i)

            # for j in range(0, 10000, 10):
            # print(j)

            d_stops = dikstra(graph, start, end, time_str)

            a_stops = astar(graph, start, end, time_str, 'p', 10)
            if a_stops is None or d_stops is None:
                continue
            diffrence = d_stops - a_stops

            file.write(f"{i},{d_stops},{a_stops},{diffrence}\n")


def a_value():
    graph = Graph()
    stops = list(graph.make_graph('unique_edges.csv'))

    with open('visted.csv', 'w') as file:
        # file.write("Iteration,Execution Time\n")
        for i in range(50):
            start = random.choice(stops)
            end = random.choice(stops)
            time_str = random_time()
            print(start)
            print(end)
            print(time_str)
            print(i)

            # for j in range(0, 10000, 10):
            # print(j)
            start_time = time.time()
            # d_time = dikstra(graph, start, end, time_str)
            end_time = time.time()
            # d_time = end_time - start_time

            start_time = time.time()
            astar(graph, start, end, time_str, 't', 2100)
            end_time = time.time()
            a1_time = end_time - start_time

            start_time = time.time()

            end_time = time.time()
            a_time = end_time - start_time
            if a1_time != None:
                # a1_minutes = time_to_minutes(a1_time)
                # a_minutes = time_to_minutes(a_time)
                # d_minutes = time_to_minutes(d_time)
                # diffrence = a1_minutes - a_minutes
                # diffrencea = a1_minutes - d_minutes
                diff = a_time - a1_time
                file.write(f"{i},{a1_time},{a_time},{diff}\n")


def optimalization_stops():
    graph = Graph()
    stops = list(graph.make_graph('unique_edges.csv'))

    with open('stopsv3.csv', 'w') as file:
        file.write("Iteration,Stops\n")
        for i in range(50):
            start, end = random.sample(stops, 2)
            time_str = random_time()
            dikstra_stops = dikstra(graph, start, end, time_str)
            # print(best)
            print(i)
            if dikstra_stops is None:
                continue

            for j in range(0, 1000, 10):
                print(j, ' ' , i)

                astar_stops = astar(graph, start, end, time_str, 'p', j)
                if astar_stops != None:
                    diffrence = dikstra_stops - astar_stops

                    file.write(f"{j},{diffrence}\n")


# print(random_time())
if __name__ == "__main__":
    optimalization_stops()
