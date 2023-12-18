
import mmap
import cv2 as cv
import numpy as np
shape = (800, 600, 4)
image_size = np.prod(shape)
if __name__ == '__main__':
    shmem = mmap.mmap(-1, image_size, "shm")
    shmem.seek(0)
    buf = shmem.read(image_size)
    print(buf)
    img = np.frombuffer(buf, dtype=np.uint8).reshape(shape)

    cv.imwrite("img.png", img)
    shmem.close()
