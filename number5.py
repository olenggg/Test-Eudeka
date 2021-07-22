def isPalindrome(line):
    return line == line[::-1]
 
line = input("Input Line:")
ans = isPalindrome(line)
 
if ans:
    print("True")
else:
    print("False")