#phrase = 'Caesar is the ruler of the Roman Empire'
#cipher = 29
phrase = str(input('Введите строку: '))
cipher = int(input('Введите шифр (число): '))

result = ""
char_db_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_db_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if cipher > len(char_db_lower):
    cipher = cipher %26
for char in phrase:
    if char in char_db_lower:
        if cipher + char_db_lower.index(char) >= 26:
            lastidxchar = char_db_lower.index(char) - len(char_db_lower) + cipher
            result += char_db_lower[lastidxchar]
        else:
            lastidxchar = char_db_lower.index(char) + cipher
            result += char_db_lower[lastidxchar]
    if char in char_db_upper:
        if cipher + char_db_upper.index(char) >= 26:
            lastidxchar = char_db_upper.index(char) - len(char_db_upper) + cipher
            result += char_db_upper[lastidxchar]
        else:
            lastidxchar = char_db_upper.index(char) + cipher
            result += char_db_upper[lastidxchar]
    if char.isspace():
        result += ' '
print(result);
