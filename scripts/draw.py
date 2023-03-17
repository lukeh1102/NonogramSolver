import turtle

TODO = """
    - make the grid size dynamic
    """
def draw_square(pen, size, start_x, start_y):
    pen.penup()
    pen.setpos(start_x, start_y)
    pen.pendown()
    for i in range(1,5):
        pen.forward(size)
        pen.right(90)

def draw_line(pen, length, start_x, start_y):
    pen.penup()
    pen.setpos(start_x, start_y)
    pen.pendown()
    pen.forward(length)

def draw_bg(pen, length, width):
    pen.speed(15)
    pen.color("black")
    pen.pensize(3)
    pen.penup()

    #draw frame and divide it into a 3x3 grid
    draw_square(pen, 602, -301, 301)

    # pen.setheading(0)
    # draw_line(pen,600,-300,100)
    # draw_line(pen,600,-300,-100)
    # pen.setheading(270)
    # draw_line(pen,600,100,300)
    # draw_line(pen,600,-100,300)

    
    pixel_length = 600/length
    pixel_width = 600/width

    #draw grid in frame where each square is 40x40
    #pen.speed(50)
    pen.color("#21a6b8")
    pen.pensize(1)
    pen.penup()

    for i in range(1,width):
        draw_line(pen,600,-300,300-(i*pixel_width))
    pen.setheading(270)
    for i in range(1,length):
        draw_line(pen,600,-300+(i*pixel_length),300)

    
    

def fill_square(pen, size, start_x, start_y, color="black"):
    pen.color(color)
    pen.penup()
    pen.setpos(start_x, start_y)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    for i in range(1,5):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def complete_image(pen, image, pallet):
    for i in range(0,len(image[0])):
        for j in range(0,len(image[0])):
            print("filling square at:", i, j, pallet[image[i][j]])
            fill_square(pen, 40, -300+(j*40), 300-(i*40), pallet[image[i][j]])
    fill_square(pen, 1, 800, 800, "white")
    print("done")

# # Testing the functions
# #create window
# window = turtle.Screen()
# window.screensize(800,800)

# #create pen
# pen = turtle.Turtle()

# #create a 15x15 2d list of alertnating 1's and 0's
# image = [[0 for i in range(15)] for j in range(15)]
# for i in range(0,15):
#     for j in range(0,15):
#         if (i+j)%2 == 0:
#             image[i][j] = 1
#         else:
#             image[i][j] = 0
# pallet = ["#21a6b8", "#21b871"]

# window.tracer(0,0)
# draw_bg(pen, 10, 7)
# window.tracer(1,1)
# #complete_image(pen, image, pallet)

# window.exitonclick()
# window.update()