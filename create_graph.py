def graph_creator(graph):
    graph.add_nondirectional_edge('task_1','fpga')
    graph.add_nondirectional_edge('task_1','risc')
    graph.add_nondirectional_edge('task_2','risc')
    graph.add_nondirectional_edge('task_3','HWM')
