import json
import sys
import re 

def argsToDict(argv):
    if len(argv) > 3:
        expr = argv[3]
    else:
        expr = input("Please, input regexp: ")
    
    dict = {
        "Name" : argv[0],
        "Input" : argv[1],
        "Output" : argv[2],
        "Expression": expr
    }
    return dict

def main(argv):
    args = argsToDict(argv)
    print(args)
    
    with open(args['Input'], 'r') as file:
        text = file.read()
    
    pattern = re.compile(args["Expression"], flags=re.MULTILINE)
    output = pattern.findall(text)
    
    json_string = json.dumps(output)
    print(json_string)
    with open(args["Output"], "w") as file:
        file.write(json_string)
    
    print("Complete :)")
    
if __name__ == "__main__":
    # Have name of program && name of input file && name of output file && regular expression
    if len(sys.argv) >= 3:
        main(sys.argv)
    else:
        print("Bad count of args!")