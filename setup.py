import os
import git
#for env in os.environ:
#    print(env)
#print('--------------------')
#print(os.environ.get('GH_TOKEN'))
#print(os.environ.get('TRAVIS_REPO_SLUG'))

travis_repo_slug=os.environ.get('TRAVIS_REPO_SLUG')
gh_token=os.environ.get('GH_TOKEN')
print("https://{0}@github.com/{1}.git".format(gh_token,travis_repo_slug))

