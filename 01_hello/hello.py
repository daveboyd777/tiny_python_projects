#!/usr/bin/env python3
"""
Say Hello

Usage: hello.py [-h] [-n name]

Dave Boyd
2024-03-06

"""
import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        default="World",
        help="usage: hello.py [-h] [-n name]",
    )
    return parser.parse_args()


def main():
    """Execute the main function."""
    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == "__main__":
    main()
