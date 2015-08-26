import sys, string, re

# 3 command line arguments
file = sys.argv[1]          # File name
target = sys.argv[2]        # Target word
window = int(sys.argv[3])   # How many surrounding words you want to return

text = open(file).read() # Opens the file and reads it into a new variable

tokens = text.split() # split on whitespace
keyword = re.compile(target, re.IGNORECASE)

for index in range( len(tokens) ):
    if keyword.match( tokens[index] ):
        start = max(0, index-window)
        finish = min(len(tokens), index+window+1)
        lhs = string.join( tokens[start:index] )
        rhs = string.join( tokens[index+1:finish] )
        print "%s [%s] %s" % (lhs, tokens[index], rhs)
