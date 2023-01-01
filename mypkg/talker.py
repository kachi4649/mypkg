import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

class Talker():          #ヘッダの下にTalkerというクラスを作成
    def __init__(self, node):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        # ↑ selfはオブジェクトのこと
        # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。
        node.create_timer(0.5, cb)

def cb(self):          #17行目で定期実行されるコールバック関数
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = self.n   #msgオブジェクトの持つdataにnを結び付け
    self.pub.publish(msg)        #pubの持つpublishでメッセージ送信
    self.n += 1
    
rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
talker = Talker(node)#オブジェクトを作成（__init__が実行される。）
rclpy.spin(node)


