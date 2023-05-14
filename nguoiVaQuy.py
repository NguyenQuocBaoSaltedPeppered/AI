# Người và Quỷ sang sông
import random as rand

# Vị trí thuyền 0: Trái. 1: Phải
# Số quỷ ở vị trí Thuyền
# Số người ở vị trí Thuyền

Start = [0, 3, 3]
Goal = [1, 3, 3]


def getChildren(O):
    ans = []
    if O[2] >= 2:
        N = [1 - O[0], 3 - O[1], 3 - O[2] + 2]
        if N[1] == N[2] or N[2] == 0 or N[2] == 3:
            ans.append(N)
    if O[2] >= 1:
        N = [1 - O[0], 3 - O[1], 3 - O[2] + 1]
        if N[1] == N[2] or N[2] == 0 or N[2] == 3:
            ans.append(N)

    if O[1] >= 2:
        N = [1 - O[0], 3 - O[1] + 2, 3 - O[2]]
        if N[1] == N[2] or N[2] == 0 or N[2] == 3:
            ans.append(N)
    if O[1] >= 1:
        N = [1 - O[0], 3 - O[1] + 1, 3 - O[2]]
        if N[1] == N[2] or N[2] == 0 or N[2] == 3:
            ans.append(N)

    if O[1] >= 1 and O[2] >= 1:
        N = [1 - O[0], 3 - O[1] + 1, 3 - O[2] + 1]
        if N[1] == N[2] or N[2] == 0 or N[2] == 3:
            ans.append(N)
    return ans


def printAll(O):
    Banthan = O[0]
    ToTien = O[1]
    if ToTien != None:
        printAll(ToTien)
    if Banthan[0] == 0:
        print(Banthan[1], Banthan[2], "t......", 3 - Banthan[1], 3 - Banthan[2])
    else:
        print(3 - Banthan[1], 3 - Banthan[2], "......t", Banthan[1], Banthan[2])


Open = []
Closed = []
OK = False
# 1. Cho đỉnh xuất phát vào open.
Open.append((Start, None))
Closed.append(Start)
# 2 - 6: Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
while len(Open) > 0:
    # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
    O = Open.pop(0)
    # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
    if O[0] == Goal:
        OK = True
        break
    # 5. Tìm tất cả các đỉnh con của ʘ, không thuộc open và closed cho vào cuối của open
    children = getChildren(O[0])
    for child in children:
        if child not in Closed:
            Open.insert(rand.randint(0, len(Open)), (child, O))

            # Open.insert(len(Open),(child,O)) # tìm kiếm theo chiều rộng
            # Open.insert(0,(child,O)) # tìm kiếm theo chiều sâu
            Closed.append(child)

if OK:
    print("Tìm kiếm thành công")
    printAll(O)
else:
    print("Tìm kiếm thất bại")
