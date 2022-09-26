import turtle
import re
import svgTurtle

def separate_commands(string):
    temp = string
    setrange = len(string)
    commands = []
    lastcommand = 0;
    for i in range(1,setrange):
        char = temp[i:i+1]
        if re.search("M|m|L|l|H|h|V|v|C|c|S|s|Q|q|T|t|A|a", temp[i:i+1]):
            commands.append([string[lastcommand:lastcommand+1],string[lastcommand+2:i]])
            lastcommand = i
        elif re.search("Z|z", temp[i:i+1]):
            commands.append([char,"0"])
    #print("COMMANDS")
    #for command in commands: print(command)
    return commands

def separate_params(commandlist):
    commands = []
    for i in commandlist:
        currentparams = i[1]
        currentparams = re.sub(",", " ", currentparams)
        currentparams = re.sub("-"," -", currentparams)
        #print("replaced:",currentparams)
        split = re.split(" ", currentparams)
        paramlist = []
        for s in range(len(split)):
            paramlist.append(float(split[s]))
        commands.append([i[0],paramlist])
        
    #for command in commands: print(command)
    return commands

def separate_lines(string):
    return string.split("\n")

### above is all file parsing

######MAIN######
file = open("wandverts.txt", "r")
lines = list((separate_lines(file.read())))

commandlist = separate_commands("M4614.5,1170.5l-546.1-546.1l728.1-728.1l728.1-728.1l539.2,539.2c298.1,298.1,541.5,557.4,541.5,575.6c-2.3,50.1-266.2,1137.6-279.9,1153.6c-18.2,15.9-1064.8,277.6-1119.5,279.9C5176.5,1716.5,4969.5,1525.4,4614.5,1170.5z")
print("separate_params:")
commandlist = separate_params(commandlist)
for command in commandlist: print(command)

#begin drawing :
xyturd = turtle.Turtle()


screen = turtle.Screen()
turdie = svgTurtle.svgTurtle(commandlist)
turdie.render(xyturd)
