import zipfile
'''一个简单的zip暴力破解密码程序'''

zFile = zipfile.ZipFile('evil.zip')
passfile = open("dictionary.txt")
for line in passfile.readlines():
    password =line.strip('\n')
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print('password = ',password)
    except Exception as e:
        pass
