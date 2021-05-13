"""問題
材料AとBから合成できる化学製品XとYをたくさん作成したい。
Xを1kg作るのに、Aが1kg、Bが3kg必要である。
Yを1kg作るのに、Aが2kg、Bが1kg必要である。
また、XもYも1kg当りの価格は100円である。
材料Aは16kg、Bは18kgしかないときに、XとYの価格の合計が最大になるようにするには、
XとYをどれだけ作成すればよいか求めよ。
"""

from pulp import *

m = LpProblem(sense=LpMaximize)  # 数理モデル
x = LpVariable("x", lowBound=0)  # 変数
y = LpVariable("y", lowBound=0)  # 変数
m += 100 * x + 100 * y  # 目的関数
m += x + 2 * y <= 16  # 材料Aの上限の制約条件
m += 3 * x + y <= 18  # 材料Bの上限の制約条件
m.solve()  # ソルバーの実行
print(value(x), value(y))  # 4, 6
