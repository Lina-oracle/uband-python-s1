#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def main():
	dictionary = {
					'abandon': 'to give up to the control or influence of another person or agent',
					'abase': 'to lower in rank, office, prestige, or esteem',
					'abash': 'to destroy the self-possession or self-confidence of'
					}

	print dictionary.keys()
	
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']
	else:
		del dictionary['abandon']
		print dictionary.keys()

	if dictionary.has_key('abase'):
		print dictionary['abase']
		dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
		print dictionary.keys()

	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
  main()