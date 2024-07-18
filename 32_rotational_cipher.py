def rotate(text, key):
    
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = (plain[key:] + plain[:key])
    
    text_cipher = ""
    for i in text:
        if i.isalpha():
            if i.isupper():
                text_cipher += cipher[plain.index(i.lower())].upper()
            else:
                text_cipher += cipher[plain.index(i)]
        else:
            text_cipher += i
    return text_cipher

if __name__ == '__main__':
    rotate("OMG", 5) # 'TRL'
        
        
