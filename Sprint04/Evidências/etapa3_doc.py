import hashlib

palavra=(input())
has1=hashlib.sha1()
cod=palavra.encode("utf-8")
has1.update(cod)
valor=has1.hexdigest()

print(valor)
