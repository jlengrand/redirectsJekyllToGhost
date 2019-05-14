import os
import json

posts_directory = "_posts"
pattern = "title: "
permanent = "true"

def extractDateAndTitle(post):
    strips = os.path.splitext(post)[0].split("-")
    return (strips[0:2], "-".join(strips[3:]))

def makeJekyllUrl(post):
    vals = extractDateAndTitle(post)
    return "/" + "/".join((vals[0] + [vals[1]]))

def grabTitleFromPost(post):
    with open(posts_directory + "/" + post, 'r', encoding='utf-8') as postFile :
        for line in postFile:
            line = line.rstrip()
            if pattern in line:
                return line

def cleanGhostTitle(title):
    toRemove="()!,'–:./"
    for char in toRemove:
        title = title.replace(char, " ")
    return title.lower()

def makeGhostUrl(post):
    title = grabTitleFromPost(post).split(pattern)[1]
    cleanTitle = cleanGhostTitle(title)
    superCleanTitle = " ".join(cleanTitle.split())
    return "/" + "-".join(superCleanTitle.split(" "))

posts = [f for f in os.listdir(posts_directory) if os.path.isfile(os.path.join(posts_directory, f))]
# print(posts)


redirects = []
for post in posts:
    redirects.append({
        "from" : makeJekyllUrl(post),
        "to": makeGhostUrl(post),
        "permanent" : permanent
    })

with open('redirects.json', 'w') as outfile:  
    json.dump(redirects, outfile)
