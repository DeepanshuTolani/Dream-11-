# import matplotlib.pyplot as plt

# features = ['Runs Scored', 'Wickets Taken', 'Form Index', 'Venue Perf.']
# importance = [0.35, 0.30, 0.20, 0.15]  # Example values

# plt.barh(features, importance, color='#FF9800')
# plt.title('Feature Importance in Random Forest')
# plt.xlabel('Importance Score')
# plt.savefig('feature_importance.png') 

# import matplotlib.pyplot as plt

# # Example player data (adapt based on your predictions)
# players = ['Virat Kohli', 'Hardik Pandya', 'Jasprit Bumrah', 'Rohit Sharma']
# points = [75, 60, 55, 70]  # Hypothetical projected points

# # Create bar chart
# plt.figure(figsize=(10, 6))
# bars = plt.bar(players, points, color='#2196F3', width=0.6)
# plt.title('Projected Dream11 Fantasy Points', fontsize=14)
# plt.ylabel('Fantasy Points', fontsize=12)
# plt.ylim(0, 100)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', fontsize=10)
# plt.tight_layout()
# plt.savefig('player_recommendation.png', dpi=100)
# plt.show()

# import matplotlib.pyplot as plt

# # Data from your paper
# models = ['Random Forest', 'XGBoost', 'Neural Networks']
# accuracy = [78, 85, 83]

# # Create bar chart
# plt.figure(figsize=(8, 5))
# plt.bar(models, accuracy, color=['#4CAF50', '#FF5722', '#2196F3'], width=0.5)
# plt.title('Model Performance Comparison', fontsize=14, pad=10)
# plt.ylabel('Accuracy (%)', fontsize=12)
# plt.ylim(0, 100)
# plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid for authenticity
# for i, v in enumerate(accuracy):
#     plt.text(i, v + 2, str(v) + '%', ha='center', fontsize=10)  # Manual value labels
# plt.tight_layout()
# plt.savefig('performance_comparison.png', dpi=100)
# plt.show()

from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='System Architecture for Dream11 Prediction', format='png')

# Set graph attributes for a simple, non-AI look
dot.attr(rankdir='LR')  # Left-to-right layout
dot.attr('node', shape='rectangle', style='filled', fillcolor='lightblue', fontname='Arial')
dot.attr('edge', arrowhead='normal', color='black')

# Add nodes (modules)
dot.node('A', 'Data Processing\nModule')
dot.node('B', 'Feature Extraction\nModule')
dot.node('C', 'Machine Learning\nModels')
dot.node('D', 'Prediction\nModule')

# Add input/output nodes (smaller, distinct style)
dot.node('IPL', 'IPL Data\n(2008-2017)', shape='ellipse', fillcolor='lightgreen')
dot.node('KF', 'Key Features', shape='note', fillcolor='lightyellow')
dot.node('TM', 'Trained Models', shape='note', fillcolor='lightyellow')
dot.node('PR', 'Player Rankings', shape='ellipse', fillcolor='lightgreen')
dot.node('FS', 'Fantasy Scores', shape='ellipse', fillcolor='lightgreen')

# Add edges (connections)
dot.edge('IPL', 'A')  # Input to Data Processing
dot.edge('A', 'B')    # Data Processing to Feature Extraction
dot.edge('B', 'KF')   # Feature Extraction outputs Key Features
dot.edge('B', 'C')    # Feature Extraction to ML Models
dot.edge('C', 'TM')   # ML Models outputs Trained Models
dot.edge('C', 'D')    # ML Models to Prediction
dot.edge('D', 'PR')   # Prediction outputs Player Rankings
dot.edge('D', 'FS')   # Prediction outputs Fantasy Scores

# Render the diagram to a file
dot.render('cloud_diagram', view=True) # Saves as 'system_architecture.png' and opens it
print("Diagram generated as 'system_architecture.png'")