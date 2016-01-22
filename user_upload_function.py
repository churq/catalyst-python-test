__author__ = 'Ranqing'
# Local-Part String
#
# The local-part string refers to the user name you choose when you create an email account
# (e.g., local-part@subdomain.domain.tld) According to EAUT rules, you can use only "atom" ASCII characters,
# meaning the sequence of ASCII characters from 33 to 126. This excludes spaces, commas, periods and semi-colons
# but includes letters and numbers, dollar signs, ampersands, question marks and underscores.
#
#
# Subdomain and Domain String
#
# The rules for subdomain and domain strings are the same.
# EAUT rules specify that domains and subdomains must be at least one character long and not longer than 63 characters.
# They can include alphanumeric characters (a-z, A-Z and 0 to 9) and the hyphen. Also, domains and subdomains must always
# start with an alpha character and must end with either an alpha or numeric character
#





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
