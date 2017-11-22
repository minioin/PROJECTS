import networkx as nx


class Network():
    """
    >>> graph = nx.read_edgelist('edges_11.11.csv', delimiter=',', data=[('weight', float), ('direction', str), ('street', str)], create_using=nx.DiGraph())
    >>> nx.dijkstra_path(graph, '446', '493')
    ['446', 'WC', '6C', '479', '5C', '490', '400', '5D', '493']
    >>> nx.dijkstra_path(graph, '164','56')
    Traceback (most recent call last):
    ...
    networkx.exception.NetworkXNoPath: No path to 56.
    """

    def __init__(self):
        self.DG = nx.DiGraph()
        self.add_edges('edges_11.11.csv')
        self.add_nodes()

    def add_edges(self, path=''):
        """Given a edges file path(as a string), using build-in function in networkx to create Digraph
        :param path: file path as a string
        :return: a Directed graph

        """
        self.DG = nx.read_edgelist(path, delimiter=',',
                                   data=[('weight', float), ('direction', str), ('street', str)],
                                   create_using=self.DG)
        return self.DG

    def add_nodes(self):
        """add attributes to nodes from the add_edges() function
        :return:

        """
        Building_node = {'56': ["Smith Music Hall", "805 S. Mathews Avenue"],
                         '164': ["Foreign Languages Building", "707 S. Mathews Avenue"],
                         '148': ["Davenport Hall", "607 S. Mathews Avenue"],
                         '712': ["Noyes Laboratory", "600 S. Mathews Avenue"],
                         '384': ["Illini Union", "1401 W. Green Street"],
                         '382': ["Altgeld Hall", "1409 W. Green Street"],
                         '334': ["Henry Admin Building", "506 S. Wright Street"],
                         '460': ["English Building", "608 S. Wright Street"],
                         '446': ["Lincoln Hall", "702 S. Wright Street"],
                         '462': ["Gregory Hall", "810 S. Wright Street"],
                         '716': ["Psychology Building", "603 E. Daniel Street"],
                         '317': ["Illini Union Bookstore", "807 S. Wright Street"],
                         '304': ["Swanlund Admin Building", "601 E. John Street"],
                         '320': ["Coble Hall", "801 S. Wright Street"],
                         '306': ["Student Services Arcade Building", "610 E. John Street"],
                         '372': ["Illini Hall", "721 S. Wright Street"],
                         '493': ["School of Information Science", "501 E. Daniel Street"],
                         '400': ["International Studies Building", "910 S. Fifth Street"],
                         '479': ["912 S. Fifth", "912 S. Fifth Street"],
                         '504': ["School of Labor and Employment Relations", "504 E. Armory Avenue"],
                         '525': ["Ice Arena", "406 E. Armory Avenue"],
                         '530': ["Irwin Academic Services Center", "402 E. Armory Avenue"],
                         '523': ["Police Training Institute", "1004 S. Fourth Street"],
                         '490': ["Sherman Hall", "909 S. Fifth Street"]}

        Cross_sectional_node = {"GG": "S.Goodwin-W.Green", "GO": "S.Goodwin-W.Oregon", "GN": "S.Goodwin-W.Neveda",
                                "MG": "S.Mathews-W.Green",
                                "MO": "S.Mathews-W.Oregon", "MN": "S.Mathews-W.Neveda", "WG": "S.Wright-W.Green",
                                "WJ": "S.Wright-E.John",
                                "WD": "S.Wright-E.Daniel", "WC": "S.Wright-E.Chalmers", "WA": "S.Wright-E.Armory",
                                "6G": "S.6th-W.Green",
                                "6J": "S.6th-E.John", "6D": "S.6th-E.Daniel", "6C": "S.6th-E.Chalmers",
                                "6A": "S.6th-E.Armory",
                                "5G": "S.5th-W.Green", "5J": "S.5th-E.John", "5D": "S.5th-E.Daniel",
                                "5C": "S.5th-E.Chalmers",
                                "5A": "S.5th-E.Armory", "4G": "S.4th-W.Green", "4J": "S.4th-E.John",
                                "4D": "S.4th-E.Daniel",
                                "4C": "S.4th-E.Chalmers", "4A": "S.4th-E.Armory"}

        # Load the information of each node.
        for key in Building_node.keys():
            self.DG.add_node(key, name=Building_node[key][0], street=Building_node[key][1])

        for key in Cross_sectional_node.keys():
            self.DG.add_node(key, name=Cross_sectional_node[key])

        ordered_building = sorted(Building_node.items(), key=lambda t: t[1][0])

        print('Building Name and its Mail Code will be listed as followed.')
        for k, v in ordered_building:  # print building name and mail code
            print('{}: {}'.format(v[0], k))
        return self.DG

    def shortest_path_output(self, start=None, end=None):
        """output shortest path following the following format.
        :param start starting building of the navigation
        :param end ending building of the navigation
        :return
        """
        shortest_path_list = nx.dijkstra_path(self.DG, start, end)
        nodes_name = nx.get_node_attributes(self.DG, 'name')
        start_name = nodes_name[shortest_path_list[0]]
        end_name = nodes_name[shortest_path_list[-1]]
        print('Travel from {} to {}:'.format(start_name, end_name))
        edges_street = nx.get_edge_attributes(self.DG, 'street')
        edges_direction = nx.get_edge_attributes(self.DG, 'direction')
        for i in range(len(shortest_path_list) - 1):
            street = edges_street[(shortest_path_list[i], shortest_path_list[i + 1])]
            direction = edges_direction[(shortest_path_list[i], shortest_path_list[i + 1])]
            if i == 0:
                print('\tStarting on {}, turn {}'.format(street, direction))
            else:
                if street == old_street:
                    pass

                else:
                    print('\tAt {}, turn {}'.format(street, direction))

            old_street = street
        print('Proceed until you arrive at {}'.format(end_name))

    def input_request(self):
        while True:
            start_end = input('\nEnter q to quit. \nEnter starting and ending mail codes to get the navigation: ')
            if start_end in ['q', 'Q']:
                print('Quit!')
                break
            try:
                se_list = start_end.split()
                start = se_list[0]
                end = se_list[1]
                self.shortest_path_output(start, end)
            except Exception:
                print('\nIn our map, no path between these two buildings.')


if __name__ == '__main__':
    test = Network()
    test.input_request()
