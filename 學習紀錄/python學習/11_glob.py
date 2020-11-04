import  glob

print(glob.glob("./*.py"))
print(glob.glob("./0*.py"))
print(glob.glob("./0[1-3]*.py"))