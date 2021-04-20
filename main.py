from PIL import Image

raw_image = 'Monro.jpg'
image = Image.open(raw_image)

red, green, blue = image.split()

pixels = 100

coordinates_to_crop_left = (pixels, 0, image.width, image.height)
coordinates_to_crop_borders_on_widht = (pixels/2, 0, image.width - pixels/2, image.height)
coordinates_to_crop_rignt = (0, 0, image.width - pixels, image.height)

left_cropped_red = red.crop(coordinates_to_crop_left) 
cropped_borders_red = red.crop(coordinates_to_crop_borders_on_widht) 
left_blended_red = Image.blend(left_cropped_red, cropped_borders_red, 0.5) 

cropped_borders_green = green.crop(coordinates_to_crop_borders_on_widht)

right_cropped_blue = blue.crop(coordinates_to_crop_rignt)
cropped_borders_blue = blue.crop(coordinates_to_crop_borders_on_widht) 
right_blended_blue = Image.blend(right_cropped_blue, cropped_borders_blue, 0.5) 
avatar = Image.merge('RGB', (left_blended_red, cropped_borders_green, right_blended_blue))
avatar.thumbnail((80,80)) 
avatar.save('avatar.jpg')