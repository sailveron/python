#Authors:
#SailVeron
#RedstonedLife
import turtle
from Config import tal as t
from Config import liel as l
t.speed(0)

def Liel():
  def right(): 
    l.seth(0)
    l.forward(100)
  def left():
    l.seth(180)
    l.forward(100)
  def up():
    l.seth(90)
    l.forward(100)
  def down():
    l.seth(270)
    l.forward(100)
  
def Tal():
   def right(): 
    t.seth(0)
    t.forward(100)
  def left():
    t.seth(180)
    t.forward(100)
  def up():
    t.seth(90)
    t.forward(100)
  def down():
    t.seth(270)
    t.forward(100)

