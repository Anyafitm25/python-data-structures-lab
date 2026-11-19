import sys
import time
import statistics

# ============================================================
# ЗАВДАННЯ 1. СПИСКИ
# ============================================================
DATA = [10, 20, 30, 40, 50, 60, 70, 80]


def show1(label, value):
    print(f"  {label:<48} -> {value}")


def check_len(lst, expected):
    """Додатково: діагностика довжини після мутації."""
    status = "OK" if len(lst) == expected else "ПОМИЛКА"
    print(f"  [діагностика] len={len(lst)}, очікувано={expected}: {status}")


def main1():
    nums = DATA  # посилання на той самий об'єкт, копія не створюється
    expected_len = len(nums)

    print("Крок 0. Початковий список")
    show1("nums", nums)
    show1("len(nums)", len(nums))

    print("\nКрок 1. Індексація")
    show1("nums[0]  (перший, додатний індекс)", nums[0])
    show1("nums[3]  (додатний індекс)", nums[3])
    show1("nums[-1] (останній, від'ємний індекс)", nums[-1])
    show1("nums[-3] (від'ємний індекс)", nums[-3])

    print("\nКрок 2. Зрізи (кожен зріз створює НОВИЙ список)")
    show1("nums[1:4]    (межі, крок 1)", nums[1:4])
    show1("nums[::2]    (весь список, крок 2)", nums[::2])
    show1("nums[-4:-1]  (від'ємні межі)", nums[-4:-1])
    show1("nums[6:1:-2] (зворотний крок -2)", nums[6:1:-2])
    show1("nums[:]      (повна копія)", nums[:])
    print(f"  nums[:] is nums -> {nums[:] is nums} (це інший об'єкт)")

    print("\nКрок 3. Мутації «на місці» (id списку не змінюється)")
    list_id = id(nums)

    nums.append(90)
    expected_len += 1
    print(f"3.1 append(90):")
    show1("nums", nums)
    check_len(nums, expected_len)

    nums.insert(2, 25)
    expected_len += 1
    print("3.2 insert(2, 25):")
    show1("nums", nums)
    check_len(nums, expected_len)

    del nums[0]
    expected_len -= 1
    print("3.3 del nums[0]:")
    show1("nums", nums)
    check_len(nums, expected_len)

    nums.remove(60)
    expected_len -= 1
    print("3.4 remove(60) (за значенням):")
    show1("nums", nums)
    check_len(nums, expected_len)

    nums[1:3] = [111, 222, 333]  # заміна діапазону довжини 2 на 3 елементи
    expected_len += 1
    print("3.5 nums[1:3] = [111, 222, 333] (заміна діапазону):")
    show1("nums", nums)
    check_len(nums, expected_len)

    print("\nКрок 4. Підсумок")
    print(f"  id списку не змінився: {id(nums) == list_id}")
    show1("фінальний список", nums)


# ============================================================
# ЗАВДАННЯ 2. КОРТЕЖІ
# ============================================================
PRODUCTS = [
    (1, "Клавіатура", 5, 850.50),
    (2, "Миша", 12, 320.00),
    (3, "Монітор", 3, 7200.99),
    (4, "Кабель HDMI", 20, 150.25),
]


def describe_record(record):
    """Розпакування кортежу в окремі поля."""
    pid, name, qty, price = record
    return pid, name, qty, price


def total_cost(records):
    """Загальна вартість складу (грн)."""
    total = 0.0
    for _id, _name, qty, price in records:
        total += qty * price
    return round(total, 2)


def print_table(records):
    print(f"{'ID':>3} | {'Назва':<12} | {'К-сть, шт.':>10} | {'Ціна, грн/шт.':>13}")
    print("-" * 49)
    for pid, name, qty, price in records:
        print(f"{pid:>3} | {name:<12} | {qty:>10} | {price:>13.2f}")


def to_dicts(records):
    """Необов'язкове: список кортежів -> список словників."""
    keys = ("id", "name", "quantity", "unit_price")
    return [dict(zip(keys, r)) for r in records]


