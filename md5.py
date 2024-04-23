import hashlib
r = open('rockyou2000.txt', 'r', encoding='utf-8')
passwords = r.read().splitlines()
r.close()

w = open('rockyou2000md5.txt', 'w')
for password in passwords:
    x = password.encode()
    hash = hashlib.md5(x).hexdigest()
    w.write(f"{password} {hash}\n")

w.close()
