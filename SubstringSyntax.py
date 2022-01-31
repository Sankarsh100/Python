s=input("Enter the string:")
subs=input("Enter the substring:")
try:
    n=s.index(subs)
except ValueError:
    print("substring not find")
else:
    print("Substring found")