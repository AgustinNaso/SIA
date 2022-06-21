from PIL import Image
import numpy as np


def show_image_from_array(image_array, shape, label):
    img = image_array.reshape(shape) * 255
    image = Image.fromarray(np.array(img).astype(np.uint8))
    image.show(title= label)

def image_to_image_array(img, shape):
    img = img.convert("RGB")
    img = img.resize(shape)
    img = np.asarray(img, dtype=np.float32) / 255
    img = img[:, :, :3]
    return img