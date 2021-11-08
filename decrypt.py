import pyAesCrypt, os
 
print('---------------------------------------')
 
file = input ('Введите имя файла для расшифровки:')
password = input ('Введите пароль для расшифровки:')
 
bufferSize = 64 * 1024
 
try:
    pyAesCrypt.decryptFile(str (file), str (os.path.splitext(file)[0]) , password, bufferSize)
 
except FileNotFoundError:
    print ("File not found!")
else:
    print ("File '" + str (os.path.splitext(file)[0]) + " ' successfully saved!")
finally:
    print ("-------------------------------------")
