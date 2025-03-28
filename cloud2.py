import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Team': ['CSK', 'MI', 'RCB', 'KKR'],
    'Total Matches': [165, 171, 168, 162],
    'Batsmen Points (%)': ['55% (45,210)', '50% (42,750)', '60% (50,400)', '45% (36,450)'],
    'Bowlers Points (%)': ['30% (24,720)', '35% (29,925)', '25% (21,000)', '35% (28,350)'],
    'All-Rounders Points (%)': ['15% (12,360)', '15% (12,825)', '15% (12,600)', '20% (16,200)'],
    'Total Dream11 Points': [82290, 85500, 84000, 81000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 2.5))
ax.axis('tight')
ax.axis('off')

# Create table
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Customize
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.title("Fig. 1.5: IPL Team Performance by Role (2008-2017)", pad=20)

# Save as image
plt.savefig('fig_1_5_new_table.png', bbox_inches='tight', dpi=100)
plt.close()
print("Table saved as 'fig_1_5_new_table.png'")