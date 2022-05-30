Server1_SecrectKey = 123
Server2_SecrectKey = 456

keySYSTEM = 5000

Server1_PublicKey = Server1_SecrectKey + keySYSTEM

Server2_PublicKey = Server2_SecrectKey + keySYSTEM

# -----------------------------------------------------

Server1_CommonKey = Server1_SecrectKey + Server2_PublicKey

Server2_CommonKey = Server2_SecrectKey + Server1_PublicKey

print(Server1_CommonKey == Server2_CommonKey)