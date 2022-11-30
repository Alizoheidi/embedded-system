from tabels import execution_time_table


def add_resource_library_nodes(graph):
    """
    :param graph: Graph object
    this function will add resource library nodes to the given graph
    and also define functions for them
    each function find execution time by an operator which depend on connected task
    functions use .loc method from pandas library to get data from dataframe (the execution-time table)
    """
    def fpga(operator):
        return execution_time_table.loc['fpga'][operator]

    graph.add_vertex('fpga', fpga)

    def risc(operator):
        return execution_time_table.loc['risc'][operator]

    graph.add_vertex('risc', risc)

    def cisc(operator):
        return execution_time_table.loc['Cisc'][operator]

    graph.add_vertex('Cisc', cisc)
