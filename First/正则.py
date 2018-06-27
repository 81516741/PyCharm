
import re

print(re.search('www', 'www.w3cschool.cn').span())  # 在起始位置匹配
print(re.search('com', 'www.w3cschool.com').span())         # 不在起始位置匹配
from imp import *
reload()