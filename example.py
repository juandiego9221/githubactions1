import os


def main():
    name = os.getenv("USERNAME")
    print(f"hello {name}")


if __name__ == "__main__":
    main()
