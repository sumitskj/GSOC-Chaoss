
1.What is the meaning of the JSON attribute 'timestamp'?<br />
  The attribute 'timestamp' gives the date and time of the moment when the code got executed and gave us the information back. Timestamp is in 'epoch' format which can be converted into date and time.<br />

2.What is the meaning of the JSON attribute 'updated_on'?<br />
  This attribute shows the date and time of when was the repo got last updated.<br />

3.What is the meaning of the JSON attribute 'origin'?<br />
  It shows the link of from where the information of repo is fetched. It usually shows the git repo link.<br />
<br />
4.What is the meaning of the JSON attribute 'category'?
  It shows what type of operation was performed, usually it is a commit operation.<br />

5.What is the meaning of the JSON attribute 'uuid'?<br />
  It is a 128 bit unique number given to that operation. It is uaually universally unique.<br />

6.Which are the common methods of the Perceval backends?<br />
  Common methods of perceval backends are fetch(), fetch_items(), has_archiving(), has_resuming(), metadata_id(), metadata_category(), etc.<br />

7.List and explain at least 3 Git commands used by the Perceval backend (you can rely on the Git documentation)<br />
  Git commands used by Perceval backend are :<br />
  * clone() :<br />
    syntax : clone(cls, uri, dirpath)<br />
    This method clones the repo. Make a bare copy of the repository stored in `uri` into `dirpath`.
    The repository would be either local or remote.<br />
        :param uri: URI of the repository<br />
        :param dirtpath: directory where the repository will be cloned<br />
        :returns: a `GitRepository` class having cloned the repository<br />

  * count_objects():<br />
    syntax : count_objects(self)<br />
    Count the objects of a repository.
    The method returns the total number of objects (packed and unpacked) available on the repository<br />

  * update() :<br />
    syntax : update(self)<br />
    Update repository from its remote. Calling this method, the repository will be synchronized with the remote repository using 'fetch' command for 'heads' refs. Any commit stored in the local copy will be removed; refs will be overwritten.<br />

  * sync() : <br />
    syntax : sync(self)<br />
    Keep the repository in sync. This method will synchronize the repository with its 'origin', fetching newest objects and updating references. It uses low level commands which allow to keep track of which things    have changed in the repository. The method also returns a list of hashes related to the new commits fetched during the process. It returns a list of new commits<br />