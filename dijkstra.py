#實作Dijkstra 主要要有三部分


#1.建立紀錄圖形的Hash table 
#裡面包括節點連接的各個節點(Node)，以及邊(edge)的長度

graph = {}
graph["Start"] = {}
graph["Start"]["a"] = 6
graph["Start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] =5

graph["fin"] = {}
print(graph)

#2.建立每個節點"成本" 的Hash table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#3.建立父節點的Hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs :
        cost = costs[node]
        if cost < lowest_cost and node not in processed :
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None :
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys() :
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)

    #把更新後cost table傳到函數，找出下一個最小個cost
    node = find_lowest_cost_node(costs)


# print("Cost from the start to each node:")

print("The Shortest Path is ")

def theshortespath (node):
    if node =="start" :
        print("start")
        print("---next node---")
        return 
    prev = parents[node]
    theshortespath(prev)
    print(node)
    print("---next node---")
    

theshortespath("fin")



