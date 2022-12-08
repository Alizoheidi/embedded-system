def add_task_nodes(graph):
    """
    :param graph: Graph object
    this function will add task nodes to the given graph
    """

    # first Task
    def task_1():
        return '+'

    graph.add_vertex('task_1', task_1())

    # second Task
    def task_2():
        return '-'

    graph.add_vertex('task_2', task_2())

    # third Task
    def task_3():
        return '*'

    graph.add_vertex('task_3', task_3())

    # forth Task
    def task_4():
        return '*'

    graph.add_vertex('task_4', task_4())

    # fifth Task
    def task_5():
        return '+'

    graph.add_vertex('task_5', task_5())

    # sixth Task
    def task_6():
        return '/'

    graph.add_vertex('task_6', task_6())
