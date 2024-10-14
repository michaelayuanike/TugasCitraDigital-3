
import imageio.v3 as image
import numpy as np

path = "C:\\citra digital\\FB_IMG_1687263642651.jpg"
my_image = image.imread(path)

# Check if the image is RGB
print('my_image.shape')
if(len(my_image.shape) < 3):
    print("gambar input harus RGB")
    exit()

# Extract red, green, and blue channels
red = my_image[:,:,0]
image_red = np.zeros_like(my_image)
image_red[:,:,0] = red

green = my_image[:,:,1]
image_green= np.zeros_like(my_image)
image_green[:,:,1] = green

blue = my_image[:,:,2]
image_blue= np.zeros_like(my_image)
image_blue[:,:,2] = blue

# Create grayscale image (black and white)
# Using the weighted sum method: 0.2989*R + 0.5870*G + 0.1140*B
grayscale = 0.2989 * red + 0.5870 * green + 0.1140 * blue
grayscale_image = np.zeros_like(my_image)
grayscale_image[:,:,0] = grayscale
grayscale_image[:,:,1] = grayscale
grayscale_image[:,:,2] = grayscale

# Save the images
image.imwrite("C:\\citra digital\\gbr_merah.jpg", image_red)
image.imwrite("C:\\citra digital\\gbr_hijau.jpg", image_green)
image.imwrite("C:\\citra digital\\gbr_biru.jpg", image_blue)
image.imwrite("C:\\citra digital\\gbr_bw.jpg", grayscale_image)

print(f"Dimensi gambar adalah {my_image.shape}")
print("proses selesai")
