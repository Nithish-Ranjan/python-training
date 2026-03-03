def balance(exp):
    st = []
    for ch in exp:
        if ch in "({[":
            st.append(ch)
        
        elif ch in ")}]":
            if st == []:
                return False

            top = st.pop()

        if (ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '['):
            return False

    return len(st) == 0

s = input("enter expression : ")
n = balance(s)
print(n)