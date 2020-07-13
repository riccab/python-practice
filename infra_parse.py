#! /usr/bin/env python

import yaml

with open("infra.yml", "r") as f:
  doc = yaml.load(f)
txt_components = doc["components"]

for line in txt_components:

  for x in line.keys():
    if line[x] == "bitbucket":
      imageV = line
      if 'version' in imageV:
        componentV = imageV.get("version", "none")
        print(componentV)

txt_images = doc["images"]

for line in txt_images:

  for x in line.keys():
    if line[x] == "bitbucket":
      imageV = line
      if 'tag' in imageV:
        tagV = imageV.get("tag", "none")
        print(tagV)
