# While_loop
num=int(input("Enter the number want to print :"))
init=1
while(init <= num):
    print(init)
    init=init+1
    
# for Loop
n = 4
for i in range(0, n):
    print(i)


#For loops in list
li = ["geeks", "for", "geeks"]
for i in li:
    print(i)

#For loops in tupple    
tup=("hey","this","is","mustakim")
for i in tup:
    print(i)

# #For loops in Dictionary
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# # Access using key
print(d["name"])

# # Access using get()
print(d.get("name"))

# #Updating values
result=d["name"]="Mustakim"
print(result)

for i in d:
    print(i,d[i])
