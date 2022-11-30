from graph_class import Graph
from tasks import add_task_nodes
from ressource_library import add_resource_library_nodes
from create_edges import add_edges
from computing import computing_results

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
    exe_time = computing_results(graph, 'task_1', 0)
    # show results
    print('\nall execution time: ',exe_time)
    

