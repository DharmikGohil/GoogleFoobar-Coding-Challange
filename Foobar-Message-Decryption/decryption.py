import base64

MESSAGE = ''' your encrypted message ''' #your encrypted message

KEY = 'your username' #I think your username is your mail address first text before @
                      # like if mail if abc23@gmail.com -> so username : abc23

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
