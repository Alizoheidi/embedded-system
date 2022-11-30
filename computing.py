def computing_results(graph, task_vertex, pre_result):
    """
    :param graph: Graph object
    :param task_vertex: a task node which should be done
    :param pre_result: result of previous task
    :return: list of all execution times that each processor
    """
    execution_times = []
    for processor in graph.give_nondirected_edges(task_vertex):
        task_result, operations = graph.vertices_functions[task_vertex](pre_result)
        for operation in operations:
            execution_times.append(graph.vertices_functions[processor](operation))
    for task in graph.give_directed_edges(task_vertex):
        next_execution_times = computing_results(graph, task, task_result)
        execution_times += next_execution_times

    return execution_times

