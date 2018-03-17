from datetime import date


def count_money(pe):
    begin_year = date(2018, 3, 17).year
    begin_month = date(2018, 3, 17).month
    today_year = date.today().year
    today_month = date.today().month
    num = (begin_year-today_year)*12 + begin_month - today_month
    result = 1000*1.01**num*(10/pe)
    return result

