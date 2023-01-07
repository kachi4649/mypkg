# 課題2提出用
# ros2のインストール方法


## トピックの名前と型と説明
ノード：talker,listener
トピック：countup
talkerからlistenerに流路で連結している。
メッセージの型は16ビット符号付整数でこれを0.5秒ずつ送信されるようになっている。

# 実行方法
1.ubuntuの端末を二つにする。
2.一つ目の端末に
```
ros2 run mypkg talker
```
を実行する。
3.2つ目の端末に
```
ros2 run mypkg listener
```
を実行する。
## テスト環境

* ros2
* Ubuntu22.04

## ライセンス
BSD 3-Clause License
