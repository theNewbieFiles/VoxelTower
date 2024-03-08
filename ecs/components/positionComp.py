
class Position: 
    #constructor
    def __init__(self, storage) -> None:
        self.storage = storage['position'] = {}; 
        
    def add(self, id, X=0, Y=0, Z=0):
        self.storage[id] = [X, Y, Z]
        
    def delete(self, id):
        if id in self.storage:
            del self.storage[id]
        else: 
            print(f"Position with id {id} not found")
        
    def printList(self):
        for id, pos in self.storage.items():
            print(f'ID: {id}, Postion: {pos}')
        
