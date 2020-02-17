import helper

def main():
    print("Name: ", __name__)
    print("Package: ", __package__)
    print("File: ", __file__)
    helper.main()

if __name__ == "__main__":
    print("Hello, World!")
    main()
