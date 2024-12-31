def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def helloWorld():
    print("Hello world")

helloWorld()