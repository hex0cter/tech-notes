# [Python - Split a string by spaces — preserving quoted substrings](http://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python)


```python
>>> import shlex
>>> shlex.split('this is "a test"')
['this', 'is', 'a test']
```
