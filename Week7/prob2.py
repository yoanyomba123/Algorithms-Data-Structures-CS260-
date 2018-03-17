# Author: D Yoan L Mekontchou Yomba


class stack():
    def __init__(self):
        self.stacklist = [];

    def push(self, value):
        self.stacklist.append(value);

    def pop(self):
        value = self.stacklist.pop()
        return value

class queue():
    def __init__(self):
        self.queuelist = []

    def enqueue(self, item):
        self.queuelist.insert(0, item)

    def dequeue(self):
        return self.queuelist.pop()

def dfs(G, root, value):
    seen  = []
    stackobject = stack()
    stackobject.push(root)
    while stackobject:
        current_val = stackobject.pop()
        if current_val == value:
            return seen
        if current_val not in seen:
            seen.append(current_val)
            for item in G[current_val]:
                stackobject.push(item)
    return False

def bfs(G, root, value):
    seen = []
    q = queue()
    q.enqueue(root)
    while q:
        current_val = q.dequeue()
        if current_val == value:
            return seen
        if current_val not in seen:
            seen.append(current_val)
            for item in G[current_val]:
                q.enqueue(item)
    return False

if __name__ == "__main__":
    graph = {
        1: [3, 6],
        2: [1, 3],
        3: [2],
        4: [3],
        5: [2, 7],
        6: [5],
        7: [8],
        8: [5],
        9: [1,2,8]
    }
    print '\n Graph Adjacency list'
    print '================================'
    for key in graph.keys():
        print str(key) + " -> " + str(graph[key])

    print '\nSpanning Trees'
    print '================================='
    print 'Depth First Search (DFS) starting at 4-> ', dfs(graph, 4, 5)
    print 'Breadth First Search (BFS) starting at 4--> ', bfs(graph, 4, 5)
    print '\n'

