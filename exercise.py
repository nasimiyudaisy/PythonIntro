Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> counter =100
>>> mile=10
>>> print counter
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(counter)?
>>> print(counter)
100
>>> a=b=c=d=1
>>> print(a)
1
>>> a=b=c="John"
>>> print(a)
John
>>> var1=1
>>> var2=10
>>> var3=15
>>> del var1;var2
10
>>> str="Hello World)
SyntaxError: EOL while scanning string literal
>>> str="hello world"
>>> print(str[0])
h
>>> 
guestList['daisy'; 'amani';'elkanah';'john')
SyntaxError: invalid syntax
>>> list=['daisy'; 'amani'; 'john']
SyntaxError: invalid syntax
>>> list=['daisy','amani','john']
>>> print(list)
['daisy', 'amani', 'john']
>>> list.append("sophia)
	    
SyntaxError: EOL while scanning string literal
>>> list.append("sophia")
>>> list.append("nasimiyu")
>>> list.append("gorgeis")
>>> print(list)
['daisy', 'amani', 'john', 'sophia', 'nasimiyu', 'gorgeis']
>>> list.remove("nasimiyu")
>>> print(list)
['daisy', 'amani', 'john', 'sophia', 'gorgeis']
>>> del list[o]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    del list[o]
NameError: name 'o' is not defined
>>> del list[0]
>>> print(list)
['amani', 'john', 'sophia', 'gorgeis']
>>> print(list[0])
amani
>>> print(list[1:3])
['john', 'sophia']
>>> guests=('1','2','3','4')
>>> print(guests)
('1', '2', '3', '4')
>>> 
