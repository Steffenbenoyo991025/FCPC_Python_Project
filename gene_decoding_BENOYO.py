name = input ("Enter your name:")
name_changer = ""

for x in range (len (name)):
    char = name [x]

    if char == "A":
        name_changer + = "B"
    elif char == "B":
        name_changer + = "C"
    elif char == "C":
        name_changer + = "D"
    elif char == "D":
        name_changer + = "E"
    elif char == "E":
        name_changer + = "F"
    elif char == "F":
        name_changer + = "G"
    elif char == "G":
        name_changer + = "H"
    elif char == "H":
        name_changer + = "I"
    elif char == "I":
        name_changer + = "J"
    elif char == "J":
        name_changer + = "K"
    elif char == "K":
        name_changer + = "L"
    elif char == "L":
        name_changer + = "M"
    elif char == "M":
        name_changer + = "N"
    elif char == "N":
        name_changer + = "O"
    elif char == "O":
        name_changer + = "P"
    elif char == "P":
        name_changer + = "Q"
    elif char == "Q":
        name_changer + = "R"
    elif char == "R":
        name_changer + = "S"
    elif char == "S":
        name_changer + = "T"
    elif char == "T":
        name_changer + = "U"
    elif char == "U":
        name_changer + = "V"
    elif char == "V":
        name_changer + = "W"
    elif char == "W":
        name_changer + = "X"
    elif char == "X":
        name_changer + = "Y"
    elif char == "Y":
        name_changer + = "Z"
    elif char == "Z":
        name_changer + = "A"
    else:
        name_changer + = char

print (name_changer)
