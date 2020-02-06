#!/usr/bin/python3

import os, random, time
from essential_generators import DocumentGenerator

gen = DocumentGenerator()
running = ""
n = random.randint(8, 16)
for x in range (0,n):
        running += gen.paragraph()

#os.system('''echo "Starting Write Process, select target in next 20 seconds" | wall''')
print("Chosen n: ", n)
time.sleep(20)

os.system('''xdotool type "''' + running.replace('''"''',"").replace("(", "").replace(")", "") + '''"''')
