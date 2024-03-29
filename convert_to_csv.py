import re

data = "259,2 0 1 0.000000000 4020 Q R 282624 + 8 [java]"
data = re.sub(r'\s+', ',', data)
print(data)
