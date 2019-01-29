import os
import git
#for env in os.environ:
#    print(env)

travis_repo_slug=os.environ.get('TRAVIS_REPO_SLUG')
gh_token=os.environ.get('GH_TOKEN')
url="https://{0}@github.com/{1}.git".format(gh_token,travis_repo_slug)
_repo_path = os.path.join('./', 'repo')
repo = git.Repo.clone_from(url, _repo_path,branch='develop')
repo.git.checkout('-b', 'build')
repo.git.push( 'origin','build' )
print(os.listdir(_repo_path))
