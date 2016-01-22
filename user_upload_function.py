__author__ = 'Ranqing'

import re
def isemail(str):
    if str =='':
        return 0
    else:
        if re.match(r'[a-zA-Z_0-9$?&]+@',str):
            str1,str2 = str.split('@',1) #str1 is before '@', str2 is after '@'
            if re.fullmatch(r'[a-zA-Z0-9]+.[a-zA-Z0-9]+',str2) or re.fullmatch(r'[a-zA-Z0-9]+.[a-zA-Z0-9]+.[a-zA-Z0-9]+',str2):
                domainList=str2.split('.')
                domainValidation = [map(lambda x: 1 if len(x)<=63 and x[0].isalpha() and (x[-1].isalpha() or x[-1].isdigit()) else 0,domainList)]
                if domainValidation.count(0)==0:
                    return 1
                else:
                    return 0

            else:

                return 0
        else:

            return 0

str='c@h.'
print (isemail(str))
