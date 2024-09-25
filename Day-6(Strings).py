Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str="Abhi"
>>> type(str)
<class 'str'>
>>> str_2 = 'Anonymous'
>>> type(str)
<class 'str'>
>>> str_3 = """ Anonymous is a very danderous group
... That group is also helping in positive way.
... """
>>> 
>>> type(str_3)
<class 'str'>
>>> str_3[0]
' '
>>> str_3[5]
'y'
>>> str[2] = "S"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    str[2] = "S"
TypeError: 'str' object does not support item assignment
>>> str[-1]
'i'
>>>  str_3[-10:-1]
...  
SyntaxError: unexpected indent
>>> str_3[-10:-1]
'tive way.'
>>> print("All ablot anonymous: %s"%str_3)
All ablot anonymous:  Anonymous is a very danderous group
That group is also helping in positive way.

>>> str_4= "{} is a best college for Engineering."
>>> print(str_4.format("GEC, Vaishali"))
GEC, Vaishali is a best college for Engineering.
>>> print(str_4.capatilize())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(str_4.capatilize())
AttributeError: 'str' object has no attribute 'capatilize'. Did you mean: 'capitalize'?
>>> print(str_4.capitalize)
<built-in method capitalize of str object at 0x0000024EF893A1F0>
>>> print(str_4.capitalize())
... 
{} is a best college for engineering.
>>> print(str_4.format("GEC, Vaishali").capitalize())
Gec, vaishali is a best college for engineering.
