a = "ABcd"
b = ""

if a:
    print("True a")
if b:
    print("True b")
else:
    print("False b")

f = open("pw.txt", "r")
print(f.read())
f.close()

c = "004282"
d = "16b54"

print(c.isnumeric())
print(d.isnumeric())

f = open("pw.txt", "w")
f.write("passord")
f.close()