#!/usr/bin/python3

import os, random, time
from essential_generators import DocumentGenerator

gen = DocumentGenerator()
running = ""
n = random.randint(8, 16)
for x in range (0,n):
        running += gen.paragraph()

print("Chosen n: ", n)
print("You have 20 seconds before data entry starts; select the window to fill.")
time.sleep(20)

os.system('''xdotool type "''' + running.replace('''"''',"").replace("(", "").replace(")", "") + '''"''')
