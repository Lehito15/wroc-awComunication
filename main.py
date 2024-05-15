from queue import PriorityQueue

# Tworzenie kolejki priorytetowej
frontier = PriorityQueue()

# Dodawanie elementów z priorytetami
frontier.put((2, 'elo'))
frontier.put((1, 'elo1'))

# Pobieranie elementu o najniższym priorytecie
print(frontier.get())