# 1) Napište funkci over_zavorky(text), která vrací TRUE, pokud je text správně uzávorkovaný (závorky jsou správně otevřené a zavřené), jinak FALSE

def over_zavorky(string, stack_number):
    seznam_zavorek = list(string)
    stack = stack_number
    
    if stack < 0:
        return False
    else:
        if len(seznam_zavorek) != 0:
            if seznam_zavorek.pop() == ")":
                return over_zavorky(seznam_zavorek, stack + 1)
            else:
                return over_zavorky(seznam_zavorek, stack - 1)
        elif len(seznam_zavorek) == 0 and stack == 0:
            return True
        else:
            return False

# print(
# over_zavorky(")))))))((((((())))", 0)
# )


def my_flatten(lists):
    flatten_list = []

    for i in lists:
        if type(i) is not list:
            flatten_list.append(i)
        else:
            flatten_list.extend(my_flatten(i))

    return flatten_list


# seznamy = [100, 200, 300, [1, 2, 3, [10, 20, 30]]]
# print(
#     my_flatten(seznamy)
# )

