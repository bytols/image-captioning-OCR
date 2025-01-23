from PIL import Image

img_file = "page_01.jpg"

img = Image.open(img_file)
print(img)
print(img.size)
img = img.rotate(180)
img.show()
img.save("page_01_rotate.jpg")