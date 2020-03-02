#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Jonathan Jones"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(directory):
    abs_path = os.path.abspath(directory)
    dir_files = os.listdir(directory)
    special_paths = []
    for file in dir_files:
        match = re.search(r'[\w]*\_{2}[\w.-]+\_{2}\.[\w]+', file)
        if match:
            abs_path = abs_path + "/" + str(match.group())
            special_paths.append(abs_path)
            print(abs_path)
            abs_path = os.path.abspath(directory)
    return special_paths


def copy_to(paths, directory):
    for file in paths:
        shutil.copy(file, directory)


def zip_to(paths, zippath):
    for file in paths:
        try:
            subprocess.call(["zip", "-j", zippath, file])
        except IOError:
            print("Error on file" + file)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument(
        'fromdir', help="directory to search for special files"
        )
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.
    # If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions

    if os.path.exists(args.fromdir):
        paths = get_special_paths(args.fromdir)
    else:
        print("Ye directory does not exist")

    if args.todir and args.fromdir:
        # print("To thy directory")
        if os.path.exists(args.todir):
            # print("Ye path does exist")
            print("copying files to directory ")
            copy_to(paths, args.todir)
        else:
            # print("path is nonexistent")
            print("Ye directory does not exist")
            print("Lets make it!")
            os.makedirs(args.todir)
            print("Directory made, now lets copy files to directory")
            copy_to(paths, args.todir)
    if args.tozip:
        # print("Ye are zipping")
        output = "zip -j " + args.tozip
        for file in paths:
            output += " " + file
        print("Command I'm going to do:")
        print(output + "\n")
        zip_to(paths, args.tozip)


if __name__ == "__main__":
    main()