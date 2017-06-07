from gitleak import GitLeak

KEYWORD ='keyword'
GITHUB_USERNAME = 'username'
GITHUB_PASSWORD = 'password'


gl = GitLeak(KEYWORD)
if gl.login(GITHUB_USERNAME,GITHUB_PASSWORD):
    gl.max_page = 2
    print '[+] Total result is about %s' % (gl.get_total_result())
    proj_list = gl.get_project_list()
    for proj in proj_list:
        print '[+] %s' %( proj)
