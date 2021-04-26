from PIL import Image, ImageDraw, ImageFont
import random

#palette taken from: https://lospec.com/palette-list/funkyfuture-8
FUNKYFUTURE_x8 = ["#2b0f54","#ab1f65","#ff4f69","#fff7f8","#ff8142","#ffda45","#3368dc","#49e7ec"]


def generatePixelImage(pallete,imageWidth, imageHeight,fileName):

    colors, size = pallete
    images = [Image.new( "RGB",(1,1), color = colors[random.randint(0,len(colors)-1)] ) for amount in range(size * size)]
    pixelImage = Image.new("RGB",(size * imageWidth,size * imageHeight))
    
    if imageHeight == imageWidth:
        fillSquareImage(pixelImage,images,imageWidth, imageHeight).save(fileName,quality = 100)

def fillSquareImage(pixelImage,images,resizeRateWidth, resizeRateHeight):
    row = 0
    while row < pixelImage.height:
        column = 0

        while column < pixelImage.width:

            current_color = images.pop(0)
            countR = row  + resizeRateHeight - 1

            while countR >= row:
                countC = column + resizeRateWidth - 1

                while countC >= column:
                    pixelImage.paste(current_color,(countR,countC)) 
                    countC -= 1

                countR -= 1
            column += resizeRateWidth
        row += resizeRateHeight
    return pixelImage


generatePixelImage(FUNKYFUTURE_x8,50,50,"funkyFuture.png")

