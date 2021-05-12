"""An engine for creating memes: text on images."""

import os
import random

from PIL import Image, ImageFont, ImageDraw

class MemeEngine():
    """Put the text on the image."""
    # https://www.geeksforgeeks.org/python-pil-imagedraw-draw-text/
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

    def __init__(self, output_dir):
        """initialize the variables."""
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make the meme."""
        img = Image.open(img_path)

        if width is not None:
            if width > 500:
                width = 500
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',size=20)
            draw.text((5, 5), f'"{text}" - {author}', font = font, fill = 'white')
        rand_num = random.randint(0, 1000)
        out_file = os.path.join(self.output_dir, f'/{rand_num}.jpg')
        img.save(out_file)
        return out_file
