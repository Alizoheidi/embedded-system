from graph_class import Graph
from tabels import PROCESSORS_NAME, ressource_library_table
from tasks import add_task_nodes
from ressource_library import add_resource_library_nodes
from create_edges import add_edges
from computing import computing_results, performance_table, execution_time_table, energy_consumption_table

if __name__ == "__main__":
    # create graph object from Graph class
    graph = Graph()
    # create task nodes
    add_task_nodes(graph)
    # create resource library nodes
    add_resource_library_nodes(graph)
    # create edges for graph
    add_edges(graph)
    # start doing all tasks and compute execution time
    # task_1 and task_4 are initial nodes
    computing_results(graph, 'task_1')
    computing_results(graph, 'task_4')
    # show results
    performance_table.index = ["FPGA(XC 2064)",
                               "RISC(IBM 801)",
                               "Cisc(INTEL X88)"]
    print('\nall performances:\n', performance_table)
    print('\nall execution times:\n', execution_time_table)
    print('\nenergy consumption:\n', energy_consumption_table)
    # Json files
    ressource_library_json = ressource_library_table.to_json(orient='index')
    print(ressource_library_json)
