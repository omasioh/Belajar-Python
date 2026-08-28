num = 2
a = 9
b = 11
age = 28
temperature = 30
Role_Access = "Admin"

# Formula = x if condition y
# print("Positif" if num > 0 else "Negative")
#result = "Even" if num % 2 == 0 else "ODD"
#num_max = a if a > b else b
#num_min = a if a < b else a
#status = "Adult" if age >=18 else "Child"
#weather = "Hot" if temperature >= 30 else "Cold"
Access_level = "Full Access" if Role_Access == "Admin" else "Limited Access"

print(Access_level)