# 3

def qsort(inlist):
    if inlist == []:
        return []
    else:
        firstly = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < firstly])
        greater = qsort([x for x in inlist[1:] if x >= firstly])
        return lesser + [firstly] + greater

# Как по мне это самый быстрый способ сортировки массива. В отличиях от встроенного "sorted" и других различных
# способов тут используется намного меньше различных операции - это и делает данную функцию быстрой. Нет лишних
# вычислений
