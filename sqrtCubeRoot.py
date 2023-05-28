import math
import numpy as np

numbers = range(1, 1001)

for num in numbers:
    sqr_root = math.sqrt(num)
    fr,whole = math.modf(sqr_root)
    if fr == 0.00:
        sqr_root = int(sqr_root)

    cub_root = np.cbrt(num)
    fr,whole = math.modf(cub_root)
    if fr == 0.00:
        cub_root = int(cub_root)
    if isinstance(sqr_root, int) and isinstance(cub_root, int):
        print(num)
        print("sqr_root:", sqr_root)
        print("cub_root:", cub_root)
        print("---------------------------------------")