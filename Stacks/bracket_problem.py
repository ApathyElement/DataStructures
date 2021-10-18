from Stack import Stack

test_data = {'[{}]': True,
             '(()())': True,
             '{]': False,
             '[]{}({})': True, 
             '[()}))()': False,
             '({})[]': True}

def is_left(br):
    if br == '{' or br=='[' or br == '(':
        return True
    else:
        return False

def is_right(br):
    if br == '}' or br==']' or br == ')':
        return True
    else:
        return False

def matchingPair(l,r):
    if  (l == '(' and r == ')') or (r == '(' and l == ')') or \
        (l == '[' and r == ']') or (r == '[' and l == ']') or \
        (l == '{' and r == '}') or (r == '{' and l == '}'):
        return True
    else:
        return False

def check_Brackets(instr):
    st = Stack()
    for _ in instr:
        if is_left(_):
            st.push(_)
        if is_right(_):
            if matchingPair(st.peek(), _):
                st.pop()
            else:
                st.push(_)

    if st.pop() == None:
        return True
    else:
        return False



for Testval, correctness in test_data.items():
    if check_Brackets(Testval) == correctness:
        print(Testval, 'test succeeded !!')
    else:
        print(Testval, 'test Failed :(')