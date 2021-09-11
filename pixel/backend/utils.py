import numpy as np
from PIL import Image
from django.shortcuts import get_object_or_404

from .models import ImageModel, PixelCount


def pixel_count_add(image_id):
    image = get_object_or_404(ImageModel, id=image_id)
    img = Image.open(image.image).convert("RGB")
    img = np.array(img)

    def rgb_to_hex(inarray):
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

    pixel = PixelCount(
        image=image,
        hex_colors=json_colors,
        black_or_white=black_or_white
    )
    pixel.save()
