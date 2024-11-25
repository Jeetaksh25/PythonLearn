import re
from icecream import ic

"""String="India is asian region"
R=re.search("^India.*reg.*$",String) # ^ = start of the string , $ = end of the string
ic(R)
if R:
    print("Match found")
else:
    print("Match not found")"""

String2="The rain in spain"
R2=re.findall("in",String2)
ic(R2)
ic(len(R2))