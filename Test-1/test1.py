# Тестовые данные — одна строка с переносами
test_data = """hell_o
my_name
world
tes_t
user_name
python"""

# Превращаем в итератор
# test_input = iter(test_data.splitlines())

# while True:
#     try:
#         word = next(test_input)   # вместо input()
#     except StopIteration:
#         break                     # данные закончились
#     if "_" not in word:
#         print("Найдено слово без '_':", word)
#         break

test_input = iter(test_data.splitlines())  # Вариант без проверок на ошибки, учебный.
word = next(test_input)
while '_' in word:
    word = next(test_input)
print(word)


# a = """@monic_abing
# @howyoudo_ing1😎
# @divorc_eguy💔
# @richard777
# @rache_lg"""
#
#
# while '_' in a:
#     if '_' not in a:
#         print(a)

# text = """@monica_bing
# @how_you_doing1😎
# @divorce_guy💔
# @richard777
# @rachel_g"""

# text = input()                  # 1-й ввод
# while 'Левон' != text:          # пока введённое НЕ "Левон"
#     # text = input()              # просим ввести снова
#     print(text)
