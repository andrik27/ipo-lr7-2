import json

# Вводим номер квалификации от пользователя и конвертируем его в целое число
number = int(input("Введите номер квалификации: "))
find = False  # Флаг для проверки, найдена ли квалификация

# Открываем файл dump.json для чтения и загружаем данные в переменную data
with open("dump.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    
    # Найти квалификацию по pk
    for skill in data:
        if skill.get("model") == "data.skill" and skill["pk"] == number:
            skill_pk = skill["pk"]  # Сохраняем pk квалификации
            skill_title = skill["fields"].get("title")  # Сохраняем название квалификации
            find = True  # Устанавливаем флаг в True, так как квалификация найдена
            break  # Прерываем цикл, так как квалификация найдена

    # Найти специальность по pk
    if find:
        for profession in data:
            if profession.get("model") == "data.specialty" and profession["pk"] == skill_pk:
                specialty_pk = profession["pk"]  # Сохраняем pk специальности
                specialty_title = profession["fields"].get("title")  # Сохраняем название специальности
                specialty_educational = profession["fields"].get("c_type")  # Сохраняем тип образования специальности
                break  # Прерываем цикл, так как специальность найдена

# Если квалификация не найдена, выводим соответствующее сообщение
if not find:
    print("=============== Не Найдено ===============")
else:
    # Если квалификация найдена, выводим информацию о специальности и квалификации
    print("=============== Найдено ===============")
    print(f"{specialty_pk} >> Специальность '{specialty_title}' , {specialty_educational}")
    print(f"{skill_pk} >> Квалификация '{skill_title}'")
