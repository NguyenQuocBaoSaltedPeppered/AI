# Trò chơi 8 số
import random as rand


def ZeroPos(O):
    for i in range(n):
        for j in range(n):
            if O[i][j] == 0:
                return i, j


def Up(O):
    i, j = ZeroPos(O)
    if i < n - 1:
        N = [O[_][:] for _ in range(n)]
        N[i][j] = N[i + 1][j]
        N[i + 1][j] = 0
        return N
    else:
        return None


def Down(O):
    i, j = ZeroPos(O)
    if i > 0:
        N = [O[_][:] for _ in range(n)]
        N[i][j] = N[i - 1][j]
        N[i - 1][j] = 0
        return N
    else:
        return None


def Left(O):
    i, j = ZeroPos(O)
    if j < n - 1:
        N = [O[_][:] for _ in range(n)]
        N[i][j] = N[i][j + 1]
        N[i][j + 1] = 0
        return N
    else:
        return None


def Right(O):
    i, j = ZeroPos(O)
    if j > 0:
        N = [O[_][:] for _ in range(n)]
        N[i][j] = N[i][j - 1]
        N[i][j - 1] = 0
        return N
    else:
        return None


def getChildren(O):
    ans = []
    if Up(O) != None:
        ans.append(Up(O))
    if Down(O) != None:
        ans.append(Down(O))
    if Left(O) != None:
        ans.append(Left(O))
    if Right(O) != None:
        ans.append(Right(O))
    return ans


n = 3
Goal = [[(i * n + j + 1) % (n * n) for j in range(n)] for i in range(n)]
Start = [Goal[i][:] for i in range(n)]

for _ in range(1000):
    r = rand.randint(0, 3)
    if r == 0:
        Next = Up(Start)
    elif r == 1:
        Next = Down(Start)
    elif r == 2:
        Next = Left(Start)
    elif r == 3:
        Next = Right(Start)
    if Next != None:
        Start = Next


def printAll(O):
    Banthan = O[0]
    ToTien = O[1]
    if ToTien != None:
        printAll(ToTien)
    for i in range(n):
        for j in range(n):
            print(Banthan[i][j], end=" ")
        print()
    print("----------")


Open = []
Closed = set()
OK = False

# 1. Cho đỉnh xuất phát vào open.
Open.append((Start, None))
Closed.add(str(Start))
count = 0

# 2 - 6: Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
while len(Open) > 0:
    count += 1
    # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
    O = Open.pop(0)
    # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
    if O[0] == Goal:
        OK = True
        break
    # 5. Tìm tất cả các đỉnh con của ʘ, không thuộc open và closed cho vào cuối của open
    children = getChildren(O[0])
    for child in children:
        if str(child) not in Closed:
            # Open.insert(rand.randint(0,len(Open)),(child,O))

            Open.insert(len(Open), (child, O))  # tìm kiếm theo chiều rộng
            # Open.insert(0,(child,O)) # tìm kiếm theo chiều sâu
            Closed.add(str(child))

if OK:
    print("Tìm kiếm thành công")
    printAll(O)
else:
    print("Tìm kiếm thất bại")
print(count)
