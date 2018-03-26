def bfs(start :int, Adj :dict):
    level  = {start: None} # {node: distance to starting node (# edges)}
    parent = {start: None} # the parent hash is optional but helps
                           # backtrack for shortest paths

    previous = [start] # what nodes in previous
                       # level (resets with each while iteration)
    i = 1
    while previous:
        next = []
        for node in previous:
            for neighbours in Adj[node]: # for children of previous nodes
                if neighbours not in level: # if it hasn't already been traversed

                    level[neighbours] = i
                    parent[neighbours] = node
                    next.append(neighbours)

        previous = next
        i += 1
# the graph is represented in Fig 2
bfs(start = 1, Adj = {1:{2,3},2:{5,4,1},3:{1,6},4:{2},5:{2},6:{3,7},7:{6}})
