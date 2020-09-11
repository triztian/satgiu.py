import io
from PIL import Image
from PIL.ExifTags import TAGS

def reduce_to_size(image: Image, size_in_bytes: int) -> Image:
    """
    Reduces the image down to the specified size in bytes
    """
    mem_image = io.BytesIO()

    while mem_image.getbuffer().nbytes > size_in_bytes:
        # Will reduce quality by 5% each round
        image.save(mem_image, format="jpg", quality=95) 

    return Image.open(mem_image)


def set_faux_dpi(image: Image, dpi: int) -> Image:
    """
    Sets the image's DPI Exif metadata without actually changing the image
    """
    print_exif(image)
    image._getexif()
    

def print_exif(image: Image) -> None:
    for (k, v) in image._getexif().items():
            print('%s = %s' % (TAGS.get(k), v))