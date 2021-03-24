import os
from datetime import datetime, timedelta


def git_shell(git_command):
    try:
        return os.popen(git_command).read().strip()
    except:
        return None


date = datetime.now()
n = 360

while n > 0:
    commit_date = date - timedelta(days=n)
    n = n - 1
    with open("./README.md", 'a+') as f:
        f.write(commit_date.strftime("- %Y-%m-%d %H:%M:%S \n"))
    git_shell('git add .')
    git_shell(r'git commit -am "feat: test"')
    print(commit_date.strftime('git commit --amend --date="%a, %d %b %Y 15:43:51 +0800"'))
    git_shell(commit_date.strftime('git commit --amend --date="%a, %d %b %Y 15:43:51 +0800"'))
    print(git_shell('git push'))

print('done')
