n = int(input("Enter line: "))
arr = ""
for i in range(0,n):
    arr += " " + input()
change = [0] * 26
count = [0] * 26
total_count = 0
for i in range(0,len(arr)):
    if 0 <= ord(arr[i]) - 65 < 26:
        total_count += 1
        count[ord(arr[i]) - 65] += 1

common = list()
for i in range(0,26):
    common.append([round(count[i]/total_count * 100,2),chr(i + 65)])
common.sort()

def printstr(string):
    global change
    for i in range(0,len(arr)):
        if 0 <= ord(arr[i]) - 65 < 26:
            if change[ord(arr[i]) - 65] != 0:
                print('\033[33m' + chr(change[ord(arr[i]) - 65]) + '\033[0m',end="")
            else:
                print(arr[i],end="")
        else:
            print(arr[i],end="")
    print("\n")
print("")
while True:
    for i in range(25,-1,-1):
        print(common[i][1] + " = " + str(common[i][0]) + "%",end="")
        if change[ord(common[i][1]) - 65] != 0:
            print(" -> " + chr(change[ord(common[i][1]) - 65]),end="")
        print("")
    printstr(arr)
    x,y = input("Enter x -> y: ").split()
    change[ord(x) - 65] = ord(y)
    print("")