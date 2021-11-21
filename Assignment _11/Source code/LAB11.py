########################################################################
##
## CS 101 Lab
## Program # 11
## Name:Austin Souphanh
## Email: ajs2dz@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import time

class Clock:
    def __init__(self, hour, minute, second, clock_type=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 25:
                    self.hour = 0

    def __str__(self):
        if self.clock_type == 0:
            return "{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second)
        else:
            if self.hour <= 11:
                if self.hour == 0:
                    return "{:02}:{:02}:{:02} am".format(12, self.minute, self.second)
                else:
                    return "{:02}:{:02}:{:02} am".format(self.hour, self.minute, self.second)
            else:
                return "{:02}:{:02}:{:02} pm".format(self.hour - 12, self.minute, self.second)


hour = int(input("What is the current hour ==> "))
minute = int(input("What is the current minute ==> "))
second = int(input("What is the current second ==> "))
clock = Clock(hour, minute, second, clock_type=1)
while True:
    print(clock)
    clock.tick()
    time.sleep(1)
