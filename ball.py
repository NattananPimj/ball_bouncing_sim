import turtle


#
# def draw_ball(color, size, x, y):
#     # draw a circle of radius equals to size at x, y coordinates and paint it with color
#     turtle.penup()
#     turtle.color(color)
#     turtle.fillcolor(color)
#     turtle.goto(x, y - size)  # some fixes
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(size)
#     turtle.end_fill()
#
#
# def move_ball(i, xpos, ypos, vx, vy, dt):
#     # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
#     xpos[i] += vx[i] * dt
#     ypos[i] += vy[i] * dt
#
#
# def update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
#     # if the ball hits the side walls, reverse the vx velocity
#     if abs(xpos[i]) > (canvas_width - ball_radius):
#         vx[i] = -vx[i]
#
#     # if the ball hits the ceiling or the floor, reverse the vy velocity
#     if abs(ypos[i]) > (canvas_height - ball_radius):
#         vy[i] = -vy[i]


# oop
class Ball:
    def __init__(self, color, radius, x, y, vx, vy, canvas_h, canvas_w):
        self.xpos = x
        self.ypos = y
        self.size = radius
        self.color = color
        self.vx = vx
        self.vy = vy
        self.canvas_h = canvas_h
        self.canvas_w = canvas_w

    def draw_ball(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.xpos, self.ypos - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self, dt):
        self.xpos += self.vx*dt
        self.ypos += self.vy*dt

    def update(self):
        # if hit wall
        if abs(self.xpos) > (self.canvas_w - self.size):
            self.vx = -self.vx
        if abs(self.ypos) > (self.canvas_h - self.size):
            self.vy = -self.vy
        # if hit other ball
