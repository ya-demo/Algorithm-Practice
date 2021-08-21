import json

class Node:
    def __init__(self, row, col, cost = None) -> None:
        self.row = row
        self.col = col
        self.cost = cost

    def __repr__(self):
        return json.dumps(self.__dict__)
    
    def __lt__(self, other):
        return self.cost < other.cost