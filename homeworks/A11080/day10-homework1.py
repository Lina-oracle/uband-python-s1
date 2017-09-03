#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def day10_homework():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
          	"abase": "to lower in rank, office, prestige, or esteem",
          	"abash" : "to destroy the self-possession or self-confidence of"
			}
	print '老妈在看一本英文书 '
	if not book.has_key('etiquette'):
		print '老妈没有查到 %s 的意思' %('etiquette')
		del book['abandon']
		print '老妈撕掉了有 %s 的一页' %('abandon') 

		if book.has_key('abase'):
			print '老妈查到了 %s ： %s' %('abase', book['abase'])

			book['abandon'] = 'to give up to the control or influence of another person or agent'
			print '老妈把 %s 的字典页又粘上了' %('abandon')  # 把撕掉的改成abase，要修改5处
		else:
			print '老妈没有查到 %s 的意思' %('abase')
	else:
		print '老妈查到了 %s ： %s' %('etiquette', book['etiquette']) # 7处改成了“老妈”
	
	if book.has_key('abase'):
		print '老爸查到了 %s ： %s' %('abase', book['abase'])
	if book.has_key('abash'):
		print '老爸查到了 %s ： %s' %('abash', book['abash'])

if __name__ == '__main__':
  day10_homework()