from typing import Dict

emptydictionary = {}
print("The vale of emptd : ", emptydictionary)

grades: dict[str, int] = { "john": 87, "Steve": 76, "Laura": 90, "kyaw": 77}
print("\nAll grades : ", grades)

print("\nSteven current grade:", grades["kyaw"])
grades["kyaw"] = 90
print("k's new grade :", grades["kyaw"])

grades["Michel"] = 93
grades["yellow"] = 68
print("\nDictionary grades: ")
print(grades)

del grades["Laura"] # deletion == make cancel
print("\nDictionary grades after :")
print(grades)