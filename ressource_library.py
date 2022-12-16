import json

with open('resource_library.json') as json_file:
    resource_lib_dict = json.load(json_file)
PROCESSORS_NAME = list(resource_lib_dict.keys())


def add_resource_library_nodes(graph):
    """
    :param graph: Graph object
    this function will add resource library nodes to the given graph
    and also define functions for them
    each function return clock rate , frequency , consume power
    """

    def fpga():
        return resource_lib_dict[PROCESSORS_NAME[0]]['type'], \
               resource_lib_dict[PROCESSORS_NAME[0]]['CPI'], \
               resource_lib_dict[PROCESSORS_NAME[0]]['frequency'], \
               resource_lib_dict[PROCESSORS_NAME[0]]['consume power'], \
               resource_lib_dict[PROCESSORS_NAME[0]]['clock rate']

    graph.add_vertex(PROCESSORS_NAME[0], fpga())

    def risc():
        return resource_lib_dict[PROCESSORS_NAME[1]]['type'], \
               resource_lib_dict[PROCESSORS_NAME[1]]['CPI'], \
               resource_lib_dict[PROCESSORS_NAME[1]]['frequency'], \
               resource_lib_dict[PROCESSORS_NAME[1]]['consume power'], \
               resource_lib_dict[PROCESSORS_NAME[1]]['clock rate']

    graph.add_vertex(PROCESSORS_NAME[1], risc())

    def cisc():
        return resource_lib_dict[PROCESSORS_NAME[2]]['type'], \
               resource_lib_dict[PROCESSORS_NAME[2]]['CPI'], \
               resource_lib_dict[PROCESSORS_NAME[2]]['frequency'], \
               resource_lib_dict[PROCESSORS_NAME[2]]['consume power'], \
               resource_lib_dict[PROCESSORS_NAME[2]]['clock rate']

    graph.add_vertex(PROCESSORS_NAME[2], cisc())
