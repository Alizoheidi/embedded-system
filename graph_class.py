
class Graph:
    """
    -1 in connection_matrix mean not connected
    we will find the index of vertex in vertices_list
    and search for it's connections with the index ,in connection_matrix
    interpretation can be a number or a function or anything else
    our matrix will be like
      A  B  C
    A -1 2  3  | it mean A is connected to B and C
    B -1 -1 1  | it mean B is connected to C
    C -1 1 -1  | B and C connected to each other with nondirectional edge
    """

    def __init__(self):
        self.connection_matrix = []
        self.vertices_list = []
        self.vertices_interpretation = {}

    # working with vertices here---------------
    def add_vertex(self, vertex, meaning=None):
        """
        add vertex to vertices list
        and make interpretation with given meaning argument
        return index of the vertex
        if vertex already existed return False
        """
        if vertex in self.vertices_list:
            return False

        length = len(self.vertices_list)
        for connection_list in self.connection_matrix:
            connection_list.append(-1)
        self.connection_matrix.append([-1] * (length + 1))
        self.vertices_list.append(vertex)
        self.vertices_interpretation[vertex] = meaning

        return length

    def make_interpretation(self, vertex, meaning):
        """
        make interpretation or change it and return True
        """
        if vertex not in self.vertices_list:
            # self.add_vertex(vertex,meaning)
            return False
        else:
            self.vertices_interpretation[vertex] = meaning
        return True

    # working with edges methods here----------------------
    def add_directional_edge(self, vertex1, vertex2, cost):
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

        self.connection_matrix[i_v1][i_v2] = cost

        return True

    def add_nondirectional_edge(self, vertex1, vertex2, cost):
        """
        add non directional edge between vertex1 to vertex2 with given cost
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

        self.connection_matrix[i_v1][i_v2] = cost
        self.connection_matrix[i_v2][i_v1] = cost

        return True

    def add_edges_dir(self, from_vertex, **to_vertices):
        """
        add directional edge from_vertex to_vertices with given
        from_vertex : vertex
        to_vertex: **vertex=cost | vertex should'nt be str ; A=1 connect to 'A' with cost 1
        return True
        """
        for to_v_c in to_vertices.items():
            self.add_directional_edge(from_vertex, to_v_c[0], to_v_c[1])
        return True

    def add_edges_nondir(self, from_vertex, **to_vertices):
        """
        add non-directional edge from_vertex to_vertices with given
        from_vertex : vertex
        to_vertex: **vertex=cost | vertex shouldn't be str ; A=1 connect to 'A' with cost 1
        return True
        """
        for to_v_c in to_vertices.items():
            self.add_nondirectional_edge(from_vertex, to_v_c[0], to_v_c[1])
        return True

    def cheapest_connection(self, vertex):
        """
        return the cheapest connection (connection with lowest cost) from connection list of vertex
        return in form (next vertex,cost)
        """
        connection_list = self.cost_list(vertex)
        connection_fillter = list(filter(lambda co: co != -1, connection_list))
        cheapest = min(connection_fillter)
        index = connection_list.index(cheapest)
        return (self.vertices_list[index], cheapest)

    def get_vertex(self, meaning):
        """
        return the vertex with given interpretation
        return False if it's not exit
        """
        try:
            index = list(self.vertices_interpretation.values()).index(meaning)
            return self.vertices_list[index]
        except:
            return False

    def cost_list(self, vertex):
        """
        return list of connections of vertex
        """
        index = self.vertices_list.index(vertex)
        return self.connection_matrix[index]

    def connected_vertices(self, vertex):
        """
        return list of connected vertices with cost of the given vertex
        in form (connected vertex,cost)
        """
        cost_list = self.cost_list(vertex)
        connected_list = []
        for i in range(len(cost_list)):
            cost = cost_list[i]
            if cost != -1:
                connected_list.append((self.vertices_list[i], cost))
        return connected_list

    def all_connections(self):
        """
        print all connections in form:
            vertex: list of connections
        """
        s = ''
        for vertex in self.vertices_list:
            s += str(vertex) + ':' + str(self.connected_vertices(vertex)) + '\n'
        print(s)

    def graph_dict(self):
        """
        return a dictionary wich map any vertex to it's connections' list
        """
        connection_dict = {}
        for vertex in self.vertices_list:
            connection_dict[vertex] = self.connected_vertices(vertex)
        return connection_dict

    def graph_table(self):
        """
        print graph table
        """
        s = ''
        for i in range(len(self.vertices_list)):
            cost_list = self.connection_matrix[i]
            s += str(self.vertices_list[i]) + '==>>'
            for j in range(len(cost_list)):
                s += '|' + str(self.vertices_list[j]) + ':' + str(self.connection_matrix[i][j]) + '|'
            s += '\n'
        print(s)

    def give_edge(self, vertex1, vertex2):
        v_connections = self.cost_list(vertex1)
        v_next_index = self.vertices_list.index(vertex2)
        return v_connections[v_next_index]
