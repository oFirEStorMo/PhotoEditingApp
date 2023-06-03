import numpy as np
from PIL import Image
from skimage import morphology
import math

def grayscale(image):
    img_array = np.array(image)
    if img_array.ndim == 3:
        gray_array = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        grayscale_image = Image.fromarray(gray_array, mode='L')
    else:
        grayscale_image = image.convert('L')

    return grayscale_image


def averaging_blur(image, size=3):
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    blurred_image = image.copy()

    if image.mode == 'RGB':
        img_array = np.array(image)
        blurred_array = np.zeros_like(img_array, dtype=np.uint8)

        for c in range(3):
            blurred_array[:, :, c] = np.round(
                np.convolve(img_array[:, :, c].astype(np.float64).flatten(), kernel.flatten(), mode='same')
            ).reshape(img_array[:, :, c].shape)

        blurred_image = Image.fromarray(blurred_array)
    else:
        img_array = np.array(image.convert('L'))
        blurred_array = np.round(np.convolve(img_array.astype(np.float64).flatten(), kernel.flatten(), mode='same')).reshape(img_array.shape)
        blurred_image = Image.fromarray(blurred_array.astype(np.uint8), mode='L')

    return blurred_image




def sobel_operator(image):
    width, height = image.size
    grayscale_image = image.convert('L')
    gradient_image = Image.new('L', (width, height))

    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel_x = sum([grayscale_image.getpixel((x + dx, y + dy)) * sobel_x[dy][dx]
                          for dx in range(-1, 2) for dy in range(-1, 2)])
            pixel_y = sum([grayscale_image.getpixel((x + dx, y + dy)) * sobel_y[dy][dx]
                          for dx in range(-1, 2) for dy in range(-1, 2)])
            gradient = int((pixel_x ** 2 + pixel_y ** 2) ** 0.5)
            gradient_image.putpixel((x, y), gradient)

    return gradient_image


def canny_edge_detection(image, low_threshold=20, high_threshold=50):
    width, height = image.size
    grayscale_image = image.convert('L')
    gradient_image = sobel_operator(grayscale_image)
    canny_image = Image.new('L', (width, height), 0)

    # Convert gradient_image to NumPy array
    gradient_array = np.array(gradient_image, dtype=np.float32)

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel = gradient_array[y, x]
            if pixel >= high_threshold:
                canny_image.putpixel((x, y), 255)
            elif low_threshold <= pixel < high_threshold:
                if np.any(gradient_array[y-1:y+2, x-1:x+2] >= high_threshold):
                    canny_image.putpixel((x, y), 255)

    return canny_image

def laplacian_filter(image):
    width, height = image.size
    grayscale_image = image.convert('L')
    filtered_image = Image.new('L', (width, height))

    laplacian = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Convert grayscale_image to NumPy array
    grayscale_array = np.array(grayscale_image, dtype=np.float32)

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel = np.sum(grayscale_array[y-1:y+2, x-1:x+2] * laplacian)
            pixel = max(0, min(pixel, 255))
            filtered_image.putpixel((x, y), int(pixel))

    return filtered_image


def unsharp_masking(image, strength=2):
    blurred_image = averaging_blur(image)
    sharpened_image = Image.new('RGB', image.size)

    # Convert images to NumPy arrays
    image_array = np.array(image, dtype=np.float32)
    blurred_array = np.array(blurred_image, dtype=np.float32)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image_array[y, x]
            br, bg, bb = blurred_array[y, x]
            # Subtracting the blurred image from the original image
            sr = int(max(0, min(r + strength * (r - br), 255)))
            sg = int(max(0, min(g + strength * (g - bg), 255)))
            sb = int(max(0, min(b + strength * (b - bb), 255)))
            sharpened_image.putpixel((x, y), (sr, sg, sb))

    return sharpened_image


def histogram_equalization(image):
    grayscale_image = image.convert('L')
    width, height = grayscale_image.size
    histogram = np.zeros(256, dtype=np.int32)

    # Calculate histogram
    pixels = np.array(grayscale_image).flatten()
    for pixel in pixels:
        histogram[pixel] += 1

    # Calculate cumulative distribution function (CDF)
    cdf = np.cumsum(histogram)

    # Scale CDF to the range [0, 255]
    cdf_min = np.min(cdf)
    cdf_max = np.max(cdf)
    scaled_cdf = ((cdf - cdf_min) * 255 / (cdf_max - cdf_min)).astype(np.uint8)

    equalized_image = Image.new('L', (width, height))

    # Apply equalization to each pixel
    pixels = np.array(grayscale_image)
    equalized_pixels = scaled_cdf[pixels]
    equalized_image.putdata(equalized_pixels.flatten())

    return equalized_image


def thresholding(image, threshold=128):
    grayscale_image = image.convert('L')
    width, height = grayscale_image.size
    binary_pixels = np.zeros((height, width), dtype=np.uint8)

    pixels = np.array(grayscale_image)

    # Apply thresholding
    binary_pixels[pixels >= threshold] = 1

    binary_image = Image.fromarray(binary_pixels, mode='1')
    return binary_image

