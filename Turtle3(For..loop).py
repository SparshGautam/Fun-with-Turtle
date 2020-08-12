  
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
  
for count in range(2):    #for loop is basically use to detect its range here you can specify any range i have range = 2
   square()               #so here i specified that build a square 2 times
