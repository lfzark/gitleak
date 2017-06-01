Github Leaked Source Code Scanner with Python (gitleak) 
======================= 
### A tool library for searching your leaked sourcecode on github

---- 

## Installation 

Use pip: 
```
pip install gitleak 
```
if you want to install from source code , you can download from pypi or simple use: 
```
git clone https://github.com/lfzark/gitleak 
```
then run: 
```
python setup.py install 
```

## Usage

```
>>> from gitleak import gl
>>> gl.login('username', 'password')
root        : INFO     login successfully
True
>>> gl.scan('password')
root        : INFO     after duplicate removal [18 -> 6]
{u'aixiatian/crawdata': u'8', u'lfzark/ArkPHP': u'17'}
```

## Example 

```python 


```
