'''
- to create address book and write some records into it
-read this address book
'''
book={}
book['tom']={
    'name':'tom',
    'address':'1 red street,NY',
    'phone': 777499109
}
book['bob']={
    'name':'bob',
    'address':'1 green street,NY',
    'phone': 1234567
}
import json
s=json.dumps(book)
with open("pythonBasics/data/book.txt","w+") as f:
    f.write(s)