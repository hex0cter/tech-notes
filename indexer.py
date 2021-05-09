#!/usr/bin/env python

import os
from os.path import isdir, isfile, join


def index_file(file_name):
  # print("index_file", index_file)
  with open(file_name) as f:
    read_data = f.read()

  lines = read_data.split('\n')
  line_of_title = [line for line in lines if line.startswith("# ")]
  title = line_of_title[0][2:]
  if title.startswith("["):
    index = title.index("](")
    return title[1:index]
  else:
    return title


def index_dir(dir_name):
  # print("index_dir", dir_name)
  files = os.listdir(dir_name)

  titles = []
  for file in files:
    # print(">>>> file", file)
    file_path = join(dir_name, file)
    if isdir(file_path):
        items = index_dir(file_path)
        title = file_path.split('/')[-1].replace('-', ' ')
        titles.append({"path": file_path, "items": items, 'title': title})
    else:
        title = index_file(file_path)
        titles.append({"path": file_path, "title": title})

  return titles
  # key_name = dir_name.split('/')[-1].replace('-', ' ')
  # nice_key_name = ' '.join(elem.capitalize() for elem in key_name.split())
  # return {nice_key_name: titles, "dir_name": dir_name}


def create_index(titles, depth = 1):
  for title in titles:
      if 'items' in title:
          create_index(title['items'], depth=depth+1)
      else:
        print(f"{' '* depth}--[{title['title']}]({title['path']})")


if __name__ == "__main__":
    os.chdir("./src")
    titles = index_dir(".")
    # print(titles)
    create_index(titles)
