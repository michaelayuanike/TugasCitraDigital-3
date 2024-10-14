import imageio
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image_path = "C:\citra digital\gbr_bw.jpg"
image = imageio.imread(image_path)

# Calculate the histogram
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.plot(bin_edges[0:-1], histogram, color='black')
plt.title("Grayscale Histogram")
plt.xlabel("Grayscale value")
plt.ylabel("Pixel count")
plt.grid(True)
plt.show()

# Return the histogram data
histogram
