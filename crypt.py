import pyAesCrypt
 
print('---------------------------------------')
 
file = input ('Введите имя файла для шифрования:')
password = input ('Введите пароль для шифрования:')
 
bufferSize = 64 * 1024
 
try:
    pyAesCrypt.encryptFile (str (file), str (file) + ".almet", password, bufferSize)
except FileNotFoundError:
    print ("File not found!")
    
else:
    print ("File '"+str (file) + " .bobr' successfully saved!")
finally:
    print ("-------------------------------------")
