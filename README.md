# GSOC-Chaoss
This repo is to show my work that I have done on Idea: [Support of Source Code Related Metrics](https://github.com/chaoss/grimoirelab/issues/182).   

My Solution for the Microtasks:

**Microtask 1:**

For mirotask 1, I have installed the perceval package on PyCharm. Now I can run perceval commands form PyCharm.

![pic](Microtask1.png)

**Microtask 2:**

For Microtask 2, I have made the python script [Microtask 2](Microtask2.py). In this I have executed the Perceval using GitHub backend. 
The code on execution requires two arguments 1. Github repo as "owner/repo" 2. Github auth token (optinal argument).
The script on execution gives output the usernames of all the persons who made commit on the repo.

Example: python perceval_username.py -r owner/repo -t XXXX

Output: 
![output](Output2.png)


**Microtask 3: **

**Microtask 4: **

For Microtask 4, I have made the python script [Microtask 4](Microtask4.py). This script finds if an given GitHub repo is on the Showheritage or not and also shows the date of last visit.

The script on execution first takes github repo url as an argument, then it uses the Showheritage API to check if repo is there or not. For this request module is used which makes an GET request on the API. The endpoint used on Showheitage API for finding repo is: "/api/1/origin/(origin_type)/url/(origin_url)/". After getting the reponse, we check is an stautus code 200 is retreived or not if not then repo is not present at showheritage otherwise we now finds its last visit. In the response got earlier we get an entry of "origin_visits_url" which has all the entries of the date when it has been visited. Now we again make an get request on the showheritage API by using the "origin_visits_url" and from the response we jsut show the first entry which is the latest visit date and time.

Base API url: "https://archive.softwareheritage.org/"
Finding repo url (origin endpoint): "https://archive.softwareheritage.org"+"/api/1/origin/(origin_type)/url/(origin_url)/"
Finding visits url (visit url) : "https://archive.softwareheritage.org" + "origin_visits_url"

Output: 
![pic](Output4.png)


**Microtask 5:**

For mirotask 5, I have installed the graal package on PyCharm. Now I can run graal commands form PyCharm.

![pic](Microtask5.png)

**Microtask 6: **

For Microtask 6, I have made the python script [Microtask 6](Microtask6.py). In this I have executed Graal using Cocom backend. 
The code on execution requires two arguments 1. Github repo as "owner/repo" 2. Github auth token (optinal argument).
The script on execution gives output the usernames of all the persons who made commit on the repo.

Example: python perceval_username.py -r owner/repo -t XXXX

Output: 
![output](output2.png)


**Microtask 8: **


