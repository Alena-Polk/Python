open("three.txt", "w").write(open("one.txt", "r").read() + open("two.txt", "r").read())
