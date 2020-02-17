
def main():
    print("Name: ", __name__)
    print("Package: ", __package__)
    print("File: ", __file__)

if __name__ == "helper":
    print("Hello, from helper!")
    main()
