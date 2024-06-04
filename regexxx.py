import re

a = "Big Planet Earth Sig"

r = re.search("^B.g.*Ea.th$", a)

f = re.findall("ig", a)

print(r)
print(f)
