# Leetcode-<3

# 217. Contains Duplicate

![carbon](https://github.com/user-attachments/assets/317b4b2d-a892-4ee6-81fc-efa6ea554b11)

Используем множество так как данный тип не может хранить дубликаты и сравниваем длинну с исходным списком

# 242. Valid Anagram

![carbon (1)](https://github.com/user-attachments/assets/b5414120-f137-4544-9651-ec37ef1450ad)

Код проверяет, являются ли две строки анаграммами.

Если длины строк разные — сразу возвращается False.
Для каждой строки создаются словари, где ключи — символы, а значения — их количество.
В цикле параллельно перебираются символы из обеих строк, и для каждого символа увеличивается его частота в соответствующем словаре.
В конце словари сравниваются: если они равны — строки анаграммы, иначе — нет
