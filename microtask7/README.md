
**1.Which are the common methods of the Graal backends?**<br />
  Common methods of Graal backends are: <br />
* fetch() :<br />
    syntax : ```fetch(self, category=CATEGORY_GRAAL, from_date=DEFAULT_DATETIME, to_date=DEFAULT_LAST_DATETIME,branches=None, latest_items=False)```<br /><br />
    Fetch commits and supports the inclusion of code analysis information. The method retrieves from a repository a list of commits. Commits are returned in the same order they were obtained.<br />
        :param category: the category of items to fetch<br />
        :param from_date: obtain commits newer than a specific date
            (inclusive)<br />
        :param to_date: obtain commits older than a specific date<br />
        :param branches: names of branches to fetch from (default: None)<br />
        :param latest_items: sync with the repository to fetch only the
            newest commits<br />
        :returns: a generator of commits. 
 <br />       
 
* metadata_category() :<br />
    syntax : ```metadata_category(item)```<br /><br />
    Extracts the category from a Graal item. This backend only generates one type of item which is 'commit'.<br />

* analyze() :<br />
    syntax : ```_analyze(self, commit)```<br /><br />
    Analyze a commit and the corresponding checkout version of the repository <br />
    :param commit: a Perceval commit item<br />
    
**2.List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).**<br />
  Git commands used by Graal are: <br />
  * worktree() :<br />
    syntax : ```worktree(self, worktreepath, branch=None)```<br />
    Create a working tree of the cloned repository with the active branch set to `branch`.The worktree is needed to perform "write" operations (e.g., git checkout), which cannot be done on a git bare repo.<br />
        :param worktreepath: the path where the working tree will be located<br />
        :param branch: the name of the branch. If None, the branch is set to `master`<br />
    
  * prune() :<br />
    syntax: ```prune(self)``` <br />
    Delete a working tree from disk.<br />
    :param worktreepath: directory where the working tree is located.<br />

  * checkout() :<br />
    syntax : ```checkout(self, hash)```<br />
    Checkout a Git repository at a given commit.<br />
    :param hash: the hash of a commit<br />