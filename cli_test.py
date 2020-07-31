import argparse
import os
import sys

# creater a parser
my_parser = argparse.ArgumentParser(description="List the content of a folder")

# add arguments to the parser objecr named my_parser
my_parser.add_argument('Path',
                        metavar='path',
                        type=str,
                        help='the path to list')

# execute the parse_args() methods
# which creates a Namespace object
# the Namespace object hold attributes and returns them
# parse_args() takes argument strings into objects and assigns them as attributes of a namespace object
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("The specified path does not exist")

sys.stdout.write('\n'.join(os.listdir(input_path)))
