fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    fh=fh.upper()
    print(fh)