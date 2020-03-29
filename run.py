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
    command = commit_date.strftime('git commit --date="%a, %d %b %Y 15:43:51 +0800" -am "feat: test."')
    git_shell(command)
    print(git_shell('git push'))

print('done')
