Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(11, 22, "Unknown!!", 22, 11)
>>> t
(11, 22, 'Unknown!!', 22, 11)
>>> type(t)
<class 'tuple'>
>>> t[2]
'Unknown!!'
>>> t[0]=33
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t[0]=33
TypeError: 'tuple' object does not support item assignment
>>> res = t.count(22)
>>> print("Count of 22 in touple is:",res)
Count of 22 in touple is: 2
>>> print("Index od 22 is:",t.index(22))
Index od 22 is: 1
>>> sets={"ab", "bc", "cd"}
>>> type(sets)
<class 'set'>
>>> days=set(["S", "M","T", "W", "T", "F", "S"])
>>> type(days)
<class 'set'>
>>> months=set(["Jan", "Feb", "March", "Apr"])
>>> months
{'Jan', 'March', 'Apr', 'Feb'}
>>> months.add("May")
>>> months
{'Apr', 'May', 'March', 'Feb', 'Jan'}
>>> months.discard("May")
>>> months
{'Apr', 'March', 'Feb', 'Jan'}
