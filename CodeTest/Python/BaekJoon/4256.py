import sys
sys.stdin = open('input.txt')


def sol(preorder, inorder):
    if not preorder or not inorder:
        return

    node = preorder[0]
    idx = inorder.index(node)

    left = inorder[:idx]
    right = inorder[idx+1:]

    sol(preorder[1:len(left)+1], left)
    sol(preorder[len(left)+1:], right)
    print(node, end=' ')


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))

    sol(preorder, inorder)
    print()
