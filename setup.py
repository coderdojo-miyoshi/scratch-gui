import os
import git
for env in os.environ:
    print(env)
print('--------------------')
print(os.environ.get('EV'))
print(os.environ.get('EX'))

print("setup")
