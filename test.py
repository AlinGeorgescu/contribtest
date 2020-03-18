#!/usr/bin/env python3

'''
    Test module for site generator
    To be run on Linux or Windows (diff -B)

    Author: Georgescu Alin-Andrei
'''

import os

def main():
    ''' Test 2 times on initial tests and one time on custom test '''
    os.system("rm -rf *.html")

    ################################## Test 1 #################################

    # Run initial tests with output in current folder
    os.system("./generate.py " + os.path.join("test", "source") + " .")

    for name in os.listdir("."):
        if ".html" in name:
            os.system("diff -B " + name + " " +
                      os.path.join("test", "expected_output", "eau_tests", name))
            os.system("rm " + name)

    ################################## Test 2 #################################

    # Run initial tests with output in output/tests/
    folder = os.path.join("output", "tests")
    os.system("./generate.py " + os.path.join("test", "source") + " " + folder)

    for name in os.listdir(folder):
        if ".html" in name:
            os.system("diff -B " + os.path.join(folder, name) + " " +
                      os.path.join("test", "expected_output", "eau_tests", name))

    os.system("rm -rf output")

    ################################## Test 3 #################################

    # To be hand reviewed
    os.system("./generate.py test/my_tests .")

if __name__ == "__main__":
    main()
