def add_edges(graph):
    """
    :param graph: Graph object
    this function will add non_directional edges from task nodes to resource library nodes
    task_1 -- > fpga
          '-- > risc
    task_2 -- > risc
    task_3 -- > Cisc
    and directional edges from task node to other task node
    task_1 -- > task_2
    task_2 -- > task_3
    """
    graph.add_nondirectional_edge('task_1','fpga')
    graph.add_nondirectional_edge('task_1','risc')
    graph.add_nondirectional_edge('task_1','cisc')
    graph.add_nondirectional_edge('task_2','risc')
    graph.add_nondirectional_edge('task_3','cisc')

    graph.add_nondirectional_edge('task_4','fpga')
    graph.add_nondirectional_edge('task_4','risc')
    graph.add_nondirectional_edge('task_4','cisc')
    graph.add_nondirectional_edge('task_5','risc')
    graph.add_nondirectional_edge('task_6','fpga')
    graph.add_nondirectional_edge('task_6','cisc')
    # add directional edges from each task to next one
    # right nodes on page
    graph.add_directional_edge('task_1', 'task_2')
    graph.add_directional_edge('task_2', 'task_3')
    # left nodes on page
    graph.add_directional_edge('task_4', 'task_5')
    graph.add_directional_edge('task_5', 'task_6')

