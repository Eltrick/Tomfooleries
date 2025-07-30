unencryptedNumbers = [int(x) for x in list(input("Stages: "))]
largestSN = int(input("What is the largest digit in the serial number? "))
smallestOdd = int(input("What is the smallest odd digit in the Serial Number? "))
for j in range(0, len(unencryptedNumbers)):
    if j == 0:
        if input("Does the bomb have an unlit CAR indicator? ").upper() == "Y":
            unencryptedNumbers[j] += 2
        elif input("Does the bomb have more unlit than lit indicators? ").upper() == "Y":
            unencryptedNumbers[j] += 7
        elif input("Are there no unlit indicators? ").upper() == "Y":
            unencryptedNumbers[j] += int(input("How many lit indicators are there? "))
        else:
            unencryptedNumbers[j] += int(input("What is the last digit of the Serial Number? "))
    elif j == 1:
        if input("Does the bomb have a Serial port? ").upper() == "Y" and input("Are there 3 or more digits in the Serial Number? ").upper() == "Y":
            unencryptedNumbers[j] += 3
        elif unencryptedNumbers[j - 1] % 2 == 0:
            unencryptedNumbers[j] += unencryptedNumbers[j - 1] + 1
        else:
            unencryptedNumbers[j] += unencryptedNumbers[j - 1] - 1
    else:
        if unencryptedNumbers[j - 1] == 0 or unencryptedNumbers[j - 2] == 0:
            unencryptedNumbers[j] += largestSN
        elif unencryptedNumbers[j - 1] % 2 == 0 and unencryptedNumbers[j - 2] % 2 == 0:
            unencryptedNumbers[j] += smallestOdd
        else:
            if unencryptedNumbers[j - 1] + unencryptedNumbers[j - 2] > 9:
                unencryptedNumbers[j] += 1
            else:
                unencryptedNumbers[j] += unencryptedNumbers[j - 1] + unencryptedNumbers[j - 2]
    unencryptedNumbers[j] %= 10
print("".join([str(x) for x in unencryptedNumbers]))