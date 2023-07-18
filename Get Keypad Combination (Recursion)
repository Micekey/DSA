# Keypad values are for demo. You can add values from 0 to 9 (as it is there in keypad phones).
keypad = {
    '1':'abc',
    '2': 'de',
    '3': 'fghi'
}

def kpCombo(number):
    if len(number) == 0:
        return [""]
    
    head = keypad[number[0]]
    apka_ans = kpCombo(number[1:])
    mera_ans = []
    for letter in head:
        for element in apka_ans:
            mera_ans.append(letter+element)
    
    return mera_ans        
    
print(kpCombo("123"))
