def loading_bar(percentage: int):
    if percentage // 10 == 10:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        percentage_for_for = percentage // 10
        graphic = []
        for i in range (1, 11):
            if i <= percentage_for_for:
                graphic.append('%')
            else:
                graphic.append('.')
        print(f'{percentage_for_for * 10}% [{"".join(graphic)}]')
        print('Still loading...')

num = int(input())
loading_bar(num)