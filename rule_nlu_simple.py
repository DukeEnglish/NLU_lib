'''
本代码针对问题为有限集合，且可以具有所有现有问题，可以整理成为正则模版。并且问题集合建议不要超过1k条。否则可能会在性能上有过大损耗（未测算）
实现原理：
1、首先对问题进行模版编辑，按照正则模版进行编辑
2、利用正则表达式进行问题关键词提取
3、利用这些关键词进行后续操作


match_file: 符合(.*)的句子是，类型
'''
import sys
import re
import json

fi_name = 'input.txt'
fo_name = 'output.txt'
module_match_file = 'module_match_file'

fout = open(fo_name,'w')

#####  module_set
module_set = set()

# re.module , question_class
for line in open(module_match_file):
	line = line.strip()
	if len(line)!=0:
		module_set.add(line)
print('The file of module_set has been read finished')
print('The length of module_set set is:', len(module_set))

##### analysis sentence
def NLU_rule(input_line):
	for line in module_set:
		# print(line) 
		line = line.split('，')
		# print(line[0].strip(), input_line)
		res = re.findall(line[0].strip(), input_line, re.M)
		if res:
			print('res is :',res)
			q_class = line[1].strip()
			break
		else:
			res = "no match"
			q_class = "We have no this kind of module right now"
	# 对q-class 进行分类
	fout.write(input_line+'@'+'|'.join(res)+'@'+q_class+'@'+'|'.join(type_unit)+'\n')


if __name__ == '__main__':
	NLU_rule()
