from PIL import Image
import urllib.request

class ImageProcessing:
    #Code below obtained from:https://levelup.gitconnected.com/how-to-convert-an-image-to-ascii-art-with-python-in-5-steps-efbac8996d5e
    #It's a cool little feature I thought would be cool to print out the images to .txt file, 
    # you could also  re-factor this code to just simply download the images.
    # This code below is a set of methods that accepts a url to an image, and downloads the image and outputs it visually in a .txt file
    # Methods download_image_as_txt(), convert_to_ascii_art(), convert_pixel_to_character(), and save_as_text()
    
    # It's running into errors getting the image from Marie Curie, but it's more like a neet trick instead of an actual feature


    def download_image_as_txt(self,url_to_image, scientist_name):
        urllib.request.urlretrieve(url_to_image,"temp_download.png")
        img = Image.open("temp_download.png")
        ascii_art = self.convert_to_ascii_art(img)
        self.save_as_text(ascii_art, scientist_name)

    def convert_to_ascii_art(self,image):
        ascii_art = []
        ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
        (width, height) = image.size
        for y in range(0, height - 1):
            line = ''
            for x in range(0, width - 1):
                px = image.getpixel((x, y))
                line += self.convert_pixel_to_character(px,ascii_characters_by_surface)
            ascii_art.append(line)
        return ascii_art

    def convert_pixel_to_character(self,pixel,ascii_characters_by_surface):
        (r, g, b) = pixel
        pixel_brightness = r + g + b
        max_brightness = 255 * 3
        brightness_weight = len(ascii_characters_by_surface) / max_brightness
        index = int(pixel_brightness * brightness_weight) - 1
        return ascii_characters_by_surface[index]

    def save_as_text(self, ascii_art,name):
        with open("data/"+name, "w") as file:
            for line in ascii_art:
                file.write(line)
                file.write('\n')
        file.close()