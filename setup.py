import os
import git
for env in os.environ:
    print(env)
print('--------------------')
print(os.environ.get('EV'))
print(os.environ.get('EX'))
print(os.environ.get('GH_TOKEN'))
print(os.environ.get('TRAVIS_REPO_SLUG'))

ev=os.environ.get('EV')
ex=os.environ.get('EX')
print("{0} {1}".format(ev,ex))

# https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git

print("setup")
