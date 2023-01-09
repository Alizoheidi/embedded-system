from charts import energy_consumption_pie_chart, time_bar_graph
from graph_class import Graph
from tasks import add_task_nodes
from ressource_library import add_resource_library_nodes
from create_edges import add_edges
from computing import computing_results, performance_table, execution_time_table, energy_consumption_table
from create_lp_results import asp_resource_library, asp_taskList,asp_mapping_option

if __name__ == "__main__":
    # create graph object from Graph class
    graph = Graph()
    # create task nodes
    initial_nodes = add_task_nodes(graph)
    # create resource library nodes
    add_resource_library_nodes(graph)
    # create edges for graph
    add_edges(graph)
    # start doing all tasks from initial nodes
    for node_name in initial_nodes:
        computing_results(graph, node_name)
    # show results
    print('\nall performances:\n', performance_table)
    print('\nall execution times:\n', execution_time_table)
    print('\nenergy consumption:\n', energy_consumption_table)
    # create .lp results
    energy_consumption_pie_chart(energy_consumption_table)
    time_bar_graph(execution_time_table)
    asp_taskList(graph)
    asp_resource_library(graph)
    asp_mapping_option()
