from salary_increase import count_money
print('''定投十年翻十倍！
开始定投吧！
请选择你的定投计划：
0.个人加薪计划;
1.待创建;''')
option = int(input())
if option == 0:
    pe = int(input('请输入 PE '))
    result = count_money(pe)
    print('''经计算，本期应投入金额为''' + str(result))
else:
    print('待开发！')
