from ressource_library import PROCESSORS_NAME
from tasks import TASKS_NAME


def add_edges(graph):
    """
    :param graph: Graph object
    this function will add non_directional edges from task nodes to resource library nodes
    task_1 -- > fpga
          '-- > risc
          '-- > Cisc
    task_2 -- > risc
    task_3 -- > Cisc
    task_4 -- > fpga
          '-- > risc
          '-- > Cisc
    task_5 -- > risc
    task_6 -- > fpga
    task_6 -- > Cisc
    and directional edges from task node to other task node
    task_1 -- > task_2
    task_2 -- > task_3
    task_3 -- > task_4
    task_4 -- > task_5
    """
    graph.add_nondirectional_edge(TASKS_NAME[0], PROCESSORS_NAME[0])
    graph.add_nondirectional_edge(TASKS_NAME[0], PROCESSORS_NAME[1])
    graph.add_nondirectional_edge(TASKS_NAME[0], PROCESSORS_NAME[2])
    graph.add_nondirectional_edge(TASKS_NAME[1], PROCESSORS_NAME[1])
    graph.add_nondirectional_edge(TASKS_NAME[2], PROCESSORS_NAME[2])

    graph.add_nondirectional_edge(TASKS_NAME[3], PROCESSORS_NAME[0])
    graph.add_nondirectional_edge(TASKS_NAME[3], PROCESSORS_NAME[1])
    graph.add_nondirectional_edge(TASKS_NAME[3], PROCESSORS_NAME[2])
    graph.add_nondirectional_edge(TASKS_NAME[4], PROCESSORS_NAME[1])
    graph.add_nondirectional_edge(TASKS_NAME[5], PROCESSORS_NAME[0])
    graph.add_nondirectional_edge(TASKS_NAME[5], PROCESSORS_NAME[2])
    # add directional edges from each task to next one
    # right nodes on page
    graph.add_directional_edge(TASKS_NAME[0], TASKS_NAME[1])
    graph.add_directional_edge(TASKS_NAME[1], TASKS_NAME[2])
    # left nodes on page
    graph.add_directional_edge(TASKS_NAME[3], TASKS_NAME[4])
    graph.add_directional_edge(TASKS_NAME[4], TASKS_NAME[5])

