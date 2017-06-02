from gitleak import GitLeak

KEYWORD ='your_keyword'
GITHUB_USERNAME = 'your_username'
GITHUB_PASSWORD = 'your_password'
SENSITIVE_KEYWORD = 'password'


gl = GitLeak(KEYWORD)
if gl.login(GITHUB_USERNAME,GITHUB_PASSWORD):
    print '[+] Total result is about %s' % (gl.get_total_result())
    sensitive_proj_list = gl.scan(SENSITIVE_KEYWORD)
    for proj in sensitive_proj_list:
        print 'Project: %s - %s' %( proj, sensitive_proj_list[proj])