set1={1,2,3,4,5,6}
num=int(input("Enter a value to remove: "))
if num in set1:
    set1.remove(num)
    print(f"The number {num} is removed.")
else:
    print(f"The number {num} is not found.")
print("updated set",set1)