def calculate_area(dimension1, dimension2, shape="triangle"):
    if shape == "triangle":
        area=(1/2)*base*height
        print(area)
    elif shape=="rectangle":
        area = dimension1 * dimension2
        print(area)
    else:
        print("not a triangle")
    return area
base=4
height=5
#without using third variable
triangle_area=calculate_area(base,height)
print("Without third parameter area of triangle is:",triangle_area)

#using triangle as 3rd vaariable
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is:",triangle_area)

length=2
width=5
#using rectangle as 3rd vaariable
rectangle_area=calculate_area(length,width,"rectangle")
print("Area of rectangle is:",rectangle_area)

def print_pattern(n=5):
    for i in range(n):
        s=''
        for j in range(i+1):
            s=s+'*'
        print(s)

print("Pattern with input 3")
print_pattern(3)

print("Pattern with input 4")
print_pattern(4)

print("Pattern with no input number")
print_pattern()