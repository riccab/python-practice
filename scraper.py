#! /usr/bin/env python

from lxml import html
import requests
import yaml

with open("infra.yml", "r") as f:
  doc = yaml.load(f)
txt = doc["components"]

for line in txt:

  for x in line.keys():
    if line[x] == "bitbucket":
      if 'version' in line:
        componentV = line.get("version", "none")
        print(componentV)

page = requests.get('https://confluence.atlassian.com/bitbucket/bitbucket-cloud-documentation-221448814.html')
tree = html.fromstring(page.content)
bitbucketVersion = tree.xpath('//li[@class="current-version"]/text()')

if componentV != bitbucketVersion:
  print("A new version of Bitbucket is available", bitbucketVersion)

