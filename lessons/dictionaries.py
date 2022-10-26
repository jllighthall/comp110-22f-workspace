"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str,int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pariing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools)

#access a value by its key -- "lookup"
print(f"UNC Has {schools['UNC']} students")

#to remove a key-value pair from a dictionary
# by its key.
#schools.pop("Duke")

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")