with open("artifact_from_01.txt","r") as f:
    text = f.read()

with open("artifact_from_02.txt","w") as f:
    text = f.write(text + "\nSome extra lines")

print("End of Stage 03")

