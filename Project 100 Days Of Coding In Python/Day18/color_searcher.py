import colorgram

colors = colorgram.extract('damien_hirst_opium.webp', 91)

def add_colors(list_of_colors):
    for each_color in colors:
        r = each_color.rgb.r
        g = each_color.rgb.g
        b = each_color.rgb.b
        colors_tuple = (r, g, b)
        list_of_colors.append(colors_tuple)

colors_list = []
add_colors(colors_list)
del colors_list[:2]