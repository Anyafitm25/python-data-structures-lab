import sys
import timeit

# =====================================================================
# ЗАВДАННЯ 1. Списки: індексація, зрізи та мутації (2 бали)
# =====================================================================
def run_task_1():
    print("=== ЗАВДАННЯ 1. Списки ===")
    # Детерміновані дані (цілі числа)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"Початковий список (id: {id(numbers)}): {numbers}, довжина: {len(numbers)}\n")
    
    # Індексація
    print(f"Додатний індекс: {numbers[2]} | Від'ємний індекс [-1]: {numbers[-1]}")
    
    # ТРИ різних зрізи (створюють нові об'єкти в пам'яті)
    slice_1 = numbers[2:6]     # Межі [2:6], крок 1
    slice_2 = numbers[:8:2]    # Крок відмінний від 1 (крок 2)
    slice_3 = numbers[::-1]    # Реверс списку
    print(f"Зріз 1 [2:6]: {slice_1} (Новий об'єкт id: {id(slice_1)})")
    print(f"Зріз 2 [:8:2]: {slice_2} (Новий об'єкт id: {id(slice_2)})")
    print(f"Зріз 3 [::-1]: {slice_3} (Новий об'єкт id: {id(slice_3)})\n")
    
    # Мутації in-place (модифікують оригінальний об'єкт)
    numbers.append(110)
    print(f"Мутація 1 (append 110): {numbers} | Нова довжина: {len(numbers)}")
    
    numbers.insert(0, 5)
    print(f"Мутація 2 (insert 5 на початок): {numbers} | Нова довжина: {len(numbers)}")
    
    numbers.remove(50)
    print(f"Мутація 3 (remove значення 50): {numbers} | Нова довжина: {len(numbers)}")
    
    numbers[1:3] = [99, 99]
    print(f"Мутація 4 (заміна зрізу [1:3]): {numbers} | Нова довжина: {len(numbers)}")
    print(f"Фінальний список має той самий id: {id(numbers)}\n")


# =====================================================================
# ЗАВДАННЯ 2. Кортежі та «розпакування» даних (2 бали)
# =====================================================================
def run_task_2():
    print("=== ЗАВДАННЯ 2. Кортежі ===")
    # Структура: (ID, Назва товару, Кількість, Ціна, [Список оцінок - мутабельний])
    products = [
        (101, "Laptop", 3, 32000.0, [5, 4, 5]),
        (102, "Phone", 10, 15000.0, [4, 4]),
        (103, "Tablet", 5, 8500.0, [5, 3, 4])
    ]
    
    # Функція розпакування
    print("Розпакування записів:")
    for prod in products:
        p_id, name, qty, price, ratings = prod
        print(f"  Товар {name} (ID: {p_id}) коштує {price} грн. Оцінки: {ratings}")
        
    # Функція агрегації
    def calculate_total(items):
        total_sum = 0.0
        for item in items:
            total_sum += item[2] * item[3] # Кількість * Ціна
        return round(total_sum, 2)
    
    print(f"\nАгрегована вартість товарів: {calculate_total(products)} грн\n")
    
    # Демонстрація імутабельності (спроба зміни)
    print("Спроба прямої мутації кортежу (помилка):")
    try:
        products[0][1] = "New Laptop Name"
    except TypeError as e:
        print(f"  Успішно перехоплено виняток: {e}")
        
    # Мутабельний об'єкт всередині кортежу
    print(f"\nПочатковий кортеж №1: {products[0]}")
    products[0][4].append(5) # Мутуємо список всередині кортежу
    print(f"Після додавання оцінки в список всередині кортежу: {products[0]}\n")


# =====================================================================
# ЗАВДАННЯ 3. Словники та облік частот (2 бали)
# =====================================================================
def run_task_3(filename="text.txt"):
    print("=== ЗАВДАННЯ 3. Словники та частотний аналіз ===")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw_text = f.read()
    except FileNotFoundError:
        raw_text = "Python is fast. Python is powerful. Python data structures are clean."
        print("Файл text.txt не знайдено, використано резервний текст.")
        
    print(f"Аналізований текст: \"{raw_text.strip()}\"")
    
    # Нормалізація та токенізація
    clean_text = raw_text.lower()
    for char in ".,!?;:()\"'-":
        clean_text = clean_text.replace(char, " ")
    words = clean_text.split()
    
    # Облік частот (Безпечний доступ через .get())
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
        
    # Сортування
    by_key = sorted(freq_dict.items())
    by_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nСортування за алфавітом (ключем): {by_key}")
    print(f"Сортування за спаданням частоти: {by_freq}")
    
    # Dict comprehension (Фільтрація: слова, що зустрічаються хоча б 2 рази)
    filtered = {k: v for k, v in freq_dict.items() if v >= 2}
    print(f"Dict comprehension (частота >= 2): {filtered}\n")


