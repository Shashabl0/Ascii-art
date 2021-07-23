from PIL import Image,ImageDraw,ImageFont
import math
import os


chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
#chars = "#Wo- "[::-1]
charArray = list(chars)
charlen = len(charArray)
interval = charlen/256

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

def ascii_gen(filename,path,scalefac = 0.1):
    oneCharwidth = 10
    oneCharheigth = 18
    scalefactor = scalefac

    #text_file = open("static\out1.txt","w")
    im = Image.open(os.path.join(path+'/'+filename))
    fnt = ImageFont.truetype("C;||Windows\\Fonts\\lucon.ttf",15)
    width,height = im.size
    #print("width ",width," height ",height," ratio ",height/width)
    im = im.resize((int(scalefactor*width),int(scalefactor*height*(oneCharwidth/oneCharheigth))),Image.NEAREST)      # NEAREST :- Flag for Resize
    width,height = im.size
    pix = im.load()

    outImage = Image.new('RGB',(int(oneCharwidth*width),int(oneCharheigth*height)),color=(0,0,0))
    d = ImageDraw.Draw(outImage)

    #w,he = outImage.size
    #print("nwidth ",w," nheight ",h," ratio ",h/w)


    for i in range(height):
        for j in range(width):
            r,g,b = pix[j,i]
            h = int(r/3+g/3+b/3)
            pix[j,i] = (h,h,h)
            #text_file.write(getChar(h))
            d.text((j*oneCharwidth,i*oneCharheigth),getChar(h),font=fnt,fill=(r,g,b))
        #text_file.write("\n")


    #im.save("out1.png")
    outImage.save("static\outImage.png")