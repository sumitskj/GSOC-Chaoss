# imports
import requests
import argparse
import json

# Parse comand line arguments
parser = argparse.ArgumentParser("Parser for taking arguments")

#adding arguments
parser.add_argument("-u", "--url", help="enter URL of repo")

args = parser.parse_args()

# Setting URLS
api_url = "https://archive.softwareheritage.org/api/1"
searchUrl = api_url + "/origin/git/url/"
baseUrl = "https://archive.softwareheritage.org/"

url = searchUrl + args.url
#print(url)

# getting response from API
response = requests.get(url)
#print(response)

data = response.json()
#print(data['origin_visits_url'])

# checking if repo found or not
if response.status_code == 200:
    print("Repo: " + args.url + " found.")

    # Finding the latest visit
    visitUrl = baseUrl + data['origin_visits_url']
    visit = requests.get(visitUrl)  # visit is an array
    visit.encoding
    v = visit.text  # converting visit to a string and storing it in v
    json_visit = json.loads(v) # coverting it to json
    print("Recent visit date: "+json_visit[0]['date'])  # fetching ans printing latest date
else:
    print("Your Repo didn't found")
