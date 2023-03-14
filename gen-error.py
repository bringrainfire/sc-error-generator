#import libs
from PIL import Image, ImageFont, ImageDraw

#open Image File
my_image = Image.open("image.png")

#Set Fonts
font_size = 16
main_font = ImageFont.truetype('Fonts/Orbitron/Orbitron-VariableFont_wght.ttf', font_size)

#Error Text to render
MainMessage =  "Offline until 4.0 release"
ErrorCode = "0"
Description = ""

#Draw Image
image_editable = ImageDraw.Draw(my_image)

#Render Text Onto Image
image_editable.text((50,75), "Error: " + MainMessage + " (Code: " + ErrorCode + " ) ", (255,255,255), font=main_font)

#image settings
image_name = "nameOfImage"
newsize = (1640, 578)
im1 = my_image.resize(newsize)

#Uncomment line below to preview result
im1.show()



#Uncomment Line Below to Save Result
#im1.save("errorPics/" + image_name + ".png")
