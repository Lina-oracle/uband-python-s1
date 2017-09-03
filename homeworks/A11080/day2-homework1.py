#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Lina

def main():
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price

	print 'pie cost %d ' % (pie_total_price)
	print 'pie cost %g ' % (pie_total_price)
	print 'pie cost %0.2f ' % (pie_total_price)

	# %d表示输出整数，%g表示输出小数格式，%0.2f表示小数点后保留两位

	number = 2 ** 3
	print 'number = %d ' % (number)

	# **表示幂次方，2**3就是2^3

	print 'test: %d ' % (1 != 2)
	print 'test: %d ' % (1 >= 2)
	if 1:
		print 'good'
	if 0:
		print 'abc'

	if (2 != 2):
		print 'we are not here'
	print 'test %d ' % (3 + 8)
	print 'test %d ' % (4 - 6)
	print 'test %d ' % (4 * 9)
	print 'test %d ' % (8/2)
	print 'test %d ' % (7//3)
	print 'test %0.2f ' % (7/3)
	print 'test %g' % (5.33%3)


if __name__ == '__main__':
  main()