def median_filter(image, size=3):
    width, height = image.size
    filtered_image = image.copy()

    if image.mode == 'RGB':
        for x in range(size // 2, width - size // 2):
            for y in range(size // 2, height - size // 2):
                window = [
                    image.getpixel((x + dx, y + dy))
                    for dx in range(-size // 2, size // 2 + 1)
                    for dy in range(-size // 2, size // 2 + 1)
                ]
                median_pixel = np.median(window, axis=0)
                filtered_image.putpixel((x, y), tuple(median_pixel.astype(int)))
    else:
        for x in range(size // 2, width - size // 2):
            for y in range(size // 2, height - size // 2):
                window = [
                    image.getpixel((x + dx, y + dy))
                    for dx in range(-size // 2, size // 2 + 1)
                    for dy in range(-size // 2, size // 2 + 1)
                ]
                median_pixel = np.median(window)
                filtered_image.putpixel((x, y), int(median_pixel))

    return filtered_image

def brightness_adjustment(image, factor):
    width, height = image.size
    adjusted_image = image.copy()

    if image.mode == 'RGB':
        pixel_array = np.array(image)
        pixel_array = pixel_array.astype(np.float32)
        pixel_array += factor
        pixel_array = np.clip(pixel_array, 0, 255)
        pixel_array = pixel_array.astype(np.uint8)
        adjusted_image = Image.fromarray(pixel_array, mode='RGB')
    else:
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                adjusted_pixel = int(max(0, min(pixel + factor, 255)))
                adjusted_image.putpixel((x, y), adjusted_pixel)

    return adjusted_image

def contrast_adjustment(image, factor):
    width, height = image.size
    adjusted_image = image.copy()

    if image.mode == 'RGB':
        pixel_array = np.array(image)
        pixel_array = pixel_array.astype(np.float32)
        pixel_array -= 128  # Shift pixel values by 128
        pixel_array *= factor
        pixel_array += 128
        pixel_array = np.clip(pixel_array, 0, 255)
        pixel_array = pixel_array.astype(np.uint8)
        adjusted_image = Image.fromarray(pixel_array, mode='RGB')
    else:
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                adjusted_pixel = int(max(0, min((pixel - 128) * factor + 128, 255)))
                adjusted_image.putpixel((x, y), adjusted_pixel)

    return adjusted_image


def rotate_image(image, angle):
    # Rotate the image
    rotated_image = image.rotate(int(angle), expand=True)
    
    return rotated_image

# def rotate_image(image, angle):
#     width, height = image.size
#     angle_rad = math.radians(int(angle))
#     cos_theta = math.cos(angle_rad)
#     sin_theta = math.sin(angle_rad)

#     # Create a grid of coordinates for the new image
#     new_coords_x, new_coords_y = np.meshgrid(range(width), range(height))
#     new_coords_x -= width // 2
#     new_coords_y -= height // 2

#     # Apply the rotation transformation to the coordinates
#     original_coords_x = np.round(new_coords_x * cos_theta + new_coords_y * sin_theta + width // 2).astype(int)
#     original_coords_y = np.round(-new_coords_x * sin_theta + new_coords_y * cos_theta + height // 2).astype(int)

#     # Mask to ensure only valid coordinates are used
#     valid_mask = (original_coords_x >= 0) & (original_coords_x < width) & (original_coords_y >= 0) & (original_coords_y < height)

#     # Get the pixel values from the original image using the transformed coordinates
#     original_pixels = np.array(image)
#     rotated_pixels = np.zeros_like(original_pixels)
#     rotated_pixels[new_coords_y[valid_mask], new_coords_x[valid_mask]] = original_pixels[original_coords_y[valid_mask], original_coords_x[valid_mask]]

#     # Create a new PIL image from the rotated pixel values
#     rotated_image = Image.fromarray(rotated_pixels, mode='RGB')

#     return rotated_image


def open_operation(image, size=3):
    # Convert PIL image to binary numpy array
    binary_image = np.array(image.convert('L')) > 128

    # Perform opening operation
    opened_image = morphology.opening(binary_image, morphology.square(size))

    # Convert binary numpy array back to PIL image
    opened_pil_image = Image.fromarray(opened_image.astype('uint8') * 255, mode='L')

    return opened_pil_image


def close_operation(image, size=3):
    # Convert PIL image to binary numpy array
    binary_image = np.array(image.convert('L')) > 128

    # Perform closing operation
    closed_image = morphology.closing(binary_image, morphology.square(size))

    # Convert binary numpy array back to PIL image
    closed_pil_image = Image.fromarray(closed_image.astype('uint8') * 255, mode='L')

    return closed_pil_image


def posterize(image, num_colors):
    # Convert image to RGB mode
    image_rgb = image.convert('RGB')

    # Calculate the step size between each quantized color level
    step_size = 255 // int(num_colors)

    # Create a numpy array from the image
    pixels = np.array(image_rgb)

    # Apply posterize filter using numpy operations
    out_pixels = np.floor(pixels // step_size) * step_size + (step_size // 2)

    # Create a new PIL image from the output pixel values
    output_image = Image.fromarray(out_pixels.astype('uint8'), mode='RGB')

    return output_image


def old_image(image):
    # Convert image to RGB mode
    image_rgb = image.convert('RGB')

    # Create a numpy array from the image
    pixels = np.array(image_rgb)

    # Apply old image filter using numpy operations
    out_pixels = np.zeros_like(pixels)
    out_pixels[:, :, 0] = np.clip(pixels[:, :, 0] * 0.393 + pixels[:, :, 1] * 0.769 + pixels[:, :, 2] * 0.189, 0, 255)
    out_pixels[:, :, 1] = np.clip(pixels[:, :, 0] * 0.349 + pixels[:, :, 1] * 0.686 + pixels[:, :, 2] * 0.168, 0, 255)
    out_pixels[:, :, 2] = np.clip(pixels[:, :, 0] * 0.272 + pixels[:, :, 1] * 0.534 + pixels[:, :, 2] * 0.131, 0, 255)

    # Create a new PIL image from the output pixel values
    output_image = Image.fromarray(out_pixels.astype('uint8'), mode='RGB')

    return output_image

def vignetting(image):
    # Convert image to RGB mode
    image_rgb = image.convert('RGB')

    # Create a numpy array from the image
    pixels = np.array(image_rgb)

    # Create meshgrid of coordinates
    x_coords, y_coords = np.meshgrid(np.arange(image.width), np.arange(image.height))

    # Calculate maximum distance from center
    max_distance = max(image.width // 2, image.height // 2)

    # Calculate distance from center for each pixel
    distance = np.sqrt((x_coords - image.width // 2) ** 2 + (y_coords - image.height // 2) ** 2)

    # Calculate factor for each pixel
    factor = 1 - distance / max_distance

    # Apply vignetting filter using numpy operations
    out_pixels = np.multiply(pixels, factor[..., np.newaxis])
    out_pixels = np.clip(out_pixels, 0, 255)

    # Create a new PIL image from the output pixel values
    output_image = Image.fromarray(out_pixels.astype('uint8'), mode='RGB')

    return output_image


def photocopy(image, threshold=128):
    # Convert image to grayscale
    grayscale_image = image.convert('L')

    # Create a numpy array from the grayscale image
    pixels = np.array(grayscale_image)

    # Create a blank output image as a numpy array
    output_pixels = np.zeros_like(pixels)

    # Apply photocopy filter using numpy operations
    mask = pixels > threshold
    output_pixels[mask] = 255
    output_pixels[~mask] = pixels[~mask] * (threshold - pixels[~mask]) // threshold ** 2

    # Create a new PIL image from the output pixel values
    output_image = Image.fromarray(output_pixels, mode='L')

    return output_image

def night_vision(image):
    # Convert image to RGB mode
    image_rgb = image.convert('RGB')

    # Create a numpy array from the RGB image
    pixels = np.array(image_rgb)

    # Create a blank output image as a numpy array
    output_pixels = np.zeros_like(pixels)

    # Apply night vision filter using numpy operations
    output_pixels[:, :, 0] = pixels[:, :, 1] // 2
    output_pixels[:, :, 2] = 2 * output_pixels[:, :, 0]
    output_pixels[:, :, 1] = 2 * output_pixels[:, :, 2]

    # Create a new PIL image from the output pixel values
    output_image = Image.fromarray(output_pixels)

    return output_image

def mirror(image):
    # Create a numpy array from the image
    pixels = np.array(image)

    # Create a blank output image as a numpy array
    output_pixels = np.zeros_like(pixels)

    # Apply mirror filter using array slicing
    output_pixels[:, :] = pixels[:, ::-1]

    # Create a new PIL image from the output pixel values
    output_image = Image.fromarray(output_pixels)

    return output_image




# Usage example:
# image = Image.open('mirror_in.jpg')

# # Apply grayscale filter
# grayscale_image = grayscale(image)
# grayscale_image.show()

# # Apply Gaussian blur filter
# blurred_image = sobel_operator(image)
# blurred_image.show()

# # Apply Sobel operator
# gradient_image = sobel_operator(image)
# gradient_image.show()

# # Apply Canny edge detection
# canny_image = canny_edge_detection(image)
# canny_image.show()

# # Apply Laplacian filter
# filtered_image = laplacian_filter(image)
# filtered_image.show()

# # Apply unsharp masking
# sharpened_image = unsharp_masking(image)
# sharpened_image.show()

# # Apply histogram equalization
# equalized_image = histogram_equalization(image)
# equalized_image.show()

# # Apply thresholding
# binary_image = thresholding(image)
# binary_image.show()
