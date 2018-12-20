import xlrd
from tkinter import *

'''
   上面导入的两个包，一个是用文件处理的，一个是gui设计用的。
   dijkstra函数实现主要功能，返回path路径，因为找到最短路径就更新相应的距离值，所以访问就可以。
   然后就是一个处理导入excel文件的数据函数，将其转化为50*50的矩阵。
   最后就是python的gui真的没有java好用，而且书上说的太少，所以现学现卖，gui做的很难看。
   关键我是个新手，实在太难了，里面有很多错误。
'''

def dijkstra(matrix, src):
        nodes = [i for i in range(0, len(matrix))]
        visited = [src]
        if src in nodes:
            nodes.remove(src)             # 将源点从未置顶点集中删除
        else:
            return None
        k = pre = src
        path = {src: {src: [src]}}        # 用来记录最短路径
        while nodes:                      # dijkstra算法实现部分
            mid_distance = float('inf')   # 存在一个我解决不了的问题，在筛选置顶节点时候，没有好的方法，出现断路好像得回溯，也不会操作，寒假我要重新写一下
            for v in visited:
                for d in nodes:
                        new_distance = matrix[src][v] + matrix[v][d]
                        if new_distance < mid_distance:
                            mid_distance = new_distance
                            matrix[src][d] = new_distance
                            matrix[d][src] = matrix[d][src]
                            k = d
                            pre = v
            path[src][k] = path[src][pre] + [k]
            nodes.remove(k)
            visited.append(k)
        for d in range(50):                                  # 这部分是修补异常的情况
            if path[src][d] == [src, d]:
                path[src][d] = path[src][abs(d-1)] + [d]
        for r in range(50):
            if len(path[src][r]) > 2:
                a = path[src][r]
                if a[1]-a[0] > 2:
                    path[src][r] = path[src][a[1]] + a[2:]

        return path


def get_distance(start, end):
    return matrix[start][end]


def handle_excel(filepath):                          # 处理excel数据
    matrix = [[0 for i in range(50)] for i in range(50)]
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[1]
    a = table.nrows
    b = table.ncols
    # print(a, b)
    for i in range(1, a):
        for j in range(1, b):
            m = i-1
            n = j-1
            matrix[m][n] = table.cell(i, j).value
            if matrix[m][n] == '∞':
                matrix[m][n] = float('inf')
    return matrix


def clicked():                        # gui设计
    a = int(var1.get())
    b = int(var2.get())
    c = dijkstra(matrix, a)
    string1 = "->".join('%s' %id for id in c[a][b])
    text1.delete(1.0, END)
    text1.insert(INSERT, '最短路径为：\n')
    text1.insert(INSERT, string1+'\n')
    text1.insert(INSERT, '最短路径长度为：\n')
    text1.insert(INSERT,  str(matrix[a][b])+ '\n')
    text1.insert(END, '时间复杂度为:\n o(n^2)')
    text1.pack()


if __name__ == '__main__':
    matrix = handle_excel('.//est.xlsx')        # 这个地方改为相对路径，与python文件同目录下,就可以打开了
    # print(matrix)
    c = dijkstra(matrix, 1)
    top = Tk()
    top.title('dijkstra算法')
    top.geometry('400x400')
    btn = Button(command=clicked)
    text1 = Text(width=100, height=20, fg='red')
    Alabel = Label(text='请在下面两个框输入起终点：').pack(fill=BOTH, ipadx=20, ipady=20)
    var1 = StringVar()
    var2 = StringVar()
    entry1 = Entry(textvariable=var1).pack(side=TOP, ipadx=2, ipady=5)
    entry2 = Entry(textvariable=var2).pack(side=TOP, ipadx=2, ipady=5)
    btn['text'] = '启动'
    btn.pack(ipadx=20, ipady=10, side="bottom")
    top.mainloop()
