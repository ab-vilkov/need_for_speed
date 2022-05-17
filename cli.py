import argparse
import os.path
import hashlib
import time
import typing
from multiprocessing.pool import ThreadPool
import requests


def url_fetch(url_tuple : typing.Tuple):
    dir, url = url_tuple
    # request = requests.Request(
    #         url,
    #         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    #     )

    response = requests.get(url)
    if response.status_code == 200:
        filename, file_ext = os.path.splitext(url)
        with open(root + dir + "/" + str(hashlib.md5(filename.encode("utf-8")).hexdigest()) + file_ext, "wb+") as file:
            result = response.content
            if pp:
               sum(x ** 2 for x in result)
            file.write(response.content)


parser_flags_cli = argparse.ArgumentParser(description="This")
parser_flags_cli.add_argument("-pp", "--processing", type=bool, default=False, help="post-processing")
parser_flags_cli.add_argument("-d", "--dir", default="defaultFolder", type=str, help="results folder")
parser_flags_cli.add_argument("-p", "--path", default="./links.txt", type=str, help="file name with links")
parser_flags_cli.add_argument("-w", "--workers", default=1, type=int, help="number of workers")
root = "./"
args = parser_flags_cli.parse_args()
dir = args.dir
path = args.path
workers = args.workers
pp = args.processing
if dir == "defaultFolder":
    dir = dir + "_" + str(workers) + "_1"
    while os.path.isdir(root + dir):
        dirSplit = list(dir.split("_"))
        dirSplit[2] = str(int(dirSplit[2]) + 1)
        dir = "_".join(dirSplit)
    os.mkdir(root + dir)
else:
    os.mkdir(dir)

links = []

with open(path, "r") as links_file:
    for line in links_file.readlines():
        links.append((dir, line.strip()))

start = time.time()
results = ThreadPool(workers).imap_unordered(url_fetch, links)
for now in results:
    continue

with open(root + dir + "/result.txt", "w+") as f:
    f.write(f"{time.time() - start}")

