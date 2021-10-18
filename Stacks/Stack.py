class Stack(object):
    def __init__(self, inarr=None):
        self.data = []
        if inarr:
            for _ in inarr:
                self.push(_)
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        try:
            return self.data.pop(-1)
        except:
            return None

    def __str__(self):
        return str(self.data)

    def peek(self):
        return self.data[-1]

