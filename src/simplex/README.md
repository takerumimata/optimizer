# 単体法をフルスクラッチで実装する

## 想定する線形計画問題
最終的には以下のような線形計画問題を解くソルバーが実装できると１００点！

```tex
max: CtX

s.t.    Ax <= b
        x >= 0
```

## まずは２変数で考える
X_1とX_2の２変数で考えよう
```
max:    X_1 + 2 * X_2
s.t.:   X_1 >= 0
        X_2 >= 0
        X_1 + X_2 <= 6
        X_1 + 3 * X_2 <= 12
        2* X_1 + X_2 <= 10
```

# Reference
[数理最適化をしっかり学ぶために2段階単体法を実装](https://yamagensakam.hatenablog.com/entry/2020/12/26/184808)