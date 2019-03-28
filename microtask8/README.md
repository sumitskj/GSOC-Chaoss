
For Microtask 8, I have made the python script [Microtask 8](Microtask8.py). This script takes the repo url and a commit SHA as inputs, then it clones that repo if it isn't there, then it checkouts to the given commit SHA and then finally performs an flake8 on that.

In the script, we first take the url and commit SHA as arguments, then we have to clone the repo which we will do by using the "git clone --mirror" command through the os moodule. Now to make a checkout to the given commit we have, first we have to create an GraalRepository object which takes parameters as repo url and cloned repo path and then we need to create an worktree for our repo about the commits and have to update worktree path. Then using this object we call GraalRepository checkout() method  which will checkout us to the certain commit. Then using the os module we will execute an flake8 on the repo.

Example: python checkout.py -u "url" -c "commit SHA"

Output:

![pic](Output8.png)
