import package
from package.strngs import text #абсолютный импорт
from package.ints import i #относительный импорт
from package.function_about_pckg import multiply_string # способы абсолютного импорта

#print(package.NAME)
print(text)
#print(package.ints.i)
print(i)
multiply_string()
multiply_string(i, text)
