def graph_creator(graph):
    graph.add_nondirectional_edge('task_1','fpga',1)
    graph.add_nondirectional_edge('task_1','risc',1)
    graph.add_nondirectional_edge('task_2','risc',1)
    graph.add_nondirectional_edge('task_3','HWM',1)
