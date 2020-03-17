import sys

print('Number of arguments for python command is ', len(sys.argv))
for i,arg in enumerate(sys.argv):
    print("The NO.", i+1, " argument for command 'python' is ", arg)
