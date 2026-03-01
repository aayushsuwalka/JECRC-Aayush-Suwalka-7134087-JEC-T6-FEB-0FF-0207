# Functions
# Types in which we can define a simple 


# def addTwoNum() :
#     a, b = int(input()), int(input())
#     print(a+b)

# def AddTwoNums(a, b):
#     print(a+b)

# def addtwonums():
#     a, b = int(input()), int(input())
#     return a+b

# def addTwoNums(a,b):
#     return a+b

nums = [1, 2, 3, 5, 6, 7, 11, 15]
target = 8
i=0
j=len(nums)-1
ans = []
while i<=j:
    if nums[i] + nums[j] == target:
        ans.append({i, j})
        i = i+1
        j = j-1
    elif nums[i]+nums[j] > target:
        j = j - 1
    else:
        i = i + 1
print(ans)
