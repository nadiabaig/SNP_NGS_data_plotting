###this script is helpful in merging various plots into 1 png image..
import sys
from PIL import Image

images = [Image.open(x) for x in ['/home/baign/Desktop/tt/06_04_Trait_16_Manhatton_plot.jpg', '/home/baign/Desktop/tt/06_04_Trait_18_Manhatton_plot.jpg','/home/baign/Desktop/tt/06_Potato_neis_population_dist_ploidy.jpg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test4.jpg')     
