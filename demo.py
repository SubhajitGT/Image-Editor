from PIL import Image, ImageOps, ImageDraw, ImageFont

#Load Image
im1=Image.open(r"C:/Users/SUBHAJIT/Pictures/Screenshots/download.jpg")

im1.show()
#Image Info.
print(im1.format)
print(im1.mode)
print(im1.size)
print(im1.width)
print(im1.height)
print(im1.info)

#Save Image
im1.save("download1.png")
im1.save("C:/Users/SUBHAJIT/Pictures/Screenshots/download1.png")

#Flip Vertically
im2=ImageOps.flip(im1)
im2.show()

#Flip Horizonatlly
im3=ImageOps.mirror(im1)
im3.show()

#Flip image into gray scale
im4=ImageOps.grayscale(im1)
im4.show()

#Invert Image
im5=ImageOps.invert(im1)
im5.show()

#Rotate Image
im6=Image.open(r"C:/Users/SUBHAJIT/Videos/images.jpg")
im6=im6.rotate(60)
im6.show()

#Resize Image
im6=im6.resize((320,200))
im6.show()

#Text on Image
im7=Image.open(r"C:/Users/SUBHAJIT/Videos/cache.png")
d=ImageDraw.Draw(im7)
myFont=ImageFont.truetype('C:/Users/SUBHAJIT/Videos/OpenSans-Bold.ttf',140)
d.text((28,36),"It's cache!",font=myFont,fill=(255,255,0))
im7.show()

#Crop and paste
im8=Image.open(r"Pictures")