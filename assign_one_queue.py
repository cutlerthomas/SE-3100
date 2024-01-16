


class Queue:

    def __init__(self):
        self.queue = []
    
    def get_front(self):
        return self.queue.pop(0)
    
    def get_back(self):
        return self.queue.pop(len(self.queue) - 1)
    
    def insert_back(self, item):
        self.queue.append(item)

    def insert_front(self, item):
        self.queue.insert(0, item)