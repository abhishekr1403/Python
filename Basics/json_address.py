import json

book = {}

book['tom'] = {
    'name': "tom",
    'address': "abcdegehj",
    'phone': 758945212
}
book['bob'] = {
    'name': "bob",
    'address': "abrgedehyjku",
    'phone': 685135264
}

s = json.dumps(book)
with open("E://Python//Sample//book.txt", 'w') as f:
    f.write(s)