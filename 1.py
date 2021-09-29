# 1) Napište funkci over_zavorky(text), která vrací TRUE, pokud je text správně uzávorkovaný (závorky jsou správně otevřené a zavřené), jinak FALSE

def over_zavorky(string, stack_number):
    seznam_zavorek = list(string)
    stack = stack_number
    
    if stack >= 0:
        if len(seznam_zavorek) != 0:
            if seznam_zavorek.pop() == ")":
                return over_zavorky(seznam_zavorek, stack + 1)
            else:
                return over_zavorky(seznam_zavorek, stack - 1)
        elif len(seznam_zavorek) == 0 and stack == 0:
            return True
        else:
            return False
    else:
        return False







print(
over_zavorky(")))))))(((((((", 0)
)
