#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lina 20170903

import codecs
import os

#用-分割
def word_spilit(words):
	new_list = []
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst = word.split('-')
			new_list.extend(lst)
	return new_list

#1.读取文件
def read_file(file_path):
	f = codecs.open(file_path,'r','utf-8')
	word_list = []
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		words = line.split(" ")
		words = word_spilit(words)
		word_list.extend(words)
	return word_list

#读取多文件
def read_files(file_paths):
	final_words = []
	for path in file_paths:
		read_file(path)
		final_words.extend(read_file(path))
	return final_words

#2.获取格式化之后的单词
def format_word(word):
	fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
	for char in word:
		if char not in fmt:
			word = word.replace(char, '')
	return word.lower()

def format_words(words):
	word_list = []
	for word in words:
		wd = format_word(word)
		if wd:
			word_list.append(format_word(word))
	return word_list

#3. 统计单词数目
def statistics_words(words):
	s_word_dict = {}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word] = s_word_dict[word]+1
		else:
			s_word_dict[word] = 1
	return s_word_dict

#3.读取文件夹里的所有文件
def get_file_from_folder(folder_path):
	file_paths = []
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			# print file_path
			file_paths.append(file_path)
	return file_paths

#4. 输出为csv
def print_to_csv(volcaulay_map,to_file_path):
	nfile = open(to_file_path,'w+')
	for key in volcaulay_map.keys():
		val = volcaulay_map[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()


def main():
	#get files
	paths = get_file_from_folder('E:/study/Python/Uband-S1/week4_final-homework/data2')
	# print len(paths)

	#1. read file
	words = read_files(paths)
	# words = read_files(['E:/study/Python/Uband-S1/week4_final-homework/data2/2016.01.02.TXT','E:/study/Python/Uband-S1/week4_final-homework/data2/2016.01.09.TXT'])
	# print words
	print '获取到%d个未格式化的单词 ' %(len(words))

	#2. format word
	# print format_word(' make  ')
	# print format_word('  kill-a')
	# print format_word('Aleppo!\u201d')
	# print format_word('Barack')

	f_words = format_words(words)
	# print f_words
	print '获取到%d个格式化的单词 ' %(len(f_words))

	#3. 统计单词数目
	word_dict = statistics_words(f_words)
	# print word_dict
	#4. 输出为scv
	print_to_csv(word_dict,'E:/study/Python/Uband-S1/homeworks-A11080/output.csv')


if __name__ == '__main__':
	main()

