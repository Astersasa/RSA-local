import re
import os
a=('123\n23\n1234\n\n\n')
n=re.split("\n",a)
n=list(filter(None, n))
print(n)