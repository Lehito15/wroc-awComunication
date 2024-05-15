import matplotlib.pyplot as plt
import pandas as pd

def plot():
    data = pd.read_csv('stopsv4.csv')

    # Wyodrębnij kolumny "Iteration" i "Execution Time"
    iterations = data['Iteration']
    execution_times = data['Stops']

    # Narysuj wykres
    plt.plot(iterations, execution_times, marker='.', linestyle='', color='black')
    plt.xlabel('Parametr')
    plt.ylabel('Przesiadki')
    plt.title('O  ile mniej przesiadek z róznymi parametrami')
    plt.grid(True)
    plt.show()


def plot1():
    df = pd.read_csv('visted.csv')

    # Stworzenie wykresu
    plt.figure(figsize=(10, 6))

    # Dodanie danych do wykresu
    plt.plot(df['index'], df['a'], label='Bez_viseted', marker='o')
    plt.plot(df['index'], df['av'], label='viseted', marker='o')
    # plt.plot(df['index'], df['d'], label='Dijkstra', marker='o')


    # Dodanie tytułu i etykiet osi
    plt.title('Porównanie szybkoście')
    plt.xlabel('Iteracja')
    plt.ylabel('czas ')

    # Dodanie legendy
    plt.legend()

    # Wyświetlenie wykresu
    plt.grid(True)
    plt.show()

plot()