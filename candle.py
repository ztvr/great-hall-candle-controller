class Candle(object):
    
    def __init__(self, xpos, zpos, lit, spd, acc):
        self.x = xpos  # x-coordinate -- for display of multiple candles
        self.y = zpos  # y-coordinate -- simulates height in room (z position)
        self.lit = lit  # Candle lighting state
        self.speed = spd  # Candle movement speed
        self.acceleration = acc  # Candle acceleration rate
        
    def light(self):
        self.lit = True
        
    def snuff(self):
        self.lit = False
        
    def flicker(self):
        self.lit = round(random(.47, 1))
        
    def accelerate(self, rate):
        self.acceleration = rate
        
    def stopMoving(self):
        self.speed = 0
        self.acceleration = 0
        
    def reverseDirection(self):
        self.speed = -self.speed
        self.acceleration = 0
        
    def display(self):
        # Update Lighting Fill
        if self.lit == True:
          noStroke()
          fill(249, 172, 66)
        else:
          noFill()
          stroke(247, 151, 21)
          
        #Update Speed Based on Acceleration
        self.speed = self.speed + self.acceleration
        if self.speed >= 20:
            self.acceleration = -2
        if self.speed <= -20:
            self.acceleration = 2
        
        # Update Position Based on Speed
        self.y = self.y + self.speed
        
        # Keep In Bounds
        if self.y <= 0:
            self.y = 0
            self.reverseDirection()
        if self.y >= height-50:
            self.y = height-50
            self.reverseDirection()
        
        # Draw
        rect(self.x,height-self.y-50,10,50)
