users = ['anna','maria','markus','florian']
mails = ['anna@no.com','maria@no.com','markus@no.com','florian@no.com']

for data in zip(users, mails):
    name, mail = data
    print(f'person = {name} => {mail}')

print('---')
