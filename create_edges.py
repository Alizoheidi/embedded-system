import random
from resource_library import PROCESSORS_NAME
from tasks import TASKS_NAME


def add_edges(graph):
    """
    :param graph: Graph object
    this function will add non_directional edges from task nodes to resource library nodes
    and directional edges from task node to other task node
    task_1 -- > task_2
    task_2 -- > task_3
    task_3 -- > task_4
    task_4 -- > task_5
    """
    # number of connected processors
    for task_name in TASKS_NAME:
        weigh_list = [10] * len(PROCESSORS_NAME)
        n_connected = random.randint(1, len(PROCESSORS_NAME))
        p_name_temp = list(PROCESSORS_NAME)
        for i in range(n_connected):
            p_chosen = random.choices(p_name_temp,weigh_list,k=1)
            graph.add_nondirectional_edge(task_name, p_chosen[0])
            weigh_list[PROCESSORS_NAME.index(p_chosen[0])] -= 1
        print(weigh_list)

    # add directional edges from each task to next one
    # right nodes on page
    graph.add_directional_edge(TASKS_NAME[0], TASKS_NAME[1])
    graph.add_directional_edge(TASKS_NAME[1], TASKS_NAME[2])
    # left nodes on page
    graph.add_directional_edge(TASKS_NAME[3], TASKS_NAME[4])
    graph.add_directional_edge(TASKS_NAME[4], TASKS_NAME[5])
    print(graph.adjacency_matrix)
