#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: lina 20170902

#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去买菜，骑了 2 小时
# - 周三的时候骑电动车去买菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

def main():
	who = '老妈'
	distance = 20 #km
	tool1 = '电动车'
	tool2 = '自行车'

	day1 = '周一'
	time1 = 0.5
	speed1 = distance/time1

	print '%s%s骑%s去买菜，骑了%0.1f小时，平均速度为%0.1fkm/h' %(who,day1,tool1,time1,speed1)

	day2 = '周二'
	time2 = 2

	print '%s%s骑%s去买菜，骑了%0.1f小时，平均速度为%0.1fkm/h' %(who,day2,tool2,time2,distance/time2)

	day3 = '周三'
	time3 = 0.6

	print '%s%s骑%s去买菜，骑了%0.1f小时，平均速度为%0.1fkm/h' %(who,day3,tool1,time3,distance/time3)

if __name__ == '__main__':
	main()

#重复太多，需简化