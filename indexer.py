#!/usr/bin/env python

import os
from os.path import isdir, join


def index_file(file_name):
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
      if file == 'SUMMARY.md' or file == 'index.md':
        continue
      title = index_file(file_path)
      titles.append({"path": file_path, "title": title})

  return titles


def create_index(file, titles, depth=0, current_dir=''):
  for title in titles:
    displayed_title = title['title'].capitalize()
    if current_dir:
      displayed_path = title['path'].replace(current_dir, '.')
    else:
      displayed_path = title['path']
    if 'items' in title:
      line = f"{' ' * depth * 2}- [{displayed_title}]({displayed_path}/index.md)"
      file.write(f"{line}\n")

      subfolder_file = open(f"{title['path']}/index.md", "w")
      subfolder_file.write(f"# {displayed_title}\n")
      create_index(subfolder_file, title['items'], current_dir=title['path'])
      subfolder_file.close()

      create_index(file, title['items'], depth=depth + 1)
    else:
      line = f"{' ' * depth * 2}- [{displayed_title}]({displayed_path})"
      file.write(f"{line}\n")


if __name__ == "__main__":
  os.chdir("./src")
  titles = index_dir(".")
  first_page_index = next((index for (index, d) in enumerate(titles) if d["path"] == "./README.md"), None)
  first_page = titles.pop(first_page_index)
  titles.insert(0, first_page)

  file = open("SUMMARY.md", "w")
  file.write("# Index\n")
  create_index(file, titles)
  file.close()
