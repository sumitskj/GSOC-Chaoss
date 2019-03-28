
1.Which are the common methods of the Graal backends?<br />
  Common methods of Graal backends are fetch(), metadata_category(), analyze(), etc.<br />

2.List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).<br />
  Git commands used by Graal are: <br />
  * worktree() :<br />
    syntax : worktree(self, worktreepath, branch=None):<br />
    Create a working tree of the cloned repository with the active branch set to `branch`.<br />
        :param worktreepath: the path where the working tree will be located<br />
        :param branch: the name of the branch. If None, the branch is set to `master`<br />
    
  * prune() :<br />
    syntax: prune(self): <br />
    Delete a working tree from disk.<br />
    :param worktreepath: directory where the working tree is located.<br />

  * checkout() :<br />
    syntax : checkout(self, hash):<br />
    Checkout a Git repository at a given commit.<br />
    :param hash: the hash of a commit<br />