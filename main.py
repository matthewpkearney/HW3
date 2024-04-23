import hashlib
import csv

r = open('rockyou2000.txt', 'r', encoding='utf-8')
passwords = r.read().splitlines()
r.close()

with open("leakedhashes.txt") as load_file:
    reader = csv.reader(load_file, delimiter=" ")
    found_hashes = [tuple(row) for row in reader]

hashes= []
for i in found_hashes:
    hashes.append(i[-1])



with open("rockyou2000md5.txt") as load_file:
    reader = csv.reader(load_file, delimiter=" ")
    md5s = [tuple(row) for row in reader]

md5_hash= []
for i in md5s:
    md5_hash.append(i[-1])



with open("rockyou2000sha256.txt") as load_file:
    reader = csv.reader(load_file, delimiter=" ")
    shas = [tuple(row) for row in reader]

sha_hash= []
for i in shas:
    sha_hash.append(i[-1])



it = 0
matches =0
for i, j, k in zip(md5_hash, sha_hash, hashes):
    # print(i, j, k)
    print(i, k)
    print(j, k)
    if (i == k):
        print(f"md5 hash match at:\n\ti={it}for:\n\thash match={hashes[it]}\n\tpassword={passwords[it]}")
        matches=matches+1
    if (j == k):
        print(f"sha256 hash match at:\n\ti={it}for:\n\thash match={hashes[it]}\n\tpassword={passwords[it]}")
        matches =matches +1
print(matches)
