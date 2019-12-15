import sys

books = []
users = []

flag = False


def login():
    print('请输入用户名：', end='')
    username = input()
    print('请输入密码：', end='')
    password = input()
    if [username, password] in users:
        print('登录成功！')
        flag = True
        fun()
    else:
        print('用户名或密码错误！请重新登录！')


def register():
    print('请输入用户名：', end='')
    username = input()
    print('请输入密码：', end='')
    password = input()
    users.append([username, password])
    print('注册成功！')


def main():
    while True:
        print('\n\n')
        print('********************************************')
        print('********************************************')
        print('********************************************')
        print('*************欢迎来到图书管理系统*************')
        print('************Made by Chen Chunhan************')
        print('********************************************')
        print('*************** 1.Log in     ***************')
        print('*************** 2.Register   ***************')
        print('*************** 0.Exit       ***************')
        print('********************************************')
        print('********************************************')
        print('********************************************')
        num = int(input('请输入对应的数字：'))
        if num == 1:
            login()
        elif num == 2:
            register()
        elif num == 0:
            sys.exit(0)


def fun():
    while True:
        print('\n\n')
        print('********************************************')
        print('********************************************')
        print('********************************************')
        print('**********  1.More Books          **********')
        print('**********  2.Delete Books        **********')
        print('**********  3.Search for Books    **********')
        print('**********  4.Change Information  **********')
        print('**********  5.View All Books      **********')
        print('**********  6.Back to Main Menu   **********')
        print('**********  0.Exit                **********')
        print('********************************************')
        print('********************************************')
        print('********************************************')
        num = int(input('请输入对应的数字：'))
        print('\n')
        if num == 1:
            bookname = input('请输入书名：')
            author = input('请输入作者：')
            press = input('请输入出版社：')
            price = input('请输入书籍定价：')
            amount = input('请输入书籍数目：')
            books.append([bookname, author, press, price, amount])
            print('\n添加书籍成功！')
        elif num == 2:
            bookname = input('请输入书名：')
            author = input('请输入作者：')
            press = input('请输入出版社：')
            price = input('请输入书籍定价：')
            amount = input('请输入书籍数目：')
            if [bookname, author, press, price, amount] in books:
                books.remove([bookname, author, press, price, amount])
                print('\n删除书籍成功！')
            else:
                print('\n该书籍不存在！自动返回...')
        elif num == 3:
            bookname = input('请输入书名：')
            j = 0
            for i in books:
                if i[0] == bookname:
                    j = 1
                    print('书名：', i[0])
                    print('作者：', i[1])
                    print('出版社：', i[2])
                    print('定价：', i[3])
                    print('数目：', i[4])
            if j == 0:
                print('\n该书籍不存在！自动返回...')
            print('\n查找结束\n')
        elif num == 4:
            bookname = input('请输入要修改的书名：')
            author = input('请输入要修改的作者：')
            press = input('请输入要修改的出版社：')
            price = input('请输入要修改的书籍定价：')
            amount = input('请输入要修改的书籍数目：')
            if [bookname, author, press, price, amount] in books:
                books.remove([bookname, author, press, price, amount])
                bookname = input('请输入修改后的书名：')
                author = input('请输入修改后的作者：')
                press = input('请输入修改后的出版社：')
                price = input('请输入修改后的书籍定价：')
                amount = input('请输入修改后的书籍数目：')
                books.append([bookname, author, press, price, amount])
                print('\n修改书籍成功！')
            else:
                print('\n该书籍不存在！自动返回...')
        elif num == 5:
            print('{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:<20s}'.format('Bookname', 'Author', 'Press', 'Price', 'Amount'),
                  end='')
            print()
            for i in books:
                print('{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:<20s}'.format(i[0], i[1], i[2], i[3], i[4]), end='')
                print()
        elif num == 6:
            main()
        elif num == 0:
            sys.exit(0)


main()
