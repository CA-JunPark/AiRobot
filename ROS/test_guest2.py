from time import sleep
while True:
    with open ("/tmp/test", mode='r+') as f:
        print(f"read: {f.readline()}")