def main2():
    print("Таблиця товарів:")
    print_table(PRODUCTS)

    print("\nРозпакування одного запису:")
    pid, name, qty, price = describe_record(PRODUCTS[0])
    print(f"  id={pid}, назва={name}, кількість={qty} шт., ціна={price} грн/шт.")

    print(f"\nЗагальна вартість: {total_cost(PRODUCTS)} грн (округлено до 2 знаків)")

    print("\nСпроба змінити елемент кортежу за індексом:")
    rec = PRODUCTS[1]
    try:
        rec[2] = 100
    except TypeError as e:
        print(f"  TypeError: {e}")

    print("\nКортеж із мутабельним вкладенням (список оцінок):")
    student = ("Іваненко", "КБ-21", [90, 85, 77])
    print(f"  до:    {student}, id списку = {id(student[2])}")
    student[2].append(100)
    student[2][0] = 95
    print(f"  після: {student}, id списку = {id(student[2])}")
    print("  Незмінні: склад кортежу (посилання на 3 об'єкти). Змінний: вміст списку всередині.")
    try:
        student[2] = [1]
    except TypeError as e:
        print(f"  Заміна самого посилання -> TypeError: {e}")

    print("\nСписок словників:")
    for d in to_dicts(PRODUCTS):
        print(" ", d)


# ============================================================
# ЗАВДАННЯ 3. СЛОВНИКИ
# ============================================================
DEFAULT_FILE = "sample_text.txt"
OUTPUT_FILE = "freq_output.txt"
THRESHOLD = 2
KEEP_CHARS = "'-"  # символи, що лишаються всередині слова


def normalize(text):
    text = text.lower()
    cleaned = []
    for ch in text:
        if ch.isalnum() or ch in KEEP_CHARS:
            cleaned.append(ch)
        else:
            cleaned.append(" ")
    return "".join(cleaned)


def tokenize_words(text):
    return [w.strip(KEEP_CHARS) for w in normalize(text).split() if w.strip(KEEP_CHARS)]


def tokenize_chars(text):
    return [ch for ch in text.lower() if ch.isalnum()]


def count_items(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1  # безпечне отримання + інкремент
    return freq


def get_freq(freq, key):
    return freq.get(key, 0)  # відсутній ключ -> 0, без винятку


def format_lines(freq, title):
    lines = [f"== {title} =="]
    lines.append("-- за ключем (алфавіт) --")
    for k in sorted(freq):
        lines.append(f"{k}\t{freq[k]}")
    lines.append("-- за спаданням частоти (за рівності — за ключем) --")
    for k, v in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"{k}\t{v}")
    return lines


def main3():
    filename = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    word_freq = count_items(tokenize_words(text))
    char_freq = count_items(tokenize_chars(text))

    frequent = {w: c for w, c in word_freq.items() if c >= THRESHOLD}  # dict comprehension

    out = []
    out += format_lines(word_freq, "Частоти слів")
    out.append(f"\n== Слова з частотою >= {THRESHOLD} ==")
    for k, v in sorted(frequent.items(), key=lambda kv: (-kv[1], kv[0])):
        out.append(f"{k}\t{v}")
    out.append("")
    out += format_lines(char_freq, "Частоти символів (додатковий режим)")

    print("\n".join(out))
    print(f"\nЧастота відсутнього слова 'відсутнє': {get_freq(word_freq, 'відсутнє')}")
    print(f"Унікальних слів: {len(word_freq)}, унікальних символів: {len(char_freq)}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"Результат збережено у {OUTPUT_FILE}")


# ============================================================
# ЗАВДАННЯ 4. МНОЖИНИ
# ============================================================
A_RAW = ["ID-001", "ID-002", "ID-003", "ID-002", "ID-004", "ID-001"]
B_RAW = ["ID-003", "ID-004", "ID-005", "ID-005", "ID-006"]
C_RAW = ["ID-003", "ID-004", "ID-003"]


def show4(label, s):
    print(f"  {label:<32} {sorted(s)}")


def main4():
    a, b, c = set(A_RAW), set(B_RAW), set(C_RAW)

    print("Унікальні значення:")
    print(f"  A: {len(A_RAW)} елементів -> {len(a)} унікальних")
    print(f"  B: {len(B_RAW)} елементів -> {len(b)} унікальних")
    print(f"  C: {len(C_RAW)} елементів -> {len(c)} унікальних")
    show4("A", a)
    show4("B", b)
    show4("C", c)

    print("\nОперації над парою A, B:")
    show4("Перетин A & B", a & b)
    show4("Об'єднання A | B", a | b)
    show4("Симетрична різниця A ^ B", a ^ b)

    print("\nОперації над парою B, C:")
    show4("Перетин B & C", b & c)
    show4("Об'єднання B | C", b | c)
    show4("Симетрична різниця B ^ C", b ^ c)

    print("\nВідношення підмножини:")
    print(f"  C <= B: {c <= b}   (істинне)")
    print(f"  A <= B: {a <= b}  (хибне)")

    print("\nНеобов'язкове: frozenset як ключ словника і елемент множини")
    fa, fb = frozenset(a), frozenset(b)
    registry = {fa: "група A", fb: "група B"}
    print(f"  registry[frozenset(A)] = {registry[frozenset(A_RAW)]}")
    set_of_sets = {fa, fb, frozenset(A_RAW)}  # дубль frozenset(A) не додається
    print(f"  розмір множини множин: {len(set_of_sets)} (дублікат A відкинуто)")


# ============================================================
# ЗАВДАННЯ 5. СКЛАДНІСТЬ
# ============================================================
SIZES = [100, 1_000, 10_000]
REPEATS = 5


def measure(func, repeats=REPEATS):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        func()
        times.append(time.perf_counter() - t0)
    return statistics.mean(times), min(times), max(times)


def bench_search_list(n):
    data = list(range(n))
    target = -1  # найгірший випадок: елемента немає
    return lambda: [target in data for _ in range(200)]


def bench_search_set(n):
    data = set(range(n))
    target = -1
    return lambda: [target in data for _ in range(200)]


def bench_search_dict(n):
    data = {i: i for i in range(n)}
    target = -1
    return lambda: [target in data for _ in range(200)]


def bench_unique_list(n):
    items = list(range(n))  # усі унікальні — найгірший випадок

    def run():
        seen = []
        for x in items:
            if x not in seen:
                seen.append(x)
    return run


def bench_unique_set(n):
    items = list(range(n))

    def run():
        seen = set()
        order = []
        for x in items:
            if x not in seen:
                seen.add(x)
                order.append(x)
    return run


def main5():
    cases = [
        ("пошук у list (200 пошуків)", bench_search_list, "O(n)"),
        ("пошук у set (200 пошуків)", bench_search_set, "O(1)"),
        ("ключ у dict (200 пошуків)", bench_search_dict, "O(1)"),
        ("унікальні: list + перевірка", bench_unique_list, "O(n^2)"),
        ("унікальні: set", bench_unique_set, "O(n)"),
    ]
    print(f"Повторів: {REPEATS}. Час у мілісекундах (мс): середнє [min..max]\n")
    print(f"{'Операція':<30}{'Асимптотика':<13}{'n':>8}{'середнє, мс':>14}{'min, мс':>11}{'max, мс':>11}")
    print("-" * 87)
    results = {}
    for name, maker, big_o in cases:
        for n in SIZES:
            avg, lo, hi = measure(maker(n))
            results[(name, n)] = avg * 1000
            print(f"{name:<30}{big_o:<13}{n:>8}{avg*1000:>14.4f}{lo*1000:>11.4f}{hi*1000:>11.4f}")
        print()

    print("Псевдографіка: пошук у list (мс залежно від n)")
    name = cases[0][0]
    peak = max(results[(name, n)] for n in SIZES)
    for n in SIZES:
        v = results[(name, n)]
        bar = "#" * max(1, int(40 * v / peak))
        print(f"  n={n:>6} | {bar} {v:.4f} мс")

if __name__ == "__main__":
    for n, fn in enumerate([main1, main2, main3, main4, main5], start=1):
        print("\n" + "=" * 60)
        print(f"ЗАВДАННЯ {n}")
        print("=" * 60)
        fn()
