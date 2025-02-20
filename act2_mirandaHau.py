# Firma digital usando RSA

# importamos las librerias
import Crypto.Random
import Crypto.Util.number
import hashlib

# Para e vamos a usar el numero 4 de Fermat
e = 65537

# Calculamos la llave publica de Alice
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print("\n", "RSA nAlice: ", nA)

# Calculamos la llave publica de Bob
# pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
# qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
# nB = pB * qB
# print("\n", "RSA nBob: ", nB)

# Calcular la llave privada de Alice
phiA = (pA -1) * (qA - 1)
dA = Crypto.Util.number.inverse(e,phiA)
print("\n", "Llave privada de Alice dA: ", dA)

# Calcular la llave privada de Bob
#phiB = (pB -1) * (qB - 1)
#dB = Crypto.Util.number.inverse(e,phiB)
#print("\n", "Llave privada de Bob dB: ", dB)

#Firmamos el mensaje
mensaje = "Hola Mundo"
print("\n", "Mensaje: ", mensaje)


# Generamos el HASH del mensaje
hM = int.from_bytes(hashlib.sha256(mensaje.encode("utf-8")).digest(), byteorder='big')
print("\n", "Hash de hM: ", hM)

# Firmamos el HASH usando la llave privada de Alice y se lo enviamos a Bob
sA = pow(hM, dA, nA)
print("\n", "Firma: ", sA)

# Bob verifica la firma de Alice usando la llave PUBLICA de Alice
hM1 = pow(sA, e, nA)
print("\n", "Hash de hM1: ", hex(hM1))

# Verificamos
print("\n", "Firma valida: ", hM == hM1, "\n")