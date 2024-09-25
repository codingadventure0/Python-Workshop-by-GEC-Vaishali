Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sets={"M", "T", "W", "T", "F", "S", "S" }
sets
{'S', 'W', 'F', 'T', 'M'}
sets.discard("M")
sets
{'S', 'W', 'F', 'T'}
sets.remove("V")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sets.remove("V")
KeyError: 'V'
>>> sets2={"J", "F", "M", "A"}
>>> sets2
{'M', 'J', 'A', 'F'}
>>> print(sets|sets2)
{'A', 'J', 'S', 'W', 'F', 'T', 'M'}
>>> print(sets&sets2)
{'F'}
>>> type(sets)
<class 'set'>
>>> dic = {}
>>> type(dic)
<class 'dict'>
>>> dic={101:"AnonumousID", 1010:"Unknown!!", 11011:"Vampire"}
>>> dic
{101: 'AnonumousID', 1010: 'Unknown!!', 11011: 'Vampire'}
>>> dic.keys()
dict_keys([101, 1010, 11011])
>>> dic.values()
dict_values(['AnonumousID', 'Unknown!!', 'Vampire'])
>>> dic[101]
'AnonumousID'
>>> dic[11011]="Alex"
>>> dic
{101: 'AnonumousID', 1010: 'Unknown!!', 11011: 'Alex'}
>>> dic.pop(11011)
'Alex'
>>> for x,y in dic.items():
...     print(x,y)
... 
...     
101 AnonumousID
1010 Unknown!!
>>> len(dic)
2
>>> print(dic.items())
dict_items([(101, 'AnonumousID'), (1010, 'Unknown!!')])
>>> dic.update({11011:["Alex", "Andrew"]})
>>> dic
{101: 'AnonumousID', 1010: 'Unknown!!', 11011: ['Alex', 'Andrew']}
>>> dic(11011[2])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dic(11011[2])
TypeError: 'int' object is not subscriptable
>>> dic[11011][0]
'Alex'
>>> dic.update({1010:"!!Unknown!!"})
>>> dic
{101: 'AnonumousID', 1010: '!!Unknown!!', 11011: ['Alex', 'Andrew']}
