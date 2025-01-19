import networkx as nx 
import matplotlib.pyplot as plt 
import community as community_louvain  # Import the Louvain method 
# Create a sample social network graph 
G = nx.karate_club_graph()  # Using the classic karate club graph for example purposes 
# Apply the Louvain method for community detec on 
partition = community_louvain.best_partition(G) 
# Visualize the communities 
plt.figure(figsize=(10, 8)) 
pos = nx.spring_layout(G) 
# Assign colors to nodes based on the detected communi es 
colors = [partition[node] for node in G.nodes()] 
nx.draw(G, pos, node_color=colors, with_labels=True, node_size=500, cmap=plt.cm.rainbow) 
plt.title("Community Detec on using Louvain Method") 
plt.show() 
# Print community structure 
print("Detected communities:") 
for community_id in set(partition.values()): 
    community_nodes = [node for node, community in partition.items() if community == community_id] 
    print(f"Community {community_id}: {community_nodes}") 