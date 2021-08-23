import json

class Location:
    def __init__(self, target, cost) -> None:
        self.target = target
        self.cost = cost

    def __repr__(self):
        return json.dumps(self.__dict__)
    
    def __lt__(self, other):
        return self.cost < other.cost