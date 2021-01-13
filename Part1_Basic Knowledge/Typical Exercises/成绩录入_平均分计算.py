# _*_ coding: utf-8 _*_

"""
录入6个学生的3门课程考试成绩（input部分）
计算每个学生的平均分和每门课的平均分（自动输出部分）

Oringinal author: 骆昊
Enhanced detail editor: Yifeng

"""

"""思路
1.对于输入者，最后要呈现的是：录入A同学math成绩；A同学的English成绩；A同学的statistics
  成绩。继而继续输入B同学等。
2.由此可见，我们先要循环学生名字，在此循环下，再循环输入每个科目的成绩。
3.当完成了这一系列的循环录入，最后再进行计算。

"""

names = ['A', 'B', 'C', 'D', 'E', 'F']
courses = ['math', 'English', 'statistics']
# 最终我们想创建的是一个列表，用来存储6人的3门成绩。这一步很关键，因为我们需要创建的是
# 一个嵌套的列表，大列表下面有6个小列表，小列表里有3个元素。
# 此处建议print(scores)看一看到底长什么样。

scores = [[0] * len(courses) for _ in range(len(names))]
# scores = [[0] * len(courses)] * len(names)
# 26与27行生成的列表长得一样，为什么最后会导致计算平均值时的不同？ 27行的结果很神奇？
# 我用28行的代码试了一次，也是没问题的。

print(scores)
# 创建好了保存成绩的列表后，就要开始录入数据,先自查enumerate的含义。
for i, name in enumerate(names):
	print(f'please input {name} score ===>')
	for j, course in enumerate(courses):
		# 此处的理解很关键，以第一次循环为例，此时在enumerate的作用下，i和j都是索引
		# 0，而name和course分别为A和math。此刻输入的成绩就会录入到索引位置scores[0][0]。
		scores[i][j] = float(input(f'{course}: '))
		
# 计算成绩和展示
print('-' * 5, 'Student Average Score', '-' * 5)
# 这一个循环很关键，因为我们是嵌套的列表，当我们计算每一个学生的平均分
# 时，只需要里面小列表的和，因此我们需要用enumerate来提取。
for index, name in enumerate(names):
	# 这里建议print(score[index])看一看,此处的scores[0]，实际是第一个小列表
	avg_score = sum(scores[index]) / len(courses)
	print(f'{name} average score is: {avg_score:.1f}')

print('-' * 5, 'Course Average Score', '-' * 5)
for index, course in enumerate(courses):
	# 此处使用的是链表推导式，建议自行学习先，熟练掌握需要时间。
	curr_course_scores = [score[index] for score in scores]
	avg_score = sum(curr_course_scores)/len(names)
	print(f'{course} average score is: {avg_score:.1f}')
