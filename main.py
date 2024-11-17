# Написать программу, которая:
#- Запрашивает у пользователя строку для поиска.
#- Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.
#- Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их.

file =  open("text.txt", 'r', encoding='utf-8') 
lines = file.readlines() 
search = input("Введите строку для поиска: ") 
search = search.lower() 

matching_lines = [line.strip() for line in lines if search in line.lower()]  
print(f"\nКоличество строк, содержащих подстроку '{search}': {len(matching_lines)}") 

matching_lines.sort(key=len) 
print("\nСтроки, содержащие подстроку, отсортированные по длине:") 
for line in matching_lines:
    print(line)
