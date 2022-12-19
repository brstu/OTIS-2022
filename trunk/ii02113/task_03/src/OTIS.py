import networkx as nx
from pyvis.network import Network

nodes = ["1"]

net = Network(600, 600)
# first
net.add_nodes([1],
              title=['node 1'],
              label=['1'],
              shape=['triangle'],
              color=['#9370DB'])
net.show_buttons()
net.show("OTIS.html")
