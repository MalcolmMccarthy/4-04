# made by malcolm
#in october 2017
#for ics3u
#converts level to percentage


def convert_level_to_percentage():
    #input
    level = raw_input("Enter level: ")
    #process
    if level == "4+":
        level = "95"
        return level
    elif level == "4":
        level == "90"
        return level
    elif level == "4-":
        level = "85"
        return level
    elif level == "3+":
        level = "77"
        return level
    elif level == "3":
        level = "75"
        return level
    elif level == "3-":
        level = "72"
        return level
    elif level == "2+":
        level = "67"
        return level
    elif level == "2":
        level == "65"
        return level
    elif level == "2-":
        level = "60"
        return level
    elif level == "1+":
        level = "58"
        return level
    elif level == "1":
        level == "55"
        return level
    elif level == "1-":
        level = "50"
        return level
    elif level == "R":
        level = "30"
        return level
    elif level == "NE":
        level = "0"
        return level
    else:
        print('enter a valid level')
        
        # output
percentage = convert_level_to_percentage()
print percentage
