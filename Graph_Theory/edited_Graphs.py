import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()

# Load the edges from file.
DG = nx.read_edgelist('C:\\Users\\tejve\\Desktop\\edges_11.6.csv', delimiter=',',create_using=nx.DiGraph(),
                      data=[('weight',float),('direction',str),('street',str)])

# View the edges information.
DG.edges(data=True)

Building_node={'56':["Smith Music Hall","805 S. Mathews Avenue"],'164':["Foreign Languages Building","707 S. Mathews Avenue"],
               '148':["Davenport Hall","607 S. Mathews Avenue"],'712':["Noyes Laboratory","600 S. Mathews Avenue"],
               '384':["Illini Union","1401 W. Green Street"],'382':["Altgeld Hall","1409 W. Green Street"],
               '334':["Henry Admin Building","506 S. Wright Street"],'460':["English Building","608 S. Wright Street"],
               '446':["Lincoln Hall","702 S. Wright Street"],'462':["Gregory Hall","810 S. Wright Street"],
               '716':["Psychology Building","603 E. Daniel Street"],'317':["Illini Union Bookstore","807 S. Wright Street"],
               '304':["Swanlund Admin Building","601 E. John Street"],'320':["Coble Hall","801 S. Wright Street"],
               '306':["Student Services Arcade Building","610 E. John Street"],'372':["Illini Hall","721 S. Wright Street"],
               '493':["School of Information Science","501 E. Daniel Street"],'400':["International Studies Building","910 S. Fifth Street"],
               '479':["912 S. Fifth","912 S. Fifth Street"],'504':["School of Labor and Employment Relations","504 E. Armory Avenue"],
               '525':["Ice Arena","406 E. Armory Avenue"],'530':["Irwin Academic Services Center","402 E. Armory Avenue"],
               '523':["Police Training Institute","1004 S. Fourth Street"],'490':["Sherman Hall","909 S. Fifth Street"]}

Cross_sectional_node={"GG":"S.Goodwin-W.Green","GO":"S.Goodwin-W.Oregon","GN":"S.Goodwin-W.Neveda","MG":"S.Mathews-W.Green",
                      "MO":"S.Mathews-W.Oregon","MN":"S.Mathews-W.Neveda","WG":"S.Wright-W.Green","WJ":"S.Wright-E.John",
                      "WD":"S.Wright-E.Daniel","WC":"S.Wright-E.Chalmers","WA":"S.Wright-E.Armory","6G":"S.6th-W.Green",
                      "6J":"S.6th-E.John","6D":"S.6th-E.Daniel","6C":"S.6th-E.Chalmers","6A":"S.6th-E.Armory",
                      "5G":"S.5th-W.Green","5J":"S.5th-E.John","5D":"S.5th-E.Daniel","5C":"S.5th-E.Chalmers",
                      "5A":"S.5th-E.Armory","4G":"S.4th-W.Green","4J":"S.4th-E.John","4D":"S.4th-E.Daniel",
                      "4C":"S.4th-E.Chalmers","4A":"S.4th-E.Armory"}

# Load the information of each node.
for key in Building_node.keys():
    DG.node[key]['name']=Building_node[key][0]
    DG.node[key]['street']=Building_node[key][1]

for key in Cross_sectional_node.keys():
    DG.node[key]['name']=Cross_sectional_node[key]

# View the edges information.
DG.nodes(data=True)
print (nx.info(DG))
nx.draw(DG)
plt.show()