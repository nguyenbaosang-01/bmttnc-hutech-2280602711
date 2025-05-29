class PlayFairCipher:
    def _init__(self) -> None:
        pass
def _init__(self):
    pass
class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên
        
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text

def create_playfair_matrix(self, key):
    key = key.replace("J", "I") # Chuyển "J" thành "I" trong khóa
    key= key.upper()
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    remaining_letters = [
        letter for letter in alphabet if letter not in key_set]
    matrix = list(key)
    for letter in remaining_letters:
        matrix.append(letter)
    if len(matrix) == 25:
        break
    playfair_matrix = [matrix[1:1+5] for i in range(0, len (matrix), 5)]
    return playfair_matrix
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col