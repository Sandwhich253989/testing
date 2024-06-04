import re

p = """
In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of
a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the 
final copy is available. It is also used to temporarily replace text in a process called greeking, which allows
designers to consider the form of a webpage or publication, without the meaning of the text influencing the design.
    """

# match the characters and get the whole word from p
t = re.findall(r'\b\w*[lL]o\w*\b', p)
print(t)

# get the next word of the matching character

s = re.findall(r'\b\w*[lL]o\w*\b\s(\b\w*\b)', p)

print(s)

