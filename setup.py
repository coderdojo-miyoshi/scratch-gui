import os
import git
#for env in os.environ:
#    print(env)

travis_repo_slug=os.environ.get('TRAVIS_REPO_SLUG')
gh_token=os.environ.get('GH_TOKEN')
url="https://{0}@github.com/{1}.git".format(gh_token,travis_repo_slug)

_repo_path = os.path.join('./', 'repo')

repo = git.Repo.init(_repo_path)
repo.create_remote( 'origin', url )
repo.checkout('develop', b='build')
repo.git.push( 'origin','build' )

