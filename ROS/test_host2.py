from time import sleep

i = 0
while True:
    with open("/tmp/test", mode='r+') as f:
        print(f"wrote {i} to /tmp/test")
        f.write(f"{i}\n")
    i += 1