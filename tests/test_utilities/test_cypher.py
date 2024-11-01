from wxabc.utilities.cypher import generate_rsa_key_pair, encrypt, decrypt


def test_rsa_encrypt_decrypt():
    pem_public_key, pem_private_key = generate_rsa_key_pair()
    encrypted = encrypt("hello world".encode(), pem_public_key)
    decrypted = decrypt(encrypted, pem_private_key)
    assert decrypted == b"hello world"
