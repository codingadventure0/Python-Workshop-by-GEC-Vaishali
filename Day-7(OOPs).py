Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class car:
...     def __init__(self):
...         self.brand="SUZIKI"
...         self.color="Blue"
...         self.top_speed=200
... 
...         
>>> car = car()
>>> car
<__main__.car object at 0x000001613AA216A0>
>>> car.brand
'SUZIKI'
>>> car.color
'Blue'
>>> 
>>> class Car:
...     def __init__(self, b, c, ts):
...         self.brand=b
...         self.color=c
...         self.top_speed=ts
... 
...         
>>> car=Car("Kawasaki", "CarbonBlack", 300)
>>> car.brand
'Kawasaki'
>>> class Testing:
...     def __init__(self,s,t,o):
...         self.scan=s
...         self.tool=t
...         self.os=o
...     def mode(self):
...         print(self.tool," is scanning on",self.os)
... 
...         
>>> test=Testing("Web","OWASPZAP","Windows")
>>> test.mode()
OWASPZAP  is scanning on Windows
