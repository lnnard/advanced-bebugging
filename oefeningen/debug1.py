import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)  # For reproducibility
x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 100  # Variable point sizes
colors = np.random.rand(100)  # Variable colors

# Create a colormap
cmap = cm.get_cmap('viridis')

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap=cmap, edgecolor='w', linewidth=0.5)

# Add a color bar
colorbar = plt.colorbar(scatter)
colorbar.set_label('Color Scale', fontsize=12)

# Add labels and title
plt.title('Very cool Scatter Plot', fontsize=16, fontweight='bold')
plt.xlabel('X-axis Label', fontsize=12)
plt.ylabel('Y-axis Label', fontsize=12)

# Style adjustments
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()
