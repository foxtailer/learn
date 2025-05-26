from PIL import Image

im = Image.open("_.gif")
data = list(im.getdata())
width, height = im.size

data = [255 if i else 0 for i in data]

img = Image.new("L", (width, height))
img.putdata(data)
img.save("reconstructed.png")