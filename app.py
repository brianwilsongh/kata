import argparse
import unittest

class App:
    
    def __init__(self):
        print("App initiated!")

    def run(self):
        print("Running Application!")
        #in here we will initiate required object, accept scanned items, display total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-V", "--verbose", help="Produce detailed output", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print("Produce verbose output")
    print("Starting app.py!")
    app = App()
    app.run()