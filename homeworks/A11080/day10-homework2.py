#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def day10_homework2():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	who = '老妈'  # 把“老爸”改成“老妈”，只需要修改who变量
	tear_word = 'abandon'  # 要撕掉有哪个词的一页，只需要修改 tear_word 变量

	print '%s在看一本英文书 ' %(who)
	if not search('etiquette', book, who):
		tear_mean = book[tear_word]  # 定义了撕掉的单词的释义，后面只需要引用，不需要重新写
		del book[tear_word]
		print '%s撕掉了有 %s 的一页 ' %(who, tear_word)

		if search('abase', book, who):
			book[tear_word] = tear_mean
			print '%s把有 %s 的一页又粘了回去' %(who, tear_word)
	search('abash', book, who)  # 用定义的函数，避免重复输入
	search('abandon', book, who)

def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s查到了 %s：%s ' %(who, key, dictionary[key])
		return True
	else:
		print '%s没有查到 %s ' %(who, key)
		return False

if __name__ == '__main__':
  day10_homework2()