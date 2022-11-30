def add_edges(graph):
    """
    :param graph: Graph object
    this function will add non_directional edges from task nodes to resource library nodes
    task_1 -- > fpga
          '-- > risc
    task_2 -- > risc
    task_3 -- > Cisc
    """
    graph.add_nondirectional_edge('task_1','fpga')
    graph.add_nondirectional_edge('task_1','risc')
    graph.add_nondirectional_edge('task_2','risc')
    graph.add_nondirectional_edge('task_3','Cisc')
