import xlrd
# dijkstra算法实现，有向图和路由的源点作为函数的输入，最短路径最为输出
def dijkstra(graph,src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=[]  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i]=graph[src][i]  # 初始化
    # print(distance)
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        mid_distance=float('inf')
        for v in visited:
            print(v)
            for d in nodes:
                print('d:', d)
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=new_distance  # 进行距离更新
                    k=d
                    pre=v
        distance[k]=mid_distance  # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
        print(visited,nodes)  # 输出节点的添加过程
    return distance,path


def handle_excel(filepath):
    matrix = [[0 for i in range(50)] for i in range(50)]
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[1]
    a = table.nrows
    b = table.ncols
    for i in range(1, a):
        for j in range(1, b):
            m = i-1
            n = j-1
            matrix[m][n] = table.cell(i, j).value
            if matrix[m][n] == '∞':
                matrix[m][n] = float('inf')
    return matrix


if __name__ == '__main__':
    graph = handle_excel('E:\paper\est.xlsx')

    distance,path= dijkstra(graph, 0)  # 查找从源点0开始带其他节点的最短路径
    print(distance,path)