#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: jiaguwen


def main():
	who = 'Lina的妈妈'
	good_price = 5
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 6
	buy_amount = 2

	print '%s上街看到了%s，卖 %d 元/斤 ' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去 '

# run function
if __name__ == '__main__':
  main()

# 1. what's the meaning of 'number', 'string', 'boolean' in python?
#    number表示数字，string表示字符串，boolean表示二进制
# 2. try to describe the meaning of 'if' statement in your mind?
#    if语句表示判断，根据所描述的情况是否满足条件，选择要执行的命令
# 3. Why we need > < == >= <= ...etc...?
#    因为有一些数值需要比较大小，然后进行选择执行