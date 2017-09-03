#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: jiaguwen

def print_list(lst):
	for lst_item in lst:
		print '%s is an American professional basketball player for the Golden State Warriors.' % (lst_item)	

def main():
	lst = ['Curry', 'Thompson', 'Durant', 'Green']
	print lst

def main2():
	index = 0
	lst = ['Curry', 'Thompson', 'Durant', 'Green']
	for lst_item in lst:
	#	print lst_item
		print '%s is an American professional basketball player for the Golden State Warriors.' % (lst_item)
		print 'No. %d' % (index)
		index = index + 1
	print '--------'

	for index, lst_item in enumerate(lst):
		print '%s is an American professional basketball player for the Golden State Warriors.' % (lst_item)
		print 'No. %d' % (index)

	print '--------'
	print lst[1]
	print lst[3]
	print len(lst)
	lst.append('Zaza')
	print lst
	del lst[3]
	print lst
	print len(lst)
	print list(lst)
	print_list(lst)
	print '------'

	lst2 = lst[0:3]
	print lst2
	print_list(lst2)
	lst3 = lst[1:4]
	print lst3
	print_list(lst3)
if __name__ == '__main__':
	main()
	main2()