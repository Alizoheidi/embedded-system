from tabels import execution_time_table


def add_ressource_library_nodes(graph):
    def fpga(operator):
        return execution_time_table.loc['fpga'][operator]

    graph.add_vertex('fpga', fpga)

    def risc(operator):
        return execution_time_table.loc['risc'][operator]

    graph.add_vertex('risc', risc)

    def hwm(operator):
        return execution_time_table.loc['HWM'][operator]

    graph.add_vertex('HWM', hwm)
