#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def search(search):
	dictionary = {
					'abandon': 'to give up to the control or influence of another person or agent',
					'abase': 'to lower in rank, office, prestige, or esteem',
					'abash': 'to destroy the self-possession or self-confidence of'
					}
	return search
def searching(search):
	if dictionary.has_key(search):
		print '看到了%s ' %(search)
		print dictionary[search]
		if dictionary.has_key('abandon'):
			pass
		else:
			dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
		print '很开心，现在有%s ' %(dictionary.keys())
	else:
		del dictionary['abandon']  #虽然用了删除词条，但没有显示出来，abandon用的列表的序列
		print '老爸怒了，撕掉了有%s的一页，现在有%s' %(search, dictionary.keys())
	return search

def main():
	search1 = 'etiquette'
	searching(search1)
	search2 = 'abase'
	searching(search2)

if __name__ == '__main__':
  main()