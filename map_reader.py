from PIL import Image
import numpy as np


img = Image.open('test.png')
img = img.convert(mode="1", dither=Image.NONE)
array = np.array(img, dtype=np.uint8)
print(array)
