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
pip install -r requirements.txt

python setup.py install 
```

## Usage

```
>>> from gitleak import GitLeak
>>> gl = GitLeak('ark1ee')
>>> gl.login('username','password')
root        : INFO     login successfully
True
>>> gl.scan('password')
root        : INFO     after duplicate removal [20 -> 7]
{u'lfzark/ArkPHP': u'17', u'aixiatian/crawdata': u'8', u'lfzark/gitleak': u'2'}

```

## Example 

```python 


```
