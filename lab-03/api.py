from flask import Flask, request, jsonify
from cipher.rsa import RSACipher

app = Flask(__name__)

# Khởi tạo đối tượng RSA
rsa_cipher = RSACipher()

# API: Tạo cặp khóa RSA
@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

# API: Mã hóa bằng khóa công khai hoặc riêng tư
@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    message = data.get('message')
    key_type = data.get('key_type')

    private_key, public_key = rsa_cipher.load_keys()

    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400

    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()

    return jsonify({'encrypted_message': encrypted_hex})

# API: Giải mã bằng khóa công khai hoặc riêng tư
@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data.get('ciphertext')
    key_type = data.get('key_type')

    private_key, public_key = rsa_cipher.load_keys()

    if key_type == 'private':
        key = private_key
    elif key_type == 'public':
        key = public_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400

    decrypted_message = rsa_cipher.decrypt(bytes.fromhex(ciphertext_hex), key)
    return jsonify({'decrypted_message': decrypted_message})
