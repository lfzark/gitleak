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

Scan Sensitive Keywords From Dictionary:

```
>>> gl.scan_with_dict('./sensitive.keywords')
root        : INFO     after duplicate removal [21 -> 7]
{u'lfzark/pygalib': {'pass': u'1'}, u'aixiatian/crawdata': {'pass': u'3'}, u'r0m3x/RSLegacy': {'pass': u'2'}, u'lfzark/ArkPHP': {'pass': u'22'}}

```
Get unique project list:

```
>>> gl.get_unique_proj_list()
root        : INFO     after duplicate removal [21 -> 7]
[u'aixiatian/crawdata', u'r0m3x/RSLegacy', u'stewartj95/tetris', u'lfzark/gitleak', u'lfzark/pygalib', u'lfzark/modal_j', u'lfzark/ArkPHP']

```
Get Project list:

```
>>> gl.get_project_list()
[
{'file_name': u'README.md', 'indexed_time': u'2017-06-02T08:19:24Z', 'project_name': u'lfzark/gitleak', 'project_href': u'https://github.com//lfzark/gitleak', 'file_href': u'/lfzark/gitleak/blob/909030dae4cd655fb3feb11b94c69c395b85e510/README.md'},
{'file_name': u'setup.py', 'indexed_time': u'2017-06-02T08:19:24Z', 'project_name': u'lfzark/gitleak', 'project_href': u'https://github.com//lfzark/gitleak', 'file_href': u'/lfzark/gitleak/blob/909030dae4cd655fb3feb11b94c69c395b85e510/setup.py'},
{'file_name': u'GitLeak.py', 'indexed_time': u'2017-06-02T08:19:24Z', 'project_name': u'lfzark/gitleak', 'project_href': u'https://github.com//lfzark/gitleak', 'file_href': u'/lfzark/gitleak/blob/909030dae4cd655fb3feb11b94c69c395b85e510/gitleak/GitLeak.py'},
{'file_name': u'bower.json', 'indexed_time': u'2017-05-24T06:50:55Z', 'project_name': u'lfzark/modal_j', 'project_href': u'https://github.com//lfzark/modal_j', 'file_href': u'/lfzark/modal_j/blob/df59b829e70a594496414b90585402f23cdfa87c/bower.json'}, 
{'file_name': u'modal_j.js', 'indexed_time': u'2017-05-24T06:44:38Z', 'project_name': u'lfzark/modal_j', 'project_href': u'https://github.com//lfzark/modal_j', 'file_href': u'/lfzark/modal_j/blob/5f218f77eacc68830296d8e2b2d48a5469334abb/modal_j.js'}, 
{'file_name': u'global_var.php', 'indexed_time': u'2017-05-14T06:22:54Z', 'project_name': u'lfzark/ArkPHP', 'project_href': u'https://github.com//lfzark/ArkPHP', 'file_href': u'/lfzark/ArkPHP/blob/5c9b7662615c2d101671528e5428649ef0500c60/framework/config/global_var.php'}, 
{'file_name': u'setting.class.php', 'indexed_time': u'2017-05-14T06:22:54Z', 'project_name': u'lfzark/ArkPHP', 'project_href': u'https://github.com//lfzark/ArkPHP', 'file_href': u'/lfzark/ArkPHP/blob/5c9b7662615c2d101671528e5428649ef0500c60/pecan/controllers/setting.class.php'}, 
{'file_name': u'index.php', 'indexed_time': u'2017-05-14T06:22:54Z', 'project_name': u'lfzark/ArkPHP', 'project_href': u'https://github.com//lfzark/ArkPHP', 'file_href': u'/lfzark/ArkPHP/blob/5c9b7662615c2d101671528e5428649ef0500c60/framework/plugins/encrypt/index.php'}
.....
]
```
Get total number of projects:

```

>>> gl.get_total_result()
u'21'
>>> 


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