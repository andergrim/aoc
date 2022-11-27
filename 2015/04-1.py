import hashlib

secret_key = "ckczppom"
num = 0

while True:
    num += 1
    key = f"{secret_key}{num}".encode('utf-8')
    md5 = hashlib.md5(key).hexdigest()

    print(f"{num}:{md5}")

    if md5[0:5] == "00000":
        break

print(num)
