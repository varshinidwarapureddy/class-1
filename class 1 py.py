Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> a,b=10,20
>>> print(a+b)
30
>>> a,b,c,b,e=10,20,30,40,50
>>> a=10
>>> type(a)
<class 'int'>
>>>  a=true
 
SyntaxError: unexpected indent
>>> a=true
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> type(a)
<class 'int'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a,b,c,d,e=10,20,30,40,50
>>> a=10
>>> type(a)
<class 'int'>
>>> type(a)
<class 'int'>
>>> a=True
>>> type(a)
<class 'bool'>
>>>  def f1():print("good")
 
SyntaxError: unexpected indent
>>> def f1():print("good")
>>>f1()
SyntaxError: invalid syntax
>>> f1()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    f1()
NameError: name 'f1' is not defined
>>> def f1():print("good")
f1()
SyntaxError: invalid syntax
>>> def f1():print("good")
;
SyntaxError: invalid syntax
>>> def f1():print("good")

>>> f1()
good
>>> f1()
good
>>> 