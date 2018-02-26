from contextlib import contextmanager


@contextmanager #데코레이터로 함수 수식
def open3(path):
    print("opening file...")
    file=open(path)
    try:
        print("yielding file...")
        yield file
    finally:
        print("closing file...")
        file.close()

with open3("test.txt") as file:
    s=file.read()
    print(s)