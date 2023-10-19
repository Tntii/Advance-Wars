import csv

from PIL import Image

def map_convert(file):
    model = Image.open(file)
    result = Image.new(model.mode, model.size)
    result_array = []

    color = ((0, 0, 0), (43, 51, 95), (126, 32, 114),
             (25, 149, 156), (139, 72, 82), (57, 92, 152),
             (169, 193, 255), (238, 238, 238), (212, 24, 108),
             (211, 132, 65), (233, 195, 91), (112, 198, 169),
             (118, 150, 222), (163, 163, 163), (255, 151, 152), (237, 199, 176))

    for y in range(model.height):
        result_array_x = []
        for x in range(model.width):
            moy_min = (500, 0)
            current_color = tuple(model.getpixel((x, y)))

            try:
                color_max = max(current_color[0], current_color[1], current_color[2])
                index = current_color.index(color_max)
                for i in range(len(color)-1, 0, -1):
                    moy_1 = abs((color[i][0] - model.getpixel((x, y))[0] + color[i][1] - model.getpixel((x, y))[1] + color[i][2] - model.getpixel((x, y))[2])/3)
                    moy_2 = abs(color_max - color[i][index])
                    moy = moy_1 + moy_2

                    if moy < moy_min[0]:
                        moy_min = (moy, i)
                result.putpixel((x, y), color[moy_min[1]])
                result_array_x.append(moy_min[1])

            except:
                result.putpixel((x, y), (0, 0, 0, 0))
                result_array_x.append(0)
        result_array.append(tuple(result_array_x))
    result.show()
    return model.size, tuple(result_array)


def remove_border(file):
    model = Image.open(file)
    print(model.mode)
    result = Image.new(model.mode, model.size)
    hauteur = 0
    largeur = 0
    x2 = 0
    y2 = 0
    put_pixel = False

#parcour l'image
    for y in range(model.height):
        if put_pixel:
            put_pixel = False
            y2 += 1
            x2 = 0
        for x in range(model.width):
            color = model.getpixel((x, y))
            if color != (255, 255, 255, 255) and color != (109, 109, 145, 255) and color != (224, 224, 224, 255) and color != (252, 252, 255, 255):
                result.putpixel((x2, y2), color)
                x2+=1
                put_pixel = True
    print(model.getpixel((-1, -1)))

    result.show()
    result.save("../texture/tile2.png")

map_convert("../map/test.png")
