import pandas
from tabels import clock_rate
from ressource_library import PROCESSORS_NAME


performance_table = pandas.DataFrame(data=[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']],
                                     index=PROCESSORS_NAME,
                                     columns=['task_1', 'task_2', 'task_3'])


def computing_results(graph, task_vertex):
    """
    :param graph: Graph object
    :param task_vertex: a task node which should be done
    """

    for processor in graph.give_nondirected_edges(task_vertex):
        # cycle per instruction
        cpi = graph.vertices_functions[processor](task_vertex)
        # performance = clock rate/CPI
        performance = round(clock_rate[processor] / cpi,1)
        # add data to the table
        performance_table.loc[processor][task_vertex] = performance
        # going to next task
    for task in graph.give_directed_edges(task_vertex):
        computing_results(graph, task)
