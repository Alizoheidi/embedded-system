# TODO: develop graph creator function
# TODO: calculate and show result function
from graph_class import Graph
from tasks import add_task_nodes
from ressource_library import add_ressource_library_nodes
from create_graph import graph_creator
from computing import computing_results
from tabels import execution_time_table

if __name__ == "__main__":
    graph = Graph()
    print('execution time table\n',execution_time_table)
    add_task_nodes(graph)
    add_ressource_library_nodes(graph)
    graph_creator(graph)
    # start from task 1
    exe_time = computing_results(graph, 'task_1', 0)
    print('\nall execution time: ',exe_time)
    print('total execution time: ',sum(exe_time))






    

