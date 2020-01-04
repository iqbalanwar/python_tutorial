'''
while loops, for loops,
continue, break,
functions
'''
# ======================= LOOPS =======================

secret = 'downbad'
pw = ''
# auth = False
# count = 0
# max_attempt = 5
# while pw != secret:
#     count += 1
#     if count > max_attempt: break
#     if count == 3: continue # continue skips the step
#     pw = input(f"{count}: What's the secret word? ")
# else: # loop exits normally, so the break didn't happen
#     auth = True
# print("Authorized" if auth else "You've used 5 attempts! You're locked.")


animals = ('bear','bunny','dog','cat','velociraptor')
# for pet in animals:
#     if pet == 'dog': continue
#     if pet == 'cat': break
#     print(pet)
# else: # loop exits normally, so the break didn't happen
#     print('that is all the animals')


# ======================= FUNCTIONS =======================

def main():
    kitten()

def kitten():
    print('Meow')

if __name__=='__main__': main()