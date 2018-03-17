'''
Author: D Yoan L Mekontchou Yomba

Date: 3/3/2018


'''

inf =  float('inf')

def generateGraph(graph, val):
    g = []
    G = []
    for item in range(len(graph)):
        for value in range(len(graph)):
            g.append(val)
        G.append(g)
        g = []
    return G

def floydWarshal(graph):
    # create a d x d matrix
    graph_d = generateGraph(graph, inf)
    graph_c = generateGraph(graph, 0)

    vertices = 0
    for item in graph.keys():
        vertices = vertices + 1
    for i in range(0, vertices):
        for j in range(0, vertices):
            graph_d[i][j] = getEdgeWeight(graph, i, j)
            if graph_d[i][j] is inf:
                graph_d[j][i] = graph_d[j][i]
                graph_d[i][j] = graph_d[j][i]
            else:
                graph_d[j][i] = graph_d[i][j]
                graph_d[i][j] = graph_d[i][j]
            if graph_d[i][j] != inf:
                graph_c[i][j] = i
    for k in range(0, vertices):
        for i in range(0, vertices):
            for j in range(0, vertices):
                if graph_d[i][k] + graph_d[k][j] < graph_d[i][j]:
                    graph_d[i][j] = graph_d[i][k] + graph_d[k][j]
                    graph_c[i][j] = graph_c[k][j]
    print "\n"
    print "====================================="
    print "distance from node (i) to node (j)"
    print "====================================="
    flag = 0;
    for item in range(0, len(graph_d)):
        for value in range(0, len(graph_d)):
            print "%8.0f" % graph_d[item][value],
        print ""
    print "======================================="
    print " node(i) to node(j) predecessor        "
    print "======================================="
    for item in range(0, len(graph_c)):
        for value in range(0, len(graph_c)):
            print "    %8s" % graph_c[item][value],
        print
    print"\n\n"



def getEdgeWeight(graph, edge_i, edge_j):
    if edge_i is edge_j:
        return 0
    for node in graph[edge_i]:
        if(node[0] == edge_j):
            return node[1]
    return inf


def getInput():
    graph = {}
    input_usr = raw_input()
    while input_usr != '':
        set_vals = []
        for value in input_usr.split()[1:]:
            set_vals.append((int(value.split(',')[0]), int(value.split(',')[1])))
        graph[int(input_usr.split()[0])] = set_vals
        input_usr = raw_input()
    return graph

def main():
    graph = getInput()
    floydWarshal(graph)

if __name__ == "__main__":
    main()
