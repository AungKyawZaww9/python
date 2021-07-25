from pip._vendor.distlib.compat import raw_input

slicestring = "abcdefghij"
slicetuple = (1,2,3,4,5,6,7,8,9,10)
slicelist = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" , "X"]

print("Slicestring : ",slicestring)
print("Slicetuple : ", slicetuple)
print("Slicelist : ", slicelist)

start = int(raw_input("Enter start : "))
end = int(raw_input("Enter end: "))



print("\nSlicestring [", start, ":", end, "] = ", \
      slicestring[start:end])
print("\nSlicetuple[", start, ":", end, "] = ", \
      slicetuple[start:end])
print("\nSlicelist[", start, ":", end, "] = ", \
      slicelist[start:end])