
level = "1"
for line in open("reddit.txt","r"):
    line_args = line.split()
    if len(line_args) >= 4:
        if line_args[1] == level:
            print " ".join(line_args)
