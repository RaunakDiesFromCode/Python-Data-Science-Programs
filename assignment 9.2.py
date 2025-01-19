import networkx as nx 
import matplotlib.pyplot as plt 
# Create a directed graph (since PageRank is typically applied to directed graphs) 
G = nx.DiGraph() 
# Add edges (rela onships) represen ng following rela onships in a social network 
edges = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Alice"), 
("Charlie", "Bob"), ("David", "Alice"), ("Eve", "David"), 
("Eve", "Bob"), ("Frank", "Eve"), ("Frank", "Charlie")] 
G.add_edges_from(edges)
# Calculate PageRank 
pagerank_scores = nx.pagerank(G, alpha=0.85)  # alpha is the damping factor 
print("PageRank Scores:", pagerank_scores) 
# Visualize the network with PageRank values 
plt.figure(figsize=(10, 8)) 
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold") 
# Display the PageRank values as node labels 
pagerank_labels = {node: f"{rank:.2f}" for node, rank in pagerank_scores.items()} 
nx.draw_networkx_labels(G, pos, labels=pagerank_labels, font_color="red") 
plt.title("Social Network with PageRank Scores") 
plt.show() 
