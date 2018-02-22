import networkx as nx
import matplotlib.pyplot as plt
g=nx.DiGraph()

Building_node={56:["Smith Music Hall","805 S. Mathews Avenue"],164:["Foreign Languages Building","707 S. Mathews Avenue"],148:["Davenport Hall","607 S. Mathews Avenue"],712:["Noyes Laboratory","600 S. Mathews Avenue"],384:["Illini Union","1401 W. Green Street"],382:["Altgeld Hall","1409 W. Green Street"],334:["Henry Admin Building","506 S. Wright Street"],
460:["English Building","608 S. Wright Street"],446:["Lincoln Hall","702 S. Wright Street"],462:["Gregory Hall","810 S. Wright Street"],716:["Psychology Building","603 E. Daniel Street"],
317:["Illini Union Bookstore","807 S. Wright Street"],304:["Swanlund Admin Building","601 E. John Street"],320:["Coble Hall","801 S. Wright Street"],306:["Student Services Arcade Building","610 E. John Street"],
372:["Illini Hall","721 S. Wright Street"],493:["School of Information Science","501 E. Daniel Street"],400:["International Studies Building","910 S. Fifth Street"],479:["912 S. Fifth","912 S. Fifth Street"],504:["School of Labor and Employment Relations","504 E. Armory Avenue"],525:["Ice Arena","406 E. Armory Avenue"],
530:["Irwin Academic Services Center","402 E. Armory Avenue"],523:["Police Training Institute","1004 S. Fourth Street"],490:["Sherman Hall","909 S. Fifth Street"]}

Cross_sectional_node={"GG":"S.Goodwin-W.Green","GO":"S.Goodwin-W.Oregon","GN":"S.Goodwin-W.Neveda","MG":"S.Mathews-W.Green","MO":"S.Mathews-W.Oregon","MN":"S.Mathews-W.Neveda","WG":"S.Wright-W.Green","WJ":"S.Wright-E.John","WD":"S.Wright-E.Daniel","WC":"S.Wright-E.Chalmers","WA":"S.Wright-E.Armory","6G":"S.6th-W.Green","6J":"S.6th-E.John","6D":"S.6th-E.Daniel",
                      "6C":"S.6th-E.Chalmers","6A":"S.6th-E.Armory","5G":"S.5th-W.Green","5J":"S.5th-E.John","5D":"S.5th-E.Daniel","5C":"S.5th-E.Chalmers","5A":"S.5th-E.Armory","4G":"S.4th-W.Green","4J":"S.4th-E.John","4D":"S.4th-E.Daniel","4C":"S.4th-E.Chalmers","4A":"S.4th-E.Armory"}

for key in Building_node.keys():

    g.add_node(key,name=Building_node[key][0],street=Building_node[key][1])

for key in Cross_sectional_node.keys():

    g.add_node(key,name=Cross_sectional_node[key][0])

print (g.node)
print (g.nodes())
print (nx.info(g))



#print (nx.draw(g,with_labels=True))
#plt.show()


#g.add_node(322,name="ischool")
#g.add_node(123,name="Thomas")
#g.add_node(456,name="ischool")
#g.add_node(676,name="ischool")
#g.add_node(909,name="ischool")
#g.add_edges_from(1,3,distance=2)
#nx.dijkstra_path(g,322,123,dis)
#nx.draw(g)
#plt.show()
#print (nx.info(g))
#print (g.add_edges_from())




#g.add_node(2)
#g.add_node(5)
#g.add_nodes_from([4,3,1])
#g.add_edge(2,5)
#g.add_edge(4,1)
#g.add_edges_from([(2,5),(1,3)])
#print (nx.info
#G.add_edges_from([(1, 2), (1, 3)])
#G.add_node(1)
#G.add_edge(1, 2)
#G.add_node("spam")        # adds node "spam"
#G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
#G.add_edge(3, 'm')
#FG = nx.Graph()
#FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
#FG[3][4]['color']="red"
#print (FG.adj.items())
#DG = nx.DiGraph()
#DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
#nx.draw(DG)
#plt.show()
#print (nx.info(FG))
