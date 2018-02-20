area=0
height=10
width=20

#calculating area of a triangle
area= height*width/2
#displaying with 2 dp
print("the area of the triangle is %.2f" % area)

#do the same thing with the .format syntax
print("the area of the triangle would be {0:f}", format(area))
print("my favorite number is {0:3d}", format(42))

#example with multiple numbers
print("Here are three numbers!" + \
    "The first is {0:d} The second is {1:4d} and the third is{2:d}".format(7,8,9))
