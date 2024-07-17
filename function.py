# 1- Traingle area
ction
def traingle_area(base, height):
    area = 0.5 * base * height
    return area


the_area = traingle_area(3, 5)

print(the_area)

# 2- area for 2 shapes

def shape_area(base, height,shape = 'traingle'):
    if shape == 'traingle':
        area = 0.5 * base * height
    elif shape == 'rectangular':
        area = base * height
    else:
        print("wrong shape")
        area = None
    return area


the_area = shape_area(3, 5,'nothing')

print(the_area)



# 3- Print pattern

def print_shape(num):
    for i in range(num):
        s = '*'
        for j in range(i):
            s += '*'
        print (s)

number = int(input('Enter an integer number: '))
print_shape(number)