import numpy as np

"""問題
max:    X_1 + 2 * X_2
s.t.:   X_1 >= 0
        X_2 >= 0
        X_1 + X_2 <= 6
        X_1 + 3 * X_2 <= 12
        2* X_1 + X_2 <= 10
"""

class Simplex:
    def __init__(self) -> None:
        self.matrix = np.array(
            [
                [1.0, 1.0, 1.0, 0.0, 0.0, 6.0],  # 制約関数① + スラック変数①
                [1.0, 3.0, 0.0, 1.0, 0.0, 12.0],  # 制約関数② + スラック変数②
                [2.0, 1.0, 0.0, 0.0, 1.0, 10.0],  # 制約関数③ + スラック変数③
                [-1.0, -2.0, 0.0, 0.0, 0.0, 0.0],  # 目的関数（ここが全部負になったらおしまい）
            ]
        )
        self.N_Col = len(self.matrix[0])    # 6
        self.N_Row = len(self.matrix)   # 4

    def run(self):
        # select column 
        i = 1
        while True:
            print(f"--- {i}回目 ---")
            _min, _column = self._select_column(100)
            print(f"min: {_min}")
            print(f"column: {_column}")
            if _min >= 0:
                break
            if i > 10:
                break
            _min, _row = self._select_row(column=_column)
            print(f"min: {_min}")
            print(f"row: {_row}")
            self._divide_pivot(column=_column, row=_row)
            self._sweep(column=_column, row=_row)
            i += 1
        # 掃き出し法で求解したので、右上に解が出ているはず
        ans = self.matrix[-1][-1]
        print(f"answer is {ans}")
        print(self.matrix)

    def _select_column(self, min):
        """select_column
        ピボットする列の選択をする。被約費用を見ていって、最大のものを見つけて返す

        Parameter
        ----------
        self: self
            インスタンス

        Return
        ----------
        max: int
            最小の被約費用
        column: int
            最小の被約費用を持つ列
        """
        # min = 100
        column = 0
        for i in range(len(self.matrix[0]) - 1):    # 列の数だけループする
            # if self.matrix[-1][i] < min: # and self.matrix[0][i] != 0:
            #     min = self.matrix[-1][i]
            #     column = i
            if self.matrix[self.N_Row - 1][i] >= min:
                    continue
            min, column = self.matrix[self.N_Row - 1][i], i
        return [min, column]

    def _select_row(self, column: int):
        """select_row
        ピボットするための行の選択。一番小さい数字を選択する

        Parameter
        ----------
        self: self
            インスタンス
        column: int
            _select_columnで求めたカラム

        Return
        ----------
        xxx
        """
        mn = 100
        for i in range(self.N_Row - 1):   # 
            _p = self.matrix[i][self.N_Col - 1] / self.matrix[i][column]
            if self.matrix[i][column] <= 0 or _p >= mn:
                continue 
            # if _p < min and self.matrix[i][column] > 0:
            mn, row = _p, i
        return [mn, row]

    def _divide_pivot(self, column: int, row: int):
        """pivot
        ピボットで対象行の値を割っていく
        """
        piv = self.matrix[row][column]
        for i in range(len(self.matrix[0])):
            self.matrix[row][i] /= piv


    def _sweep(self, column: int, row: int):
        """sweep
        掃き出し法による辞書の更新処理
        """
        for i in range(len(self.matrix)):
            if i == row:
                continue
            d = self.matrix[i][column]
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] -= d * self.matrix[row][j]

    

def main():
    """limitation
    1. 与えられる変数は非負制約を持つ
    2. 制約条件は全て標準形で与えられる。すなわち Xi <= bi の形式で与えられるものとする
    """
    obj = Simplex()
    obj.run()


if __name__ == "__main__":
    main()
