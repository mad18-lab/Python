names = []
for i in range(3):
    names.append(input("Enter the respective names: "))

nums = []
for j in range(3):
    nums.append(input("Enter the respective mobile numbers: "))

if names[0] == names[1] or names[1] == names[2] or names[2] == names[0]:
    print("Warning: Name Details Are Same!")
elif nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
    print("Warning: Mobile Number Details Are Same!")

for a in nums:
    if len(a) != 10:
        print("Entered mobile number is invalid")

for b, c in zip(names, nums):
    print(b+" - "+c)
