"""
Usefull to debug if we have repeated comments
"""
#Every line on file2 it is present on file1
def debug1():
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

#Every line on file it is not repeated
def debug2():
    repeatedLine = False
    index = 0
    index2 = 0
    for line in open("reddit.txt","r"):
        repeatedLine = False
        index += 1
        index2 = 0
        for line2 in open("reddit.txt","r"):
            index2 += 1
            if line2.split()[4:] == line.split()[4:]:
                repeatedLine = True
        if repeatedLine == True:
            print "Line " + str(index) + " and Line " + str(index2) + " repeated"


if __name__ == '__main__' :
    #debug1()
    #debug2()
