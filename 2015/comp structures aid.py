Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[4,1,2,6,7,3]
>>> b='412673'
>>> a[1]=9
>>> b[1]=9
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b[1]=9
TypeError: 'str' object does not support item assignment
>>> b[1]='9'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b[1]='9'
TypeError: 'str' object does not support item assignment
>>> a
[4, 9, 2, 6, 7, 3]
>>> b
'412673'
>>> fruit=['banana','avocado','peach','orange','peach','peach']
>>> fruit.count(peach)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fruit.count(peach)
NameError: name 'peach' is not defined
>>> fruit.count('peach')
3
>>> fruit.reverse()
>>> fruit
['peach', 'peach', 'orange', 'peach', 'avocado', 'banana']
>>> fruit.remove('peach')
>>> fruit
['peach', 'orange', 'peach', 'avocado', 'banana']

>>> fruit.sort()
>>> fruit
['avocado', 'banana', 'orange', 'peach', 'peach']
>>> fruit.index('orange')
2
>>> fruit.insert(2,'canteloupe')
>>> fruit
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'peach']
>>> fruit.pop()
'peach'
>>> fruit
['avocado', 'banana', 'canteloupe', 'orange', 'peach']
>>> fruit.append('starfruit')
>>> fruit
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
>>> (3<4)+5
6
>>> high+5
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    high+5
NameError: name 'high' is not defined
>>> 'high'+str(5)
'high5'
>>> int(5/2)
2
>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(64)
8.0
>>> import fractions
>>> 3/4
0.75
>>> fractions.Fraction(3,4)
Fraction(3, 4)
>>> for x in fruit:
	print(x)
	fruit

	
avocado
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
banana
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
canteloupe
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
orange
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
peach
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
starfruit
['avocado', 'banana', 'canteloupe', 'orange', 'peach', 'starfruit']
>>> fruit=['banana','apple','orange','watermelon','peach']
>>>for whatever in fruit:
>>>print(whatever)
  
