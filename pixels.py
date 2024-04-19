from PIL import Image as im
import numpy as np

threshold = (160, 160, 160)
image = im.open('image.png', 'r')

pixel_values = list(image.getdata())


type_A = 0
type_B = 0
for pixel in pixel_values:
    if pixel > threshold:
        type_A += 1
    else:
        type_B += 1

print("typeA percentage: ", 100*type_A/(type_A + type_B))
print("typeB percentage: ", 100*type_B/(type_A + type_B))


brightness_vals = [(0.21*rgb[0] + 0.72*rgb[1] + 0.07*rgb[2])/3 for rgb in pixel_values  ]



brightness_level = sum(brightness_vals)/ len(brightness_vals)

bw_photo = [0 if val > brightness_level else 1 for val in brightness_vals ]
arr = np.array(bw_photo)

new_image = im.fromarray(arr, mode="1")
new_image.save('new_image.png')

