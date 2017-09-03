#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def main():
	dictionary = {
				'good': 'of a high standard or quality',
				'nice': 'pleasant, attractive, or enjoyable',
				'pretty': 'a woman or child who is pretty has a nice, attractive face'
				}     #大括号在的位置缩进多少不影响
				
	print dictionary.keys()  #获取key，注意keys后面要加括号
	print dictionary.values()  #获取value，注意时values复数
	print dictionary   #获取整个列表
	print len(dictionary)   #字典长度
	print '------'

	print dictionary.has_key('good')  #有good这个词
	print dictionary.has_key('bad')   #没有bad这个词
	print dictionary['good']   #输出词条释义，用方括号[]
	print '--------'

	dictionary['beautiful'] = 'extremely attractive to look at'
	print dictionary.keys()
	print '------'

	if dictionary.has_key('pretty'):
		print dictionary['pretty']
	else:
		print 'no pretty'
	print '------'

	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print 'no bad'
	print '-----'

	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
  main()