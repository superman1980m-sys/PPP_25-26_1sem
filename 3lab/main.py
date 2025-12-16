

if __name__ == "__main__":
    def generate_permutations(elements, current_permutation=[], steps=[]):
    if len(elements) == 0:
        steps.append(f"Итоговая перестановка: {current_permutation}")
        return [current_permutation]
    
    permutations = []
    for i in range(len(elements)):
        new_elements = elements[:i] + elements[i+1:]
        new_permutation = current_permutation + [elements[i]]
        steps.append(f"Шаг: {new_permutation}, оставшиеся элементы: {new_elements}")
        permutations += generate_permutations(new_elements, new_permutation, steps)
    
    return permutations

def generate_combinations(elements, combination_size, start=0, current_combination=[], steps=[]):
    if len(current_combination) == combination_size:
        steps.append(f"Итоговая комбинация: {current_combination}")
        return [current_combination]
    
    combinations = []
    for i in range(start, len(elements)):
        new_combination = current_combination + [elements[i]]
        steps.append(f"Шаг: {new_combination}, оставшиеся элементы: {elements[i+1:]}")
        combinations += generate_combinations(elements, combination_size, i + 1, new_combination, steps)
    
    return combinations

# Пример использования
elements = ['a', 'b', 'c']
steps = []

# Генерация всех перестановок
print("Перестановки:")
permutations = generate_permutations(elements, steps=steps)
print(permutations)

# Генерация всех комбинаций (выбор 2 элементов)
steps.clear()  # Очистим шаги для следующей генерации
print("\nКомбинации:")
combinations = generate_combinations(elements, 2, steps=steps)
print(combinations)

# Вывод шагов
print("\nШаги вычислений:")
for step in steps:
    print(step)
