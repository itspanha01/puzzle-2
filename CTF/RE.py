import hashlib
import time
import math

'''Welcome Honey. Are you ready for this round?

Down here, is a basic hashing technique. Your job is to crack the code the retrive the flag (often looks like this: flag{..})
Now, There are multiple ways to crack this code and each can differently from each other. You can try and guess the
code but I assure you it will take a bit of time. I will also provide you with hints for you along the way.

Given hints: "Panha's recent favorite word.'''

# Work here
def hashing():
    print("======================= Simple Reverse Engineering =======================")
    decrypt = input("Code: ")
    encrypt = "0dd1495a2f74d28f8ab0395b6d7ae091fe05a1bd8bd1046dd4d7f6e0368e5c57"
    
    def check():
        with open('flag.txt', 'r', encoding='cp1252') as file:
            text = file.read()
            text = bytes(text,"cp1252")
            print(str(text))
    
    if encrypt == hashlib.sha256(decrypt.encode('utf-8')).hexdigest():
        time.sleep(1.5)
        # Just a progress bar. Don't worry about this.
        def progress(progress, total):
            percent = (progress/(total))*100
            bar = '▮' * int(percent) + "▯" * int(100 - percent)
            print(f'\r|{bar}| {percent:.2f}%', end="\r")

        numbers = [x * 5 for x in range(1, 1500)]
        results = []

        progress(0, len(numbers))   
        for i, x in enumerate(numbers):
            results.append(math.factorial(x))
            progress(i+1, len(numbers))  # progress bar by Nerualine
        check()
    else:
        print(f'Try again.')

#initialize game
hashing()