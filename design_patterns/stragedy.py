#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Play(object):

    def __init__(self, age, play_method=None):
        self.age = age
        self.play_method = play_method if play_method else default_play

    def myplay(self):
        if self.age < 10:
            print("小学生多读书不要打球")
        elif self.age > 70:
            print("老年人好好照顾身体")
        else:
            self.play_method(self.age)

def default_play(age):
    print("持球单打")

def step_back(age):
    if age == 29:
        print("登哥式后撒步投篮")
    else:
        print("Draw Faul 未遂")

def slam_dumk(age):
    if 20 < age < 30:
        print("大风车灌篮")
    else:
        print("滑到了！")

if __name__ == "__main__":
    p1 = Play(99)
    p1.myplay()
    p1 = Play(19)
    p1.myplay()

    p2 = Play(29, play_method=slam_dumk)
    p2.myplay()

    p3 = Play(29, play_method=step_back)
    p3.myplay()

    p4 = Play(39, play_method=step_back)
    p4.myplay()

    p5 = Play(39, play_method=step_back)
    p5.myplay()

    p6 = Play(1)
    p6.myplay()

    p7 = Play(39, play_method=slam_dumk)
    p7.myplay()
