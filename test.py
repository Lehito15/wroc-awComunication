import pandas as pd
import time
import heapq


# Przykładowe dane z pliku CSV
# czas = '24:01:00'
#
# # Podziel czas na godziny, minuty i sekundy
# godziny, minuty, sekundy = map(int, czas.split(':'))
#
# # Oblicz liczbę sekund
# czas_w_sekundach = godziny * 3600 + minuty * 60 + sekundy
#
# print(czas_w_sekundach)


def check_time(file):
    start_time = time.time()
    df = pd.read_csv('connection_graph.csv')
    for row in df.itertuples():
        pass
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


# Pomiar czasu wykonania funkcji
# time_taken = check_time('connection_graph.csv')
# print("Czas wykonania funkcji: {:.2f} sekund".format(time_taken))
def mixed_type():
    df = pd.read_csv('connection_graph.csv', dtype={'line': str})
    edge = set()
    # Wyświetlenie wierszy zawierających błędy mieszanych typów danych w drugiej kolumnie
    for row in df.itertuples():
       edge.add(row.line)
    print(edge)


# mixed_type()


def delete_repeats(file):
    df = pd.read_csv('connection_graph.csv', dtype={'line': str})
    edges = set()
    for row in df.itertuples():
        edge = (
        row.company, row.line, row.departure_time, row.arrival_time, row.start_stop, row.end_stop, row.start_stop_lat,
        row.start_stop_lon,
        row.end_stop_lat, row.end_stop_lon)
        edges.add(edge)

    unique_edges_df = pd.DataFrame(edges, columns=['company', 'line', 'departure_time', 'arrival_time', 'start_stop',
                                                   'end_stop', 'start_stop_lat', 'start_stop_lon', 'end_stop_lat',
                                                   'end_stop_lon'])
    unique_edges_df.to_csv('unique_edges.csv', index=True)

# delete_repeats('connection_graph.csv')
def uniqu_names(file):
    df = pd.read_csv('connection_graph.csv', dtype={'line': str})
    names = set()
    for row in df.itertuples():
        names.add(row.start_stop)
    print(len(names))
uniqu_names('connection_graph.csv')
d = {2: ['e'],
     3:["3"]}
d[2].append('r')

d[4] = ['2']
pq = [(0, 6)]
print(pq)


