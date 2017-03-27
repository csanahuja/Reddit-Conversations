"""
Usefull to debug if we have repeated comments
"""

def debug1():
    level = "1"
    for line in open("reddit.txt","r"):
        line_args = line.split()
        if len(line_args) >= 4:
            if line_args[1] == level:
                print " ".join(line_args)

def debug2():
    lineFound = False
    index = 0
    for line2 in open("reddit2.txt","r"):
        lineFound = False
        index += 1
        for line in open("reddit.txt","r"):
            if line2.split()[4:] == line.split()[4:]:
                lineFound = True
        if lineFound == False:
            print "Line " + str(index) + " not found"
        else:
            print "Line " + str(index) + " found"

if __name__ == '__main__' :
    #debug1()
    #debug2()
