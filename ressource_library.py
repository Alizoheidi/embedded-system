from tabels import PROCESSORS_NAME, ressource_library_table


def add_resource_library_nodes(graph):
    """
    :param graph: Graph object
    this function will add resource library nodes to the given graph
    and also define functions for them
    each function find CPI depended on connected task
    functions use .loc method from pandas library to get data from dataframe (the CPI table)
    """

    def fpga():
        return ressource_library_table.loc[PROCESSORS_NAME[0]]['clock rate'],\
               ressource_library_table.loc[PROCESSORS_NAME[0]]['frequency rate'],\
               ressource_library_table.loc[PROCESSORS_NAME[0]]['consume power']

    graph.add_vertex(PROCESSORS_NAME[0], fpga)

    def risc():
        return ressource_library_table.loc[PROCESSORS_NAME[1]]['clock rate'],\
               ressource_library_table.loc[PROCESSORS_NAME[1]]['frequency rate'],\
               ressource_library_table.loc[PROCESSORS_NAME[1]]['consume power']
    graph.add_vertex(PROCESSORS_NAME[1], risc)

    def cisc():
        return ressource_library_table.loc[PROCESSORS_NAME[2]]['clock rate'],\
               ressource_library_table.loc[PROCESSORS_NAME[2]]['frequency rate'],\
               ressource_library_table.loc[PROCESSORS_NAME[2]]['consume power']
    graph.add_vertex(PROCESSORS_NAME[2], cisc)
