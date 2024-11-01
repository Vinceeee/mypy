from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generate_rsa_key_pair() -> tuple[bytes, bytes]:
    """生成RSA密钥对
    用了最常规的RSA加解密方式
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    public_key = private_key.public_key()

    # 序列化密钥以便存储或传输
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # 打印密钥
    print(pem_private_key.decode("utf-8"))
    print(pem_public_key.decode("utf-8"))

    return pem_public_key, pem_private_key


def encrypt(message: bytes, pem_public_key: bytes) -> bytes:
    public_key = serialization.load_pem_public_key(pem_public_key, backend=default_backend())
    # 使用公钥加密数据
    encrypted = public_key.encrypt(
        message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return encrypted


def decrypt(encrypted: bytes, pem_private_key: bytes) -> bytes:
    private_key = serialization.load_pem_private_key(pem_private_key, password=None, backend=default_backend())
    # 使用私钥解密数据
    decrypted = private_key.decrypt(
        encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return decrypted
