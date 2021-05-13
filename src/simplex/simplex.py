import numpy as np

"""問題
max:    X_1 + 2 * X_2
s.t.:   X_1 >= 0
        X_2 >= 0
        X_1 + X_2 <= 6
        X_1 + 3 * X_2 <= 12
        2* X_1 + X_2 <= 10
"""


def main():
    """limitation
    1. 与えられる変数は非負制約を持つ
    2. 制約条件は全て標準形で与えられる。すなわち Xi <= bi の形式で与えられるものとする
    """

    # n = input("変数の数を入力してください: ")
    # m = input("制約条件の数を入力してください: ")
    # print(f"変数の数は{n}個, 制約条件の数は{m}個です")
    # print("係数行列を入力してください")

    # matrix = [input().split() for i in range(int(m) + 1)]
    # print(matrix)

    cost = np.array([1, 2])

    # 規定行列を作る
    basic_matrix = np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )

    # 非規定行列を作る
    nonbasic_matrix = np.array(
        [
            [1, 1],
            [1, 3],
            [2, 1],
        ]
    )

    # 扱う行列
    mx = np.array(
        [
            [1, 2, 0, 0, 0, 0],  # 目的関数（ここがどちらも負になったらおしまい）
            [1, 1, 1, 0, 0, 6],  # 制約関数① + スラック変数①
            [1, 3, 0, 1, 0, 12],  # 制約関数② + スラック変数②
            [2, 1, 0, 0, 1, 10],  # 制約関数③ + スラック変数③
        ]
    )

    inv_b = np.linalg.inv(basic_matrix)
    print(inv_b)

    b = np.array([6, 12, 10])
    print(np.dot(inv_b, b))


if __name__ == "__main__":
    main()