# =====================================================================
# ЗАВДАННЯ 4. Множини: унікальність та операції (2 бали)
# =====================================================================
def run_task_4():
    print("=== ЗАВДАННЯ 4. Множини ===")
    # Вхідні колекції з повторами
    list_A = ["id_1", "id_2", "id_3", "id_1", "id_4"]
    list_B = ["id_3", "id_4", "id_5", "id_6", "id_4"]
    list_C = ["id_1", "id_2"]
    
    set_A = set(list_A)
    set_B = set(list_B)
    set_C = set(list_C)
    
    print(f"Множина A (унікальні): {set_A}")
    print(f"Множина B (унікальні): {set_B}")
    print(f"Множина C (унікальні): {set_C}\n")
    
    # Математичні операції
    print(f"Перетин (A & B): {set_A.intersection(set_B)}")
    print(f"Об'єднання (A | B): {set_A.union(set_B)}")
    print(f"Симетрична різниця (A ^ B): {set_A.symmetric_difference(set_B)}")
    
    # Відношення підмножини
    print(f"\nЧи є C підмножиною A (C <= A)? {set_C.issubset(set_A)} (Очікувано: True)")
    print(f"Чи є B підмножиною A (B <= A)? {set_B.issubset(set_A)} (Очікувано: False)\n")


# =====================================================================
# ЗАВДАННЯ 5. Алгоритмічна складність та бенчмарки (3 бали)
# =====================================================================
def run_task_5():
    print("=== ЗАВДАННЯ 5. Експериментальний аналіз складності ===")
    sizes = [100, 1000, 10000]
    results = {size: {} for size in sizes}
    
    for n in sizes:
        # Генеруємо дані
        t_list = list(range(n))
        t_set = set(t_list)
        t_dict = {i: i for i in t_list}
        target = n + 5  # Гарантована відсутність (найгірший випадок)
        
        # Кількість тестів залежить від N, щоб уникнути зависання
        iters = 2000 if n <= 1000 else 200
        
        # Вимірювання пошуку
        time_list = timeit.timeit(lambda: target in t_list, number=iters) / iters * 1_000_000
        time_set = timeit.timeit(lambda: target in t_set, number=iters) / iters * 1_000_000
        time_dict = timeit.timeit(lambda: target in t_dict, number=iters) / iters * 1_000_000
        
        # Вимірювання побудови унікальних з дублікатів (list vs set)
        input_data = list(range(n)) + list(range(n))
        
        def build_via_list():
            res = []
            for x in input_data:
                if x not in res: res.append(x)
                
        def build_via_set():
            res = set()
            for x in input_data: res.add(x)
            
        time_build_list = timeit.timeit(build_via_list, number=5) / 5 * 1_000_000
        time_build_set = timeit.timeit(build_via_set, number=5) / 5 * 1_000_000
        
        results[n] = (time_list, time_set, time_dict, time_build_list, time_build_set)
        
    # Табличний вивід
    print(f"{'N':<7} | {'Пошук List(мкс)':<16} | {'Пошук Set(мкс)':<14} | {'Пошук Dict(мкс)':<15} | {'Збір List(мкс)':<15} | {'Збір Set(мкс)':<14}")
    print("-" * 92)
    for n in sizes:
        r = results[n]
        print(f"{n:<7} | {r[0]:<16.4f} | {r[1]:<14.4f} | {r[2]:<15.4f} | {r[3]:<15.2f} | {r[4]:<14.2f}")
        
    print("\n[Псевдографіка] Візуалізація зростання часу збору унікальних у Списку (O(N^2)):")
    for n in sizes:
        scale = int(results[n][3] / (results[10000][3] + 1) * 30) + 1
        print(f"N={n:<5} | " + "█" * scale + f" ({results[n][3]:.1f} мкс)")


if __name__ == "__main__":
    run_task_1()
    run_task_2()
    run_task_3()
    run_task_4()
    run_task_5()
