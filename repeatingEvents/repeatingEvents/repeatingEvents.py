import turtle
nbrsides=5
for wierdname in range(nbrsides):
    turtle.forward(100)
    turtle.right(360/nbrsides)
    turtle.color("red")
    #for steps in range(nbrsides):
    #    turtle.foward(50)
    #    turtle.right(360/nbrsides)
#specifying numbers to count from
for steps in range(1,4):
    print(steps)

#specifying steps 
for thesteps in range(1,10,2):
    print(thesteps)

for rasteps in (1,2,3,4,5):
    print(rasteps)

    #using colors
for colours in("red","blue","green","purple"):
    turtle.color(colours)
    turtle.forward(100)
    turtle.left(90)