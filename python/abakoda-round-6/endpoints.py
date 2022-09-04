a = input()

if (a[0:9] == "...---..." or a[-9:] == "...---..."):
    print("SOS")
else:
    print("Hay SOS!")