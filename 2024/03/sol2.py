import os

def cleaner(in_file):
    clean_file = []
    
    for line in in_file:
        # Initialize empty result for this line
        clean_line = ""
        i = 0
        
        while i < len(line):
            # Look for do() and don't() instructions
            if line[i:i+4] == "do()":
                clean_line += "do()"
                i += 4
                continue
            elif line[i:i+7] == "don't()":
                clean_line += "don't()"
                i += 7
                continue
            # Look for "mul" followed by proper format
            if line[i:i+3] == "mul" and i+3 < len(line):
                if line[i+3] == "(":
                    # Try to extract numbers between parentheses
                    j = i + 4
                    num1 = ""
                    while j < len(line) and line[j].isdigit() and len(num1) < 3:
                        num1 += line[j]
                        j += 1
                        
                    if j < len(line) and line[j] == "," and num1 != "":
                        j += 1
                        num2 = ""
                        while j < len(line) and line[j].isdigit() and len(num2) < 3:
                            num2 += line[j]
                            j += 1
                            
                        if j < len(line) and line[j] == ")" and num2 != "":
                            # Valid mul instruction found
                            clean_line += f"mul({num1},{num2})"
                            i = j + 1
                            continue
            
            i += 1
            
        if clean_line:
            clean_file.append(clean_line)
    
    return clean_file

def cleaner2(line):
    clean_line = ""
    i = 0
    enabled = True
    
    while i < len(line):
        # Check for don't() and do() instructions
        if line[i:i+7] == "don't()":
            enabled = False
            i += 7
            continue
        elif line[i:i+4] == "do()":
            enabled = True
            i += 4
            continue
            
        # Only process mul instructions if enabled
        if enabled and line[i:i+3] == "mul" and i+3 < len(line):
            if line[i+3] == "(":
                # Try to extract numbers between parentheses
                j = i + 4
                num1 = ""
                while j < len(line) and line[j].isdigit() and len(num1) < 3:
                    num1 += line[j]
                    j += 1
                    
                if j < len(line) and line[j] == "," and num1 != "":
                    j += 1
                    num2 = ""
                    while j < len(line) and line[j].isdigit() and len(num2) < 3:
                        num2 += line[j]
                        j += 1
                        
                    if j < len(line) and line[j] == ")" and num2 != "":
                        # Valid mul instruction found
                        clean_line += f"mul({num1},{num2})"
                        i = j + 1
                        continue
        
        i += 1
        
    return clean_line




def calculator(line):
    total = 0
    i = 0
    
    while i < len(line):
        if line[i:i+3] == "mul":
            # Find the numbers between parentheses
            start = line.find("(", i) + 1
            end = line.find(")", i)
            if start > 0 and end > 0:
                nums = line[start:end].split(",")
                # Multiply the two numbers and add to total
                total += int(nums[0]) * int(nums[1])
                i = end + 1
                continue
        i += 1
        
    return total




# main
if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    # input = "input_ex2"
    input = "input"
    
    sol = 0
    
    with open(dir + "\\" + input, "r") as in_file:
        clean_file = cleaner(in_file)

    double_clean = []

    for line in clean_file:
        double_clean.append(cleaner2(line))

    for line in double_clean:
        sol += calculator(line) 

    print("Part 2: " + str(sol))