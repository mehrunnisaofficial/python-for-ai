# Building our own library

# we need to first create the structure

def main():
    hello("world")
    goodbye("World")


def hello(name):
    print(f"hello {name}")

def goodbye(name):
    print(f"Goodbye {name}")


if __name__ == "__main__":
    main()