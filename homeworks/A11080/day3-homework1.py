#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: jiaguwen

# 单一职责原则：一个代码块负责一个任务
# 一个代码块相当于一个函数function
# return可以传递变量
# 可以return多个变量

def account(is_cheap4, good_price4, buy_amount4):
	total_cost = good_price4 * buy_amount4
	if is_cheap4:
		print '老妈在小本子上记下：今天买菜共花了%d元' % (total_cost)

def talk_with_dad(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家，对老爸说："菜好便宜，我买了%d斤。"' % (buy_amount3)
	else:
		print '老妈回到家，对老爸说："菜好贵，我没买。"'

def buy():
	who = 'Lina的妈妈'
	good_description = "西双版纳大白菜"

	good_price = 4
	reasonable_price = 5
	buy_amount = 2
	
	is_cheap = False
	
	print '%s上街看到了%s，卖%d元/斤 ' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
	# 每降低1元，多买1斤
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去 '

	return is_cheap, good_price, buy_amount

def main():
	is_cheap2, good_price2, buy_amount2 = buy()
	talk_with_dad(is_cheap2, buy_amount2)
	account(is_cheap2, good_price2, buy_amount2)

# run function
if __name__ == '__main__':
	main()