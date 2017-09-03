#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('purple')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(1)
	for i in range(1,10):
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.left(90)
		bran.back(20)
		bran.left(90)
		bran.forward(40)

if __name__ == '__main__':
  main()