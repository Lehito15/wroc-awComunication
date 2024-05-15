import pandas as pd


def mean():
    data = pd.read_csv('stopsv3.csv')
    averaged_data = data.groupby('Iteration', as_index=False)['Stops'].mean()
    averaged_data.to_csv('stopsv4.csv', index=False)


def a_vs_dikstra():
    df = pd.read_csv('visted.csv')
    average_difference = df['av'].mean()
    print("Średnia różnica:", average_difference)


a_vs_dikstra()
mean()
