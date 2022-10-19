import turtle as t
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 42)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228),
 (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50),
 (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36),
 (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8),
 (89, 48, 31), (39, 46, 81), (26, 97, 94)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def dots_row():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


tim.hideturtle()
y_cor = -200
for i in range(10):
    tim.penup()
    tim.goto(-250, y_cor)
    y_cor += 50
    dots_row()


screen = t.Screen()
screen.exitonclick()






