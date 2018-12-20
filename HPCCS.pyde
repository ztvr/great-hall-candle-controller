"""

Harry Potter Candle Control Simulator

Copyright 2018 - Zak Van Reesen

"""

from candle import Candle

greatHallCandles = []

def setup():
    size(800, 600)
    for i in range(10):
        greatHallCandles.append(Candle(i*width/10,int(random(0,height-50)),round(random(0,1)),random(-1,1),0))
    
def draw():
    background(0)
    for i in range(10):
        greatHallCandles[i].display()
        greatHallCandles[i].flicker()
    greatHallCandles[int(random(0,10))].accelerate(random(-1,1))
