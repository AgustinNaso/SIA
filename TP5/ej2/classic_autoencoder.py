import numpy as np
import json
from TP5.helpers.plot_helpers import plot_comparison_no_noise
from TP5.helpers.mlp_helper import create_multilayer_perceptron_and_train
from TP5.helpers.image_helper import show_image_from_array, image_to_image_array
import os
from PIL import Image


with open("config.json") as jsonFile:
    config = json.load(jsonFile)
    jsonFile.close()

data_folder = config['data_folder']
images_folder = os.path.join(data_folder, config['images_folder'])
images_shape = config['images_shape']
width = images_shape['width'] if 'width' in images_shape else 16
height = images_shape['height'] if 'height' in images_shape else 16
images_shape = (width, height)

saves_folder = config['saves_folder']

# defining the key parameters
colors_dim = 3  # rgb

# Parameters of the input images (handwritten digits)
original_dim = images_shape[0] * images_shape[1] * colors_dim

if not os.path.exists(images_folder) or not os.path.isdir(images_folder):
    print(f'ERROR: Missing images folder')

images = [file for file in os.listdir(images_folder) if file.endswith(('jpeg', 'png', 'jpg'))]
images = [images[0]]  # remove later
x = []
processed = 0
for image in images:
    full_path = os.path.join(images_folder, image)
    img = Image.open(full_path)
    if len(img.split()) >= 3:
        img = image_to_image_array(img, images_shape)
        x.append(img)

        processed += 1

print(f"Loaded {processed} out of {len(images)} images with shape {images_shape}")

if (processed == 0): exit(1)

x = np.array(x)
(x_train, y_train), (x_test, y_test) = (x, x), (x, x)
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
layers = np.array([100, 20, 10, 20, 100])
learning_rate = 0.0005
epoch: int = 1

perceptron = create_multilayer_perceptron_and_train(x_train, x_train, learning_rate, epoch, layers, 10000, momentum=True)
# midPoints = perceptron.enc_bulk(x_train)
#
outputs = perceptron.test_input(x_train)
outputs = np.array(outputs)
for i in range(len(outputs)):
    show_image_from_array(x_train[i], (15, 20, 3), f"item {i} real")
    show_image_from_array(outputs[i], (15, 20, 3), f"item {i} gen")


# plot_comparison_no_noise(np.array(outputs), x_train, epoch, learning_rate, (80, 60))