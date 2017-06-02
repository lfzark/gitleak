#!usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import logging
import math
import requests
import sys
import time
import urllib


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', 
                    filename='gitleak.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def judge_login(func):
    
    def is_login(self, *args, **kwargs):
        if not self.is_logged:
            logging.warn('[-] not logged in yet.')
        return func(self, *args, **kwargs)
    return is_login

INTERVAL_TIME = 5
NUM_PAGE = 10.0
MAX_PAGE = 50
RESULT_NUM_RE = '#js-pjax-container > div.container > div > div.column.three-fourths.codesearch-results.pr-6 > div.d-flex.flex-justify-between.border-bottom.pb-3 > h3'

class GitLeak():
    '''
    Github泄漏监控
    '''

    def __init__(self,_keyword='ark1ee'):
        '''
        Constructor
        '''
        self.cookie = ''
        self.q = requests.session()
        self.q.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                          "Accept-Encoding": "gzip, deflate, br",
                          "Accept-Language": "zh-CN,zh;q=0.8",
                          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0"
                         }
        self.keyword =_keyword 
        self.is_logged = False
        self.project_result = []
        self.set_query_url()

    def login(self, username, password):
        
        LOGIN_URL = 'https://github.com/login'
        SESSION_URL = 'https://github.com/session'

        login_content = self.q.get(LOGIN_URL).content
        token_finder = BeautifulSoup(login_content, "html.parser")
        token = token_finder.find('input', {'name': 'authenticity_token'})['value']

        post_params = {
            'commit': 'Sign+in',
            'utf8': "✓",
            "login": username,
            "password": password,
            'authenticity_token':token
        }

        if self.q.post(SESSION_URL, data=post_params,).content.count(username) > True:
            logging.info('login successfully')
            self.is_logged = True
        else:
            logging.error('login failed')
            self.is_logged = False
            
        return self.is_logged

    def set_query_url(self, repository='', order='desc', keyword=None, stype='Code', s='indexed'):
        if keyword != None:
            _keyword = keyword
        else:
            _keyword = self.keyword
            
        self.url = 'https://github.com/%ssearch?o=%s&utf8=✓&q=%s&s=%s&type=%s' % (urllib.quote(repository.decode(sys.stdin.encoding).encode('gbk'))
+ '/', order, _keyword, s, stype)
        
        return self.url
    
    @judge_login
    def get_page_content(self, page=1, url=None):
        
        if url == None:
            rquest_url = self.url
        else:
            rquest_url = url
            
       
        logging.debug('[+] request' + rquest_url + "&p=%s" % page)

        try:
            r = self.q.get(rquest_url + "&p=%s" % page)
             
            if r.status_code == 200:
                return r.content
            else:
                return '<html>not 200 reuturn</html>'
             
        except Exception as e:
            return '<html>%s</html>' % e
        
    def get_total_page(self):
        
        return int(math.ceil (int(self.get_total_result()) / NUM_PAGE))
    
    def get_project_list(self):

        total_page = self.get_total_page()
        
        if total_page == 0:
            logging.error('no project.')
            exit()

        if total_page < MAX_PAGE:
            end_page = total_page 
        else:
            end_page = MAX_PAGE 
            
        for _ in range(1, end_page + 1):
            
            time.sleep(INTERVAL_TIME)
            html_content = self.get_page_content(page=_)
            p_result = self.extract_project_list(html_content)
            
            self.project_result += p_result
        return self.project_result
    
#         for project_name in [ _['project_name'] for _ in self.project_result]:
#             print self.set_query_url(repository=project_name, keyword='password')
#             content = self.get_page_content(url = self.set_query_url(repository=project_name,keyword='password')) 
#             print self.get_total_result(content)

    def extract_project_list(self, html_content):

        result = []
        soup = BeautifulSoup(html_content, 'html5lib')
        #
        code_list = soup.find_all(attrs={'class': 'code-list-item'})

        if len(code_list) > 0:
            
            for item in code_list:
                #
                project_info = item.select('div.d-inline-block.col-10 > a.text-bold')[0]
                project_href = 'https://github.com/%s' % project_info.attrs['href']
                project_name = project_info.string 

                file_info = item.select('div.d-inline-block.col-10 > a:nth-of-type(2)')[0]
                file_href = file_info.attrs['href']
                file_name = file_info.string 

                indexed_time = item.find('relative-time').attrs['datetime']
                
                result.append({'project_name':project_name, 'project_href':project_href, 'file_name':file_name, 'file_href':file_href, 'indexed_time':indexed_time})

        return result 


    def get_total_result(self, content=None):

        if content == None:
            page_content = self.get_page_content()
        else:
            page_content = content

        s = BeautifulSoup(page_content, "lxml")
        
        RESULT_NUM_RE = '#js-pjax-container > div.border-bottom.mb-4 > div > nav > a.underline-nav-item.selected > span'
        


        result_num = s.select(RESULT_NUM_RE)
        if len(result_num) == 0:
            return 0
        else:
            return result_num[0].string

    def get_total_result_from_proj(self, content=None):
        
        if content == None:
            return 
        else:
            page_content = content

        s = BeautifulSoup(page_content, "lxml")
        
        RESULT_NUM_RE = '#js-repo-pjax-container > div > div.repository-content > div.border-bottom.mb-4 > div > nav > a.underline-nav-item.selected > span'
        
        result_num = s.select(RESULT_NUM_RE)
        if len(result_num) == 0:
            return 0
        else:
            if result_num[0].string.find('K'):
                result_num[0].string=result_num[0].string.replace('K',"000")
            elif result_num[0].string.find('M'):
                result_num[0].string=result_num[0].string.replace('M',"000000")

    def scan(self, _sensitive_word):
 
        proj_list_duplicate = self.get_unique_proj_list()
        
        key_result = {}
        for proj in proj_list_duplicate:
            p_url = self.set_query_url(repository=proj, keyword=_sensitive_word)
            p_content = self.get_page_content(url=p_url)
            key_num = self.get_total_result_from_proj(p_content)
            if key_num > 0:
                key_result[proj] = key_num
        return key_result
    
    def get_unique_proj_list(self): 
        total_page = self.get_total_page()
        result_list = []
        
        for _ in range(1, total_page + 1):
            result = self.extract_project_list(self.get_page_content(page=_))
            result_list += result
            
        # 去重
        proj_list = map(lambda x :x['project_name'], result_list)

        proj_list_duplicate = list(set(proj_list))
        
        logging.info('after duplicate removal [%d -> %d]' % (len(proj_list), len(proj_list_duplicate)))

        return proj_list_duplicate
    
    def check_sensitive_word_from_dict(self,path):
        
        proj_list_unique = self.get_unique_proj_list()
 
        scan_result = {}
        with open(path,'r') as k_dict:
            for k in  k_dict.readlines():

                for proj in proj_list_unique:
                    p_url = self.set_query_url(repository=proj, keyword=k)
                    p_content = self.get_page_content(url=p_url)
                    key_num = self.get_total_result_from_proj(p_content)
                    if key_num > 0:
                        scan_result[proj] ={}
                        scan_result[proj][k] = key_num

        return scan_result
    






