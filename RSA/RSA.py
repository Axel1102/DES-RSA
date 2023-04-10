import random
import math

# 模N大数的幂乘的快速算法
def fastExpMod(b, e, m):  # 底数，幂，大数N
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0:  
            e -= 1
            result = (result * b) % m
            continue
        e >>= 1
        b = (b * b) % m
    return result
    


# 针对随机取得p，q两个数的素性检测
def miller_rabin_test(n):  
    p = n - 1
    r = 0
    while p % 2 == 0: 
        r += 1
        p /= 2
    b = random.randint(2, n - 2)  
    if fastExpMod(b, int(p), n) == 1:
        return True  # 通过测试,可能为素数
    for i in range(0,11): 
        if fastExpMod(b, (2 ** i) * p, n) == n - 1:
            return True  # 如果该数可能为素数，
    return False  # 不可能是素数


# 生成大素数：
def create_prime_num(keylength): 
    while True:
        n = random.randint(keylength/2, keylength)
        if n % 2 != 0:
            found = True
            for i in range(0, 20):
                if miller_rabin_test(n):
                    pass
                else:
                    found = False
                    break
            if found:
                return n


# 生成密钥（包括公钥和私钥）
def create_keys(keylength):
    p = create_prime_num(keylength)
    q = create_prime_num(keylength)
    n = p * q
    # euler函数值
    fn = (p - 1)*(q - 1)
    e = selectE(fn, keylength)
    d = match_d(e, fn)
    return (n, e, d)


# 扩展Euclid 算法
def selectE(fn, halfkeyLength):
    while True:
        # e and fn are relatively prime
        e = random.randint(0, fn)
        if math.gcd(e, fn) == 1:
            return e
# 根据选择的e，匹配出唯一的d
def match_d(e, fn):
    d = 0
    while True:
        if (e * d) % fn == 1:
            return d
        d += 1




def encrypt(M, e, n):
    return fastExpMod(M, e, n)

def decrypt( C, d, m):
    return fastExpMod(C, d, m)

def display():
    print("1.使用RSA加密")
    print("2.使用RSA解密")

def encrypt_file():
    print("请输入明文：")
    mess = input().replace(' ','')
    n, e, d = create_keys(1024)
    print("生成密钥:(n:",n," ,d:",d,",e:",e,")")
    s = ''
    #s = encrypt(int(mess), e, n)
    for ch in mess:
        c = chr(encrypt(ord(ch), e, n))
        s += c
    print("加密后的密文：")
    print(s)
    f = open("./pass.txt", "w", encoding='utf-8')
    f.write(str(s))
    print("加密完成")

def decrypt_file():
    f = open('./pass.txt', 'rb')
    mess = f.read().decode('utf-8')
    f.close()
    n,d= map(int, input("输入私钥（n,d）（使用空格分隔）:").split())
    s = ''
    #s = decrypt(int(mess), d, n)

    for ch in mess:
        c = chr(decrypt(ord(ch), d, n))
        s += c
    print("解密后的明文：")
    print(s)
    f = open("rsa-mes.txt", "w", encoding='utf-8')
    f.write(str(s))
    print("解密完成")

