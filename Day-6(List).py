Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[11, "Abhi", "Anonymous", 22]
... 
>>> l
[11, 'Abhi', 'Anonymous', 22]
>>> l.append(33)
>>> l
[11, 'Abhi', 'Anonymous', 22, 33]
>>> l.insert(0, 0)
>>> l
[0, 11, 'Abhi', 'Anonymous', 22, 33]
>>> l.pop()
33
>>> l.remove(0)
>>> l
[11, 'Abhi', 'Anonymous', 22]
>>> l.remove("Anonymous")
>>> l
[11, 'Abhi', 22]
>>> l[0:2]
[11, 'Abhi']
>>> l[1:3]
['Abhi', 22]
>>> len(l)
3
>>> l2=[5,10,20]
>>> l3=[40,80,160]
>>> l2+l3
[5, 10, 20, 40, 80, 160]
>>> max[l2]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    max[l2]
TypeError: 'builtin_function_or_method' object is not subscriptable
