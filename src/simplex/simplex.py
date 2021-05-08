import numpy as np
# import argparse

"""問題
max:    X_1 + 2 * X_2
s.t.:   X_1 >= 0
        X_2 >= 0
        X_1 + X_2 <= 6
        X_1 + 3 * X_2 <= 12
        2* X_1 + X_2 <= 10
"""

def main():
    n = input("変数の数を入力してください: ")
    m = input("制約条件の数を入力してください: ")
    print(f"変数の数は{n}個, 制約条件の数は{m}個です")
    print("係数行列を入力してください")

    a = [int(input()) for i in range(n)]


if __name__=="__main__":
    main()