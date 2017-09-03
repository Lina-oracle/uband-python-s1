#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: jiaguwen

def main():
	lst = ['Curry', 'Thompson', 'Durant', 'Green']
	print lst

def main2():
	lst = ['Curry', 'Thompson', 'Durant', 'Green']
	for lst_item in lst:
		print lst_item
		print '%s is an American professional basketball player for the Golden State Warriors.' % (lst_item)

if __name__ == '__main__':
	main()
	main2()