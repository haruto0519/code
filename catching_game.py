#import
import turtle as t
import random as r

#screen
wn = t.Screen()
wn.setup(width=1.0, height=1.0)

#shapes
wn.addshape("acorn.gif")
wn.addshape("basket.gif")

#font
font_setup = ("Verdana", 50, "normal")

#level 

level = 1

#basket setup
basket = t.Turtle()
basket.penup()
basket_speed = 0
basket.speed(basket_speed)
basket.goto(0,-288)
basket_speed = 6
basket.speed(basket_speed)
basket.shape("basket.gif")

#acorn setup
acorn_cor_list = [-740, -640, -540, -440, -340, -240, -140, -40, 60, 160, 260, 360, 460, 560, 660, 730]
acorn_speed = 1
#background color
wn.bgpic("forest.gif")

#counter setting
score = 0
counter = t.Turtle()
counter.hideturtle()
counter.speed(0)
counter.pencolor("white")
counter.penup()
counter.goto(-500, 200)

#list 
acorn_list = []
for i in range(10):
  acorn_list.append(t.Turtle())

#game_over
'''def game_over():
  wn.bgpic(“game_over.gif”)'''

#moving function
def move_left():
  x = basket.xcor()
  x -= 40
  basket.setx(x)

def move_right():
  x = basket.xcor()
  x += 40
  basket.setx(x)

#keypresses

wn.onkeypress(move_left,"a")
wn.onkeypress(move_right, "d")

#function to draw acorns in random coordinate
def draw_acorns(index):
  acorn_list[index].hideturtle()
  random_acorn_cor = r.randint(0,15)
  random_cordinate = acorn_cor_list[random_acorn_cor]
  acorn_list[index].penup()
  acorn_list[index].speed(0)
  acorn_list[index].goto(random_cordinate,450)
  acorn_list[index].shape("acorn.gif")
  acorn_list[index].showturtle()
  acorn_list[index].speed(acorn_speed)
  acorn_list[index].setx(random_cordinate)
  acorn_list[index].goto(random_cordinate, -500)
  wn.tracer(True)
  wn.update()
  #closes the screen when the acorns reach the ground
  '''if acorn_list [index].ycor == -400:
    game_over()'''
	


def update_score():
  counter.clear()
  counter.write(score, font=font_setup)

update_score()


#function call
for i in range(10):
  draw_acorns(i)
  #if touches

"""
def catched():
  score == score + 1 
  if score % 15 = 0:
    level == level + 1
    acorn_speed == acorn_speed + 20
    basket_speed == basket_speed + 2
  update_score
"""



wn.listen()
wn.mainloop()

