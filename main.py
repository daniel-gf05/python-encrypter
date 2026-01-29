from Crypto.Hash import SHA256

print("HASHING APP TEST")

m = SHA256.new()
passwd = "abc".encode()
m.update(passwd)
m.digest()
hashed_passwd = m.hexdigest()

print("before-> " + str(passwd))
print("after-> " + hashed_passwd)