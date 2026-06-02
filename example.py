import os


def main():
    name = os.getenv("USERNAME")
    print("-----------------")
    print(f"hello {name}")
    print("-----------------")


if __name__ == "__main__":
    main()
