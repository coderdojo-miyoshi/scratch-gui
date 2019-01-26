import os
import git
#for env in os.environ:
#    print(env)
print('--------------------')
print(os.environ.get('EV'))
print(os.environ.get('EX'))
print(os.environ.get('GH_TOKEN'))
print(os.environ.get('TRAVIS_REPO_SLUG'))

ev=os.environ.get('EV')
ex=os.environ.get('EX')
travis_repo_slug=os.environ.get('TRAVIS_REPO_SLUG')

print("https://{0}@github.com/{1}.git".format(ev,travis_repo_slug))

