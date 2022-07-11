# Scientific Computing with Python
# Arithmetic Formatter
# arithmetic_arranger.py
import re

def arithmetic_arranger(param1, *param2):
    param1 = str(param1)
    param1 = param1.replace("[", "").replace("]", "").replace("\'", "")
    print("\t" + param1 + "\n")
    param1split = param1.split(",")
    param1A = []

    errcount = 0

    if (len(param1split) <= 4):

        for i in range(len(param1split)):
            param1Str = str(param1split[i])

            if (param1Str.find("+") > 0):
                param1Num = param1Str.split("+")
                param1Sign = "+"
                for j in range(len(param1Num)):
                    if (checkNum(param1Num[0]) == 0) or (checkNum(param1Num[1]) == 0):
                        print("Error: Numbers must only contain digits.\n")
                        errcount = 1
                        break
                    if (maxDigit(param1Num[0]) > 4) or (maxDigit(param1Num[1]) > 4):
                        print("Error: Numbers cannot be more than four digits.\n")
                        errcount = 1
                        break

            elif  (param1Str.find("-") > 0):
                param1Num = param1Str.split("-")
                param1Sign = "-"
                for j in range(len(param1Num)):
                    if (checkNum(param1Num[0]) == 0) or (checkNum(param1Num[1]) == 0):
                        print("Error: Numbers must only contain digits.\n")
                        errcount = 1
                        break
                    if (maxDigit(param1Num[0]) > 4) or (maxDigit(param1Num[1]) > 4):
                        print("Error: Numbers cannot be more than four digits.\n")
                        errcount = 1
                        break

            elif (param1Str.find("+") < 0 ) and ((param1Str.find("-") < 0 )):
                print("Error: Operator must be '+' or '-'..\n")
                errcount = 1
                break

            if errcount == 0:
                if param1Sign == "+":
                    param1Sum = int(param1Num[0]) + int(param1Num[1])
                else:
                    param1Sum = int(param1Num[0]) - int(param1Num[1])
                param1len = maxLen(trim(str(param1Num[0])), trim(str(param1Num[1])), trim(str(param1Sum)))
                param1Arr = [param1Sign, int(param1Num[0]), int(param1Num[1]), int(param1Sum), param1len+2]
                param1A.append(param1Arr)



    elif(len(param1split) > 4):
        print("Error: Too many problems.\n")
        errcount = 1

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    if errcount == 0:

        for i in range(len(param1A)):
            line1 = line1 + str(addLead(param1A[i][1],  param1A[i][4])) + "  "
            line2 = line2 + param1A[i][0] + str(addLead(param1A[i][2],  param1A[i][4]-1)) + "  "
            line3 = line3 + addDot(param1A[i][4]) + "  "
            line4 = line4 + addLead(param1A[i][3], param1A[i][4]) + "  "
        print(line1)
        print(line2)
        print(line3)

        if (bool(param2) == True):
            print(line4 + "\n")

def maxDigit(str1):
    maxD = len(trim(str1))
    return maxD


def checkNum(str1):
    bolIsNum = 0
    if (bool(re.findall("[a-zA-Z]", trim(str1)))) == True:
        # print("str", str1, len(str1))
        bolIsNum = 0
    else:
        bolIsNum = 1
    return bolIsNum



def addLead(str1, param1):
    str1 = str(str1)
    sp = ""
    addSp = 0
    if len(str1) < param1:
        addSp = param1 - len(str1)
        for i in range(0, addSp):
            sp = sp + " "
        str1 = sp + str1
    return str1

def addDot(param1):
    str1 = "-"
    for i in range(0, param1-1):
        str1 = str1 + "-"
    return str1

def maxLen(param1Num1, param1Num2, param1Sum):
    paramLen = max([len(trim(param1Num1)), len(trim(param1Num2)), len(trim(param1Sum))])
    return paramLen

def trim(p):
    p = p.strip()
    return p

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():

    print("1. 1st Parameter only.")
    arithmetic_arranger(["3 + 698", "3801 - 2", "45 + 43", "123 + 49"], )

    print("\n2. 2 Parameters.")
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

    print("\n3. Error: Too many problems.")
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "123 + 49"], True)

    print("\n4. Error: Operator must be '+' or '-'.")
    arithmetic_arranger(["32 + 8", "1 / 3801", "9999 + 9999", "523 - 49"], True)

    print("\n5. Error: Numbers must only contain digits.")
    arithmetic_arranger(["32 + 8", "a + 3801", "9999 + 9999", "523 - 49"], True)

    print("\n6. Error: Numbers cannot be more than four digits.")
    arithmetic_arranger(["32000 + 8", "1 + 1380", "9999 + 9999", "523 - 49"], True)


if __name__ == "__main__":
    main()
