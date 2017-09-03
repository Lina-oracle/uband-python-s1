#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jiaguwen

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup[1:3]
 
  # 是否存在某值
  print (1 in tup)
  print (0 in tup)
  
  # 赋值
  a = tup[0]
  print a
  b, c, d = tup[1:]
  print b, c, d
  print '----'

  # 遍历
  for item in tup:
    print item
  print '----'

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    # tup.append(7)
    # tup[2] = 1
    # del tup[0]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


