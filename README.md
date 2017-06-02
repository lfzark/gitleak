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
Login:
```
>>> from gitleak import GitLeak
>>> gl = GitLeak('ark1ee')
>>> gl.login('username','password')
root        : INFO     login successfully
True
```

Scan Sensitive Keywords:

```
>>> gl.scan('password')
root        : INFO     after duplicate removal [20 -> 7]
{u'lfzark/ArkPHP': u'17', u'aixiatian/crawdata': u'8', u'lfzark/gitleak': u'2'}

```

## Example
 
Code:

```python 

from gitleak import GitLeak

KEYWORD ='ark1ee'
GITHUB_USERNAME = 'your_username'
GITHUB_PASSWORD = 'your_password'
SENSITIVE_KEYWORD = 'password'


gl = GitLeak(KEYWORD)
if gl.login(GITHUB_USERNAME,GITHUB_PASSWORD):
    print '[+] Total result is about %s' % (gl.get_total_result())
    sensitive_proj_list = gl.scan(SENSITIVE_KEYWORD)
    for proj in sensitive_proj_list:
        print 'Project: %s - %s' %( proj, sensitive_proj_list[proj])
```

Output:
```
root        : INFO     login successfully
[+] Total result is about 21
root        : INFO     after duplicate removal [21 -> 7]
Project: lfzark/ArkPHP - 17
Project: aixiatian/crawdata - 8
Project: lfzark/gitleak - 2

```