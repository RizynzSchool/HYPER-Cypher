# TO-DO = Convert Hexadecimals to 64
# HIPERCODE
top = []
bot = []
let = []
i = 0
uInp = raw_input('String >> ')
let = list(uInp)

# Getting Top List
while i != len(let):
    top += let[i]
    i += 2
    if i > len(let):
        let += '0'
# Getting Bottom List
i = 1
while i != len(let):
    bot += let[i]
    i += 2
    if i > len(let):
        let += '0'
bot.pop()

# Final Product
Final = ''.join(top + bot)
print('Char >> ' + Final)
# Turning into ASCII
ASCII_Values = [ord(character) for character in Final]
ASCII_Hex = [hex(character) for character in ASCII_Values]
print('Hex >> ' + ''.join(ASCII_Hex))
