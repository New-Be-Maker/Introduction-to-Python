"""
Request API of Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise is from textbook <Python Crash Course>

:copyright: by Eric Matthes
:enhanced detail editor: by Yifeng
"""

import requests

"""
Part 1
This part is simply connect Github and get some information
"""

# 运用方法get将API里的信息存储在r变量里
# q=*****这部分内容是否都需要自己来填入 ？
# 如何阅读及好好利用https://api.github.com/  ？
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# 相应回来的对象(存储在变量r里面）里有一个status_code的属性，200表示的是响应成功
print("Status code:", r.status_code)

# 我们将API response(响应回来的是json格式的)存储在response_dict这个变量中。【并用json()使之转化为一个python的字典？】
# 简而言之，应该涉及到一个核心问题：当我们request从而得到response的过程中，究竟发生了什么？
response_dict = r.json()
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

# 了解更多有关repositories的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected info. about the first repository")
print("Name:", repo_dict['name'])
# print("Owner:", repo_dict['owner']['login'])为什么就要报错呢？ 且Line45输出了很多东西。
print("Owner:", repo_dict['owner'])
print("Stars:", repo_dict['stargazers_count'])
print("Repository:", repo_dict['html_url'])

"""
Part 2
"""
