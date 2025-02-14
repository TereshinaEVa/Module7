def custom_write(file_name, strings):
    string_positions = {}
    count_str = 1
    file = open(file_name, 'a', encoding='utf-8')
    for srting_n in strings:
        position = file.tell()
        file.write(srting_n + '\n')
        string_positions[(count_str, position)] = srting_n
        count_str += 1
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)