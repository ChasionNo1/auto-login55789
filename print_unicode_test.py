import sys
import unicodedata

str1 = ()
word = list(str1)
print(sys.argv[1:])
str3 = "".join(sys.argv[1:])

if str3 in ['-h', '--help']:
    print("usage:{0}{1}".format(sys.argv[0], sys.argv[1]))
    word.append('0')
    print(word)
else:
    word = sys.argv[1:len(sys.argv)]
    print(word)  # 列表获取输入的字符

                                         #sys.argv函数，sys.argv[0]是获取代码本身文件路径
def print_unicode_table(word):
    str2 = "".join(word)
    print(str2)
    print("decimal    hex    char   {0:^40}".format("name"))
    print("-------    ----   ---      {0:-<40}".format(""))
    for i  in range(0,len(str2)):
        code = ord(str2[i])
        c = chr(code)
        name = unicodedata.name(c, "*** unknown  ***")
        print("{0:7}   {0:5X}    {0:^3c}       {1}".format(code, name.title()))


if '0' not in word:
    print_unicode_table(word)
