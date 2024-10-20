''' wir use her  regular expression for spilt string in a python list '''
# Regular expression

# re == regular expression
import re
my_string = 'Ahmad and him Father is in Home'
x = re.split('i', my_string)
print(x)

"""regular expression for spilt string in a python list """
my_string_list = list(['ahmad', 'mariem', 'mohammad'])
for word in my_string_list:
    print(word[0])