#write a code to convert jpeg to pdf

from PIL import Image

# Open the image file
image = Image.open('image.jpeg')

# Save the image as a PDF file
image.save('image.pdf')

print('Image converted to PDF successfully!')

