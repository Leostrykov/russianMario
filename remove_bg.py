from rembg import remove
from PIL import Image

input_path = 'img/shegol.jpg'
output_path = 'shegol.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)