import networkx as nx 
import matplotlib.pyplot as plt 
# Create a social network graph 
G = nx.Graph() 
# Add nodes (individuals) 
G.add_nodes_from(["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]) 
# Add edges (rela onships) 
G.add_edges_from([("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), 
("Charlie", "David"), ("Emma", "David"), ("Frank", "Alice")]) 
# Calculate centrality measures 
degree_centrality = nx.degree_centrality(G) 
betweenness_centrality = nx.betweenness_centrality(G) 
closeness_centrality = nx.closeness_centrality(G) 
print("Degree Centrality:", degree_centrality) 
print("Betweenness Centrality:", betweenness_centrality) 
print("Closeness Centrality:", closeness_centrality) 
# Draw the graph with labels 
plt.figure(figsize=(8, 6)) 
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight="bold" ) 
plt.title("Social Network Graph") 
plt.show() 


