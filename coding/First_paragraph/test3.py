# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop':
#         break
#     if not reply.isdigit():
#         print('Bad!'*8)
#     else:
#         print(int(reply) ** 2)
# print('bye')

while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        int(reply)
    except:
        print('Bad' * 8)
    else:
        print(int(reply) ** 2)

print('Bye')
