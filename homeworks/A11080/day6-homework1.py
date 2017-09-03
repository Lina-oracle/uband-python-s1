#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: jiaguwen


def print_list(lst):
	for lst_item in lst:
		print '%s ' %(lst_item)

# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
def main():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	print '老妈来到菜市场 '
	index = 0
	for lst_item in lst:
		if (index % 2) == 0:
			print '老妈看到%s，买了%d斤 ' %(lst_item, index + 1)
		else:
			print '老妈看到%s，不买 ' %(lst_item)
		print '老妈继续逛'
		index = index + 1
	print '---------'

def main2():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	print '老妈来到菜市场 '
	for index, lst_item in enumerate(lst):
		if (index % 2) == 0:
			print '老妈看到%s，买了%d斤 ' %(lst_item, index + 1)
		else:
			print '老妈看到%s，不买 ' %(lst_item)
		print '老妈继续逛 '
	print '----------'

# 2. 完成后，用今天的学到的列表知识，加 3 个菜
	lst.append('茄子')
	lst.append('黄瓜')
	lst.append('粽子')
	print_list(lst)
	print '----------'

#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
	lst2 = lst[5:10]
	print '老妈来到菜市场 '
	for index2, lst_item2 in enumerate(lst2):
		if (index2 % 2) == 0:
			print '老妈看到%s，买了%d斤 ' %(lst_item2, index2 + 1)
		else:
			print '老妈看到%s，不买 ' %(lst_item2)
		print '老妈继续逛 '

if __name__ == '__main__':
#	main()
	main2()