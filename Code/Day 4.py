

'''
def printFact(n, ansSoFar) :
    if n == 0 :
        print(ansSoFar)
        return
    ansSoFar = ansSoFar * n
    print(n, ansSoFar)
    printFact(n - 1, ansSoFar)

printFact(5, 1)
'''


# def fact(n) :
#     if n == 1 :
#         return n
#     return n * fact(n - 1)

# print(fact(5))




def getSubsequences(s) :
    if len(s) == 0 :
        return [""]
    smallOutput = getSubsequences(s[1 : ])
    output = [] 
    for i in range(len(smallOutput)) :
        output.append(smallOutput[i])
    for i in range(len(smallOutput)) :
        output.append(s[0] + smallOutput[i])
    return output

def printSubsequences(s, outputSoFar) :
    if len(s) == 0 :
        print(outputSoFar)
        return 
    printSubsequences(s[1 : ], outputSoFar)
    printSubsequences(s[1 : ], outputSoFar + s[0])

printSubsequences("abc", "")


# s = "abcd"
# output = getSubsequences(s) 
# print(output, len(output))

'''
nums1 = [10, 20]
nums2 = [30, 40]
nums3 = nums2 + nums1 
print(nums3)
'''






'''
def tower(n, source, helper, destination) :
    if n == 1 :
       print(source, destination)
       return 
    tower(n - 1, source, destination, helper)
    print(source, destination)
    tower(n - 1, helper, source, destination)

n = 4
tower(n, "s", "h", "d")
'''