#!/usr/bin/python3
import argparse

import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--old", "-o", type=str, help="Old status")
    parser.add_argument("--new", "-n", type=str, help="New status")
    args = parser.parse_args()
    if args.old is None or args.new is None:
        print("Please provide both --old and --new arguments.")
        return 1
    old_status = pd.read_excel(args.old)
    new_status = pd.read_excel(args.new)
    return 0


if __name__ == "__main__":
    main()
