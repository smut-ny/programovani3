# 1) Napište funkci over_zavorky(text), která vrací TRUE, pokud je text správně uzávorkovaný (závorky jsou správně otevřené a zavřené), jinak FALSE

from ssl import VERIFY_X509_STRICT


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


def get_fibo(number):

    if number < 2:
        return number
    else:
        return get_fibo(number - 1) + get_fibo(number - 2)


def get_fibo_it(number):
    range_list = [i for i in range(0, number)]
    vysledek = []
    vysledek_lich = 1
    vysledek_sud = 1

    for i in range_list:

        if i < 2:
            vysledek.extend([1])
        else:
            if i % 2 == 1:
                vysledek_lich += vysledek_sud
                vysledek.extend([vysledek_lich])
            else:
                vysledek_sud += vysledek_lich
                vysledek.extend([vysledek_sud])
    return vysledek

