import numpy as np
from PIL import Image
from skimage import morphology
import math

def grayscale(image):
    width, height = image.size
    grayscale_image = Image.new('L', (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            # Calculate grayscale value using average of RGB values
            gray = int((r + g + b) / 3)
            grayscale_image.putpixel((x, y), gray)

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

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel = gradient_image.getpixel((x, y))
            if pixel >= high_threshold:
                canny_image.putpixel((x, y), 255)
            elif low_threshold <= pixel < high_threshold:
                if any(gradient_image.getpixel((x + dx, y + dy)) >= high_threshold
                       for dx in range(-1, 2) for dy in range(-1, 2)):
                    canny_image.putpixel((x, y), 255)

    return canny_image


def laplacian_filter(image):
    width, height = image.size
    grayscale_image = image.convert('L')
    filtered_image = Image.new('L', (width, height))

    laplacian = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel = sum([grayscale_image.getpixel((x + dx, y + dy)) * laplacian[dy][dx]
                         for dx in range(-1, 2) for dy in range(-1, 2)])
            pixel = max(0, min(pixel, 255))
            filtered_image.putpixel((x, y), pixel)

    return filtered_image


def unsharp_masking(image, strength=2):
    blurred_image = averaging_blur(image)
    sharpened_image = Image.new('RGB', image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            br, bg, bb = blurred_image.getpixel((x, y))
            # Subtracting the blurred image from the original image
            sr = int(max(0, min(r + strength * (r - br), 255)))
            sg = int(max(0, min(g + strength * (g - bg), 255)))
            sb = int(max(0, min(b + strength * (b - bb), 255)))
            sharpened_image.putpixel((x, y), (sr, sg, sb))

    return sharpened_image


def histogram_equalization(image):
    grayscale_image = image.convert('L')
    width, height = grayscale_image.size
    histogram = [0] * 256

    # Calculate histogram
    for x in range(width):
        for y in range(height):
            pixel = grayscale_image.getpixel((x, y))
            histogram[pixel] += 1

    # Calculate cumulative distribution function (CDF)
    cdf = [sum(histogram[:i + 1]) for i in range(256)]

    # Scale CDF to the range [0, 255]
    cdf_min = min(cdf)
    cdf_max = max(cdf)
    scaled_cdf = [int((cdf[i] - cdf_min) * 255 / (cdf_max - cdf_min)) for i in range(256)]

    equalized_image = Image.new('L', (width, height))

    # Apply equalization to each pixel
    for x in range(width):
        for y in range(height):
            pixel = grayscale_image.getpixel((x, y))
            equalized_pixel = scaled_cdf[pixel]
            equalized_image.putpixel((x, y), equalized_pixel)

    return equalized_image


def thresholding(image, threshold=128):
    grayscale_image = image.convert('L')
    width, height = grayscale_image.size
    binary_image = Image.new('1', (width, height), 0)

    for x in range(width):
        for y in range(height):
            pixel = grayscale_image.getpixel((x, y))
            if pixel >= threshold:
                binary_image.putpixel((x, y), 1)

    return binary_image

def median_filter(image, size=3):
    width, height = image.size
    filtered_image = image.copy()

    for x in range(size // 2, width - size // 2):
        for y in range(size // 2, height - size // 2):
            pixels = [
                image.getpixel((x + dx, y + dy))
                for dx in range(-size // 2, size // 2 + 1)
                for dy in range(-size // 2, size // 2 + 1)
            ]
            median_pixel = sorted(pixels)[len(pixels) // 2]
            filtered_image.putpixel((x, y), median_pixel)

    return filtered_image

def brightness_adjustment(image, factor):
    width, height = image.size
    adjusted_image = image.copy()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = int(max(0, min(r + factor, 255)))
            g = int(max(0, min(g + factor, 255)))
            b = int(max(0, min(b + factor, 255)))
            adjusted_image.putpixel((x, y), (r, g, b))

    return adjusted_image

def contrast_adjustment(image, factor):
    width, height = image.size
    adjusted_image = image.copy()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = int(max(0, min((r - 128) * factor + 128, 255)))
            g = int(max(0, min((g - 128) * factor + 128, 255)))
            b = int(max(0, min((b - 128) * factor + 128, 255)))
            adjusted_image.putpixel((x, y), (r, g, b))

    return adjusted_image


def rotate_image(image, angle):
    width, height = image.size
    angle_rad = math.radians(angle)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)

    # Calculate new image size
    new_width = int(math.ceil(abs(width * cos_theta) + abs(height * sin_theta)))
    new_height = int(math.ceil(abs(width * sin_theta) + abs(height * cos_theta)))

    # Create a blank image with the new size
    rotated_image = Image.new('RGB', (new_width, new_height), (0, 0, 0))

    # Calculate the center point of the new image
    center_x = new_width // 2
    center_y = new_height // 2

    for x in range(new_width):
        for y in range(new_height):
            # Calculate the original coordinates of the pixel in the rotated image
            original_x = int((x - center_x) * cos_theta + (y - center_y) * sin_theta + width / 2)
            original_y = int(-(x - center_x) * sin_theta + (y - center_y) * cos_theta + height / 2)

            # Check if the original coordinates are within the bounds of the original image
            if 0 <= original_x < width and 0 <= original_y < height:
                # Get the pixel value from the original image and set it in the rotated image
                pixel = image.getpixel((original_x, original_y))
                rotated_image.putpixel((x, y), pixel)

    return rotated_image


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
    step_size = 255//num_colors

    # Create a blank output image
    output_image = Image.new('RGB', image.size)

    # Apply posterize filter
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image_rgb.getpixel((x, y))
            out_r = math.floor(r//step_size)*step_size + (step_size//2)
            out_g = math.floor(g//step_size)*step_size + (step_size//2)
            out_b = math.floor(b//step_size)*step_size + (step_size//2)
            output_image.putpixel((x, y), (int(out_r), int(out_g), int(out_b)))

    return output_image

def old_image(image):
    # Create a blank output image
    output_image = Image.new('RGB', image.size)
    
    # Apply old image filter
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            out_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            out_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            out_b = int(r * 0.272 + g * 0.534 + b * 0.131)
            output_image.putpixel((x, y), (out_r, out_g, out_b))
    
    return output_image


def vignetting(image):
    # Create a blank output image
    output_image = Image.new('RGB', image.size)
    
    # Calculate maximum distance from center
    max_distance = max(image.width // 2, image.height // 2)
    
    # Apply vignetting filter
    for x in range(image.width):
        for y in range(image.height):
            distance = ((x - image.width // 2) ** 2 + (y - image.height // 2) ** 2) ** 0.5
            factor = 1 - distance / max_distance
            pixel = image.getpixel((x, y))
            output_pixel = tuple(int(value * factor) for value in pixel)
            output_image.putpixel((x, y), output_pixel)
    
    return output_image


def photocopy(image, threshold=128):
    # Convert image to grayscale
    grayscale_image = image.convert('L')
    
    # Create a blank output image
    output_image = Image.new('L', image.size)
    
    # Apply photocopy filter
    for x in range(image.width):
        for y in range(image.height):
            pixel_value = grayscale_image.getpixel((x, y))
            if pixel_value > threshold:
                output_image.putpixel((x, y), 255)
            else:
                output_image.putpixel((x, y), pixel_value * (threshold - pixel_value) // threshold ** 2)
    
    return output_image

def night_vision(image):
    # Convert image to RGB mode
    image_rgb = image.convert('RGB')
    
    # Create a blank output image
    output_image = Image.new('RGB', image.size)
    
    # Apply night vision filter
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image_rgb.getpixel((x, y))
            out_r = g // 2
            out_b = 2 * out_r
            out_g = 2 * out_b
            output_image.putpixel((x, y), (out_r, out_g, out_b))
    
    return output_image

def mirror(image):
    # Create a blank output image
    output_image = Image.new('RGB', image.size)
    
    # Apply mirror filter
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            output_image.putpixel((image.width - x - 1, y), pixel)
    
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
