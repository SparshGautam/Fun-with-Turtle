import turtle             #first we have to import turtle to our python
sparsh = turtle.Turtle()  #here we have assigned sparsh variable to turtle 
                          #so we dont have to type turtle again we can use sparsh you may can type anything
def square():             #here we have specified that are further code are under a function called square
  sparsh.forward(100)     #here we have moved our turtle to forward by 100 positions
  sparsh.right(90)        #here we are aiming to change the position of turtle to right by 90 degrees
  sparsh.forward(100)
  sparsh.right(90)
  sparsh.forward(100)
  sparsh.right(90)
  sparsh.forward(100)
  
square()                #here we called are function we dont need to type tha code again
sparsh.forward(100)     #now with this the turtle will moe 200 positions upside
square()                #after moving it will made an another square
