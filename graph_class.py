
class Graph:
    """
    -1 in adjacency matrix means not connected
    we will find the index of vertex in vertices_list
    and search for its connections with the index ,in adjacency matrix
    interpretation can be a number or a function or anything else
    our matrix will be like
      A  B  C
    A -1 1  1     | it mean A is connected to B and C
    B -1 -1 1  | it mean B is connected to C
    C -1 1 -1  | B and C connected to each other with non-directional edge
    """

    def __init__(self):
        self.adjacency_matrix = []
        self.vertices_list = []
        self.vertices_functions = {}

    # working with vertices here---------------
    def add_vertex(self, vertex, function=None):
        """
        add vertex to vertices list
        and make function with given meaning argument
        return index of the vertex
        if vertex already existed return False
        """
        if vertex in self.vertices_list:
            return False

        length = len(self.vertices_list)
        for connection_list in self.adjacency_matrix:
            connection_list.append(-1)
        self.adjacency_matrix.append([-1] * (length + 1))
        self.vertices_list.append(vertex)
        self.vertices_functions[vertex] = function

        return length

    # working with edges methods here----------------------
    def add_directional_edge(self, vertex1, vertex2, cost=1):
        """
        add directional edge from vertex1 to vertex2 with given cost
        return True
        """
        if vertex1 not in self.vertices_list:
            i_v1 = self.add_vertex(vertex1)
        else:
            i_v1 = self.vertices_list.index(vertex1)
        if vertex2 not in self.vertices_list:
            i_v2 = self.add_vertex(vertex2)
        else:
            i_v2 = self.vertices_list.index(vertex2)

        self.adjacency_matrix[i_v1][i_v2] = cost

        return True

    def add_nondirectional_edge(self, vertex1, vertex2, cost=1):
        """
        add non-directional edge between vertex1 to vertex2 with given cost
        return True
        """
        if vertex1 not in self.vertices_list:
            i_v1 = self.add_vertex(vertex1)
        else:
            i_v1 = self.vertices_list.index(vertex1)
        if vertex2 not in self.vertices_list:
            i_v2 = self.add_vertex(vertex2)
        else:
            i_v2 = self.vertices_list.index(vertex2)

        self.adjacency_matrix[i_v1][i_v2] = cost
        self.adjacency_matrix[i_v2][i_v1] = cost

        return True

    def cost_list(self, vertex):
        """
        return list of connections of vertex
        """
        index = self.vertices_list.index(vertex)
        return self.adjacency_matrix[index]

    def connected_vertices(self, vertex):
        """
        return list of connected vertices
        """
        cost_list = self.cost_list(vertex)
        connected_list = []
        for i in range(len(cost_list)):
            cost = cost_list[i]
            # if it's connected
            if cost != -1:
                connected_list.append(self.vertices_list[i])
        return connected_list

    def give_nondirected_edges(self,vertex):
        """
        :param vertex: vertex name
        :return: all non-directional edges of the given vertex
        """
        v_connected = self.connected_vertices(vertex)
        nondir_edge_list = []
        for v in v_connected:
            if vertex in self.connected_vertices(v):
                nondir_edge_list.append(v)
        return nondir_edge_list

    def give_directed_edges(self,vertex):
        """
        :param vertex: vertex name
        :return: all directional edges of the given vertex
        """
        v_connected = self.connected_vertices(vertex)
        dir_edge_list = []
        for v in v_connected:
            if vertex not in self.connected_vertices(v):
                dir_edge_list.append(v)
        return dir_edge_list

