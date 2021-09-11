import numpy as np
from PIL import Image
import re


image = Image.open('file.jpeg').convert("RGB")
img = np.array(image)
height = img.shape[0]
width = img.shape[1]


def rgb_to_hex(inarray):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (inarray[0], inarray[1], inarray[2])


colors, counts = np.unique(img.reshape(-1, 3), axis=0, return_counts=1)
json_colors = dict(
    zip(
        [rgb_to_hex(i) for i in colors],
        [int(j) for j in counts]
    )
)

count_black = json_colors.get('#000000', 0)
count_white = json_colors.get('#ffffff', 0)

if count_black > count_white:
    black_or_white = 'black'
elif count_white > count_black:
    black_or_white = 'white'
else:
    black_or_white = 'equal'


print(json_colors["#000000"])
print(black_or_white)

a = re.search('^#[0-9A-Fa-f]{6}$', '#aabcc')
if a:
    print(a.group(0))

# print(json_colors.get(black, 0))
# print(json_colors.get(white, 0))


# print(colors, counts)

# for i in range(len((colors))):
#     json_colors[rgb_to_hex(colors[i])] = counts[i]
# for i in range(height):
#     for j in range(width):
#         r = img[i][j][0]
#         g = img[i][j][1]
#         b = img[i][j][2]
#         hex = rgb_to_hex(r, g, b)
#         if hex in dict:
#             dict[hex] += 1
#         else:
#             dict[hex] = 1

# print(dict)
