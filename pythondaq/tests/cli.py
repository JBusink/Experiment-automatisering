# cli.py
import sys
args = sys.argv
print(args)
if args[1] == "test":
    print(f"This is a test: {args[2]}")
else:
    print(f"CommandNotFoundError: No command '{args[1]}'.")