import sys

def checkForVariables(input):
    '''Check for empty lines and comments'''
    if "\n" == input:
        return False
    elif "=" not in input:
        return False
    else:
        return True

def extractValues(inputDictionary, input):
    variable = input.split("<")[1].split(">")[0]
    try:
        result = inputDictionary[variable]
        return input.replace(input[input.index("<"):input.index(">")+1], result)
    except KeyError:
        print("ERROR: No value found for key {}!".format(variable))
        exit(1)

def readIn(filename):
    try:
        fileHandleIn = open(filename, "r")
        output = fileHandleIn.readlines()
        fileHandleIn.close()
        return output
    except(FileNotFoundError, PermissionError):
        print("ERROR: Input file {} does not exist, or you do not have permission to access it!".format(filename))
        exit(1)

def writeEnv(inputDictionary, filename, mode):
    try:
        fileHandleOut = open(filename, mode)
        for i, j in inputDictionary.items():
            print("{}={}".format(i, j), file=fileHandleOut)
        fileHandleOut.close()
    except PermissionError:
        print("ERROR: You do not have permission to write to {}!".format(filename))
        exit(1)

def writeOut(inputDictionary, filename):
    try:
        writeEnv(inputDictionary, filename, "x")
    except FileExistsError:
        userInput = input("ERROR: Target output file {} exists!\nOverwrite? (Y/N)\n".format(filename))
        if userInput.lower() == "y":
            writeEnv(inputDictionary, filename, "w")
        else:
            exit(1)

def processArguments():
    argumentsList = sys.argv
    if len(argumentsList) != 3:
        print("ERROR: Invalid arguments detected!")
        exit(1)
    return argumentsList

def iterate(contents):
    variables = {}
    for i in contents:
        if checkForVariables(i):
            splitVals = i.split("=")
            if "<" in splitVals[1]:
                splitVals[1] = extractValues(variables, splitVals[1])
            variables[splitVals[0]] = splitVals[1].strip("\n")
    return variables

def main():
    arguments = processArguments()
    contents = readIn(arguments[1])
    variables = iterate(contents)
    writeOut(variables, arguments[2])

if __name__ == "__main__":
    main()