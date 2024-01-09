import magic
from PIL import Image


class File:
    def image_resize(self, file_id, filename, pixel):
        file = magic.from_file(filename, mime=True)
        if file != 'image/png' and file != 'image/jpeg':
            return False

        if pixel != 720 and pixel != 1080:
            return False

        pixels = {
            720: (1280, 720),
            1080: (1920, 1080),
        }

        if file == 'image/png':
            image = Image.open(filename)
            new_image = image.resize(pixels[pixels])
            new_image.save(f'media/files/{file_id}_photo_{pixel}.png')
            return f'files/{file_id}_photo_{pixel}.png'

        image = Image.open(filename)

        new_image = image.resize(pixels[pixel])
        new_image.save(f'media/files/{file_id}_photo_{pixel}.jpg')
        return f'files/{file_id}_photo_{pixel}.jpg'
