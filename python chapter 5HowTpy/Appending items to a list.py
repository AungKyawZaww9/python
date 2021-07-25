from pip._vendor.distlib.compat import raw_input

playlist = []

print("ENter your 5 favorite name")

for i in range(5):
    playname = raw_input("Play %d :" % (i+1))
    playlist.append(playname)

print("\nSubscript      value")
for i in range(len(playlist)):
    print("%8d      %-25s" % (i+1, playlist[i]))