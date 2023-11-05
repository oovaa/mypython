import argparse as ap

# create_files.py

with open("file1.txt", "w") as file1:
    file1.write("This is the content of file1.")

with open("file2.txt", "w") as file2:
    file2.write("Content of file2 is different.\nIt has multiple lines.")


parser = ap.ArgumentParser(prog="top", description="Show top lines from each file")
parser.add_argument("names", nargs="+")
parser.add_argument("-l", "--lines", type=int, default=10)
args = parser.parse_args()
print(args)
