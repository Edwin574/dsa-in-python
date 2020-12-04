class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def get_items(self):
        return self.items
    
    def is_empty(self):
        print(len(self.items) == 0)
        return len(self.items) == 0
    
    def peek(self):
        if  len(self.items) > 0:
            return self.items[-1]

myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
print(myStack.get_items())
print(myStack.peek())
myStack.push('D')
myStack.pop()


def check_balanced_brackets(arr):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(arr) and is_balanced:
        paren = arr[index]

        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()

                if not is_match(top, paren):
                    is_balanced = False
        index +=1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    else:
        return False

print(check_balanced_brackets("{(}"))

def reverse_string(string_value):
    s_array = Stack()
    index = len(string_value) - 1
    

    while index >= 0:
    
        item = string_value[index]
        s_array.push(item)

        index -= 1
    
    return "".join(s_array.items)

print(reverse_string('novak'))



def convert_int_to_bin(dec_num):
    numbers = Stack()
    div = dec_num
    str_rep = ""
    while div > 0:
        numbers.push(str((div % 2)))
   
        div = div // 2

    while not numbers.is_empty():
        str_rep += numbers.pop()
    return str_rep

print(convert_int_to_bin(42))