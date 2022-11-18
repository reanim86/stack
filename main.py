class Stack():
    def __init__(self):
        self.list = []

    def is_empty(self):
        """
        Проверка стэка пустоту
        :return:
        """
        if not self.list:
            return True
        else:
            return False

    def push(self, add_var):
        """
        добавляет новый элемент на вершину стека
        :param add_var:
        :return:
        """
        self.list.append(add_var)
        return

    def pop(self):
        """
        удаляет верхний элемент стека
        :return: возвращает удаленный элемент стэка
        """
        res = self.list[-1]
        self.list.pop()
        return res

    def peek(self):
        """
        возвращает верхний элемент стека, но не удаляет его
        :return:
        """
        return self.list[-1]

    def size(self):
        """
        возвращает количество элементов в стеке
        :return:
        """
        return len(self.list)

def check(mystr):
    """
    Функция проверяет сбалансированность скобок
    :param mystr:строка со скобками для проверки
    :return:результат проверки
    """
    open_list = ['[', '{', '(']
    close_list = [']', '}', ')']
    stack = Stack()
    for i in mystr:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((stack.size() > 0) and (open_list[pos] == stack.peek())):
                stack.pop()
            else:
                return 'Несбалансированно'
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

