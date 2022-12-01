PROCESSORS_NAME = ['fpga', 'risc', 'Cisc']

from tabels import cycle_per_instruction_table


def add_resource_library_nodes(graph):
    """
    :param graph: Graph object
    this function will add resource library nodes to the given graph
    and also define functions for them
    each function find CPI depended on connected task
    functions use .loc method from pandas library to get data from dataframe (the CPI table)
    """

    def fpga(task_name):
        return cycle_per_instruction_table.loc[PROCESSORS_NAME[0]][task_name]

    graph.add_vertex(PROCESSORS_NAME[0], fpga)

    def risc(task_name):
        return cycle_per_instruction_table.loc[PROCESSORS_NAME[1]][task_name]

    graph.add_vertex(PROCESSORS_NAME[1], risc)

    def cisc(task_name):
        return cycle_per_instruction_table.loc[PROCESSORS_NAME[2]][task_name]

    graph.add_vertex(PROCESSORS_NAME[2], cisc)
