from PIL import Image
import numpy as np


objects = {
    (255, 255, 255): "*",
    (0, 0, 0): "+",
    (0, 255, 0): ".",
    (255, 0, 0): "A",
}

img = Image.open('test.png')
img = img.convert(mode="1", dither=Image.NONE)
array = np.array(img, dtype=np.uint8)

print("Raw map: ")
print(array)

img = Image.open("test.png")
array = np.array(img, dtype=np.uint8)

res = []
for i, row in enumerate(array):
    tmp = ""
    for j, el in enumerate(row):
        tmp += objects[tuple(el)]
    res.append(tmp)

print("After 'render': ")
print("\n".join(res))
