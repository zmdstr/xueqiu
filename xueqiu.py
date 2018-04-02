from salary_increase import count_money

while True:
    print('''
    定投十年翻十倍!
    开始定投吧!
    0.个人加薪计划,
    1.退出;''')
    option = int(input('请选择你的定投计划:\n'))
    if option == 0:
        pe = float(input('请输入市盈率(PE):\n'))
        result = count_money(pe)
        print('''经计算，本期应投入金额为: %d 元！''' % result)
    else:
        break
