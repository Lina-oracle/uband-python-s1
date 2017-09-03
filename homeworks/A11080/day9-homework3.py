#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def main():
	dictionary = {
					'abandon': 'to give up to the control or influence of another person or agent',
					'abase': 'to lower in rank, office, prestige, or esteem',
					'abash': 'to destroy the self-possession or self-confidence of'
					}

	print '老爸在看一本英文书，翻开手边的词典想查词'
#	lst = dictionary.keys()
	lst = ['abandon', 'abase', 'abash']

	print '词典里只有三个词 %s，%s，%s' %(lst[0], lst[1], lst[2])

	print '老爸先查了一个词 etiquette'
	
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']
	else:
		print '竟然没有查到'
		del dictionary['abandon']  #虽然用了删除词条，但没有显示出来，abandon用的列表的序列
		print '老爸怒了，撕掉了有%s的一页' %(lst[0])

	print '老爸又查了一个词 abase'

	if dictionary.has_key('abase'):
		print '老爸得到了abase的解释：%s ' %(dictionary['abase'])
		print '老爸很开心，又把有%s的一页加入了词典' %(lst[0])
		dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	
	print '词典又变回了原样'
	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
  main()