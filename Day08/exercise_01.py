import math

def paint_calc(height, width, cover):
    cans_of_paint = math.ceil((height * width)/cover)
    print(f"You'll need {cans_of_paint} cans of paint.")

test_h = int(input("The height of the wall: ")) 
test_w = int(input("The width of the wall: ")) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

