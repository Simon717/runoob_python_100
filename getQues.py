import os

import requests
from lxml import etree

url = 'https://www.runoob.com/python/python-exercise-example{}.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
if os.path.exists('菜鸟100.md'):
    os.remove('菜鸟100.md')
for i in range(100):
    response = requests.get(url.format(i+1), headers=headers).text
    code = etree.HTML(response)
    info = code.xpath('/html/body/div[4]/div/div[2]/div/div[3]/div/p[2]/text()')
    fenxi = code.xpath("/html/body/div[4]/div/div[2]/div/div[3]/div/p[3]/text()")
    with open('菜鸟100.md', 'a', encoding='utf-8') as f:
        f.write(f"## 题目{i+1:03d}\n\n "
                f"**题目**：{info[0] if info else ''}\n\n "
                f"**分析**：{fenxi[0] if fenxi else ''}\n\n "
                f"**链接**: [菜鸟教程]({url.format(i+1)})\n\n "
                f"**实现**: \n```python\n\n``` \n")
    # break
