def solution(strings, n):
    ascii_index_matrix = []
    ascii_list = []
    ans = []
    for i in range(len(strings)):
        ascii_index_matrix.append([ord(strings[i][n]),i])
        ascii_list.append(ord(strings[i][n]))
    ascii_index_matrix.sort()
    for i in range(len(strings)):
        if len(ascii_list) == 0:
            break
        else:
            cnt = ascii_list.count(min(ascii_list))
            a = []
            for j in range(cnt):
                a.append(strings[ascii_index_matrix[0][1]])
                ascii_list.remove(min(ascii_list))
                ascii_index_matrix.remove(ascii_index_matrix[0])
            a.sort()
            ans += a
    return ans