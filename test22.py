import xlrd


def dijkstra(matrix, src):
        nodes = [i for i in range(0, len(matrix))]
        visited = [src]
        if src in nodes:
            nodes.remove(src)
        else:
            return None
        k = pre = src
        path = {src: {src: [src]}}
        while nodes:
            mid_distance = float('inf')
            for v in visited:
                for d in nodes:
                        new_distance = matrix[src][v] + matrix[v][d]
                        print(matrix[src][v], matrix[v][d])
                        if new_distance < mid_distance:
                            mid_distance = new_distance
                            matrix[src][d] = new_distance
                            matrix[d][src] = matrix[d][src]
                            k = d
                            pre = v
                            print(pre, k)
                        path[src][pre] = [src, pre]
            print(matrix[src][1], matrix[1][2])
            path[src][k] = path[src][pre] + [k]
            print(nodes, k)
            nodes.remove(k)
            visited.remove(pre)
            visited.append(k)
            # print(visited, nodes)
        print(matrix[0][2])
        return path


def get_distance(start, end):
    return matrix[start][end]


def handle_excel(filepath):
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


if __name__ == '__main__':
    matrix = handle_excel('E:\paper\est.xlsx')
    # print(matrix)
    a = dijkstra(matrix, 0)
    # for i in range(50):
    print(a[0][2])
