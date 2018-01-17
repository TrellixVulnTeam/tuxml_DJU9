#!/usr/bin/python3

import os
from sys import argv
import argparse

# We define the function use in the script


def dockerBuild():
    print("Update of the docker image tuxml/tuxmldebian")
    # Build the choosen docker image
    str1 = 'sudo docker build -t tuxml/tuxmldebian .'
    os.system(str1)


def dockerPush():
    print("Push of the image on the distant repository")
    # Push of the docker image on docker hub
    strpush = 'sudo docker push tuxml/tuxmldebian'
    rstrpush = os.system(strpush)
    # If needed, login to the repository
    if rstrpush == 256:
        str3 = 'sudo docker login'
        os.system(str3)

# Start of the script


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="test", formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-b', '--build', help="Folder where is locate a valid docker file use to build a docker image, default is  [.] ", default=".")
    parser.add_argument('-g', '--generate', help="Image use to generate a docker file")
    parser.add_argument('-dep', '--dependences', help="Dependences you want to add to your docker image when you generate your dockerfile")

args = parser.parse_args()
