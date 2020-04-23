from PIL import Image
def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    # TODO: Fill in decoding functionality
    # To get RGB values for an image at X, Y:
    # r, g, b = red_channel.getpixel((1, 1))
    decoded_image.save("decoded_image.png")
