from PIL import Image
import numpy as np

# Color means object in the game
WHITE = (255, 255, 255)  # road
BLACK = (0, 0, 0)  # wall
GREEN = (0, 255, 0)  # bush
RED = (255, 0, 0)  # exit

map = [
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
    [BLACK, WHITE, BLACK, BLACK, BLACK, WHITE, WHITE, WHITE, WHITE, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, GREEN, WHITE, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, GREEN, WHITE, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, WHITE, WHITE, BLACK],
    [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, WHITE, WHITE, BLACK],
    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, BLACK]
]

nparray = np.array(map, dtype=np.uint8)

resultim = Image.fromarray(nparray)
resultim.save('test.png')
