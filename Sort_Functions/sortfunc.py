def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]

def insertion_sort(ls):
    # Начинаем сортировать со второго элемента, т.к. первый элемент считается отсортированным
    for i in range(1, len(ls)):
        item = ls[i]
        # берем элемент для вставки и сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # отсортированный кусок списка двигаем вперед, если он больше элемента для всавки
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
        # вставляем элемент
        ls[j + 1] = item