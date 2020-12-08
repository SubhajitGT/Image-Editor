from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageColor

#create image
image=Image.new("RGB",(512,512),ImageColor.getrgb("#ffffff"))

draw=ImageDraw.Draw(image)

#draw line
draw.line([(0,0),(100,100)],fill="red",width=5)

#draw rectangle
draw.rectangle((200,100,100,200),fill="green",outline=(0,0,0))

#draw circle
draw.ellipse((200,100,300,200),fill="purple",outline="blue")

#get image height and width
width,height =image.size

#loop for dots
for d in range(height):
    image.putpixel((d,d),(0,0,0,255))
    image.putpixel((d,-d),(0,0,0,255))

#display image
image.show()