def add_task_nodes(graph):
    # first Task
    def task_1(x):
        return 4 + 3 - 1, ('+','-')

    graph.add_vertex('task_1', task_1)

    # second Task
    def task_2(x):
        return x * 10 + 9, ('+', '*')

    graph.add_vertex('task_2', task_2)

    # third Task
    def task_3(x):
        return x / 5 - 2, ('/', '-')

    graph.add_vertex('task_3', task_3)

    # add edges
    graph.add_directional_edge('task_1', 'task_2')
    graph.add_directional_edge('task_2', 'task_3')


