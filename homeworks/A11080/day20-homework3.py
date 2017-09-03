#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author:lina 20170902
#面向对象

class car():
	def __init__(self,brand,speed):
		self.brand = brand
		self.speed = speed

	def drive(self,distance):
		time = float(distance)/self.speed
		print "驾驶 %s 时长 %0.1f 小时 路程 %d 时速 %0.1f" %(self.brand,time,distance,self.speed)

def main():
	car1 = car('捷达',100)
	car1.drive(300)

	car2 = car('奔驰',150)
	car2.drive(300)

if __name__ == '__main__':
	main()


