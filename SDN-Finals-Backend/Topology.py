from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel


def createCustomTopology():
    net = Mininet(controller=RemoteController)

    # 添加控制器
    c0 = net.addController('c0', ip='127.0.0.1', port=6633)

    # 添加交换机
    s1 = net.addSwitch('s1', protocols='OpenFlow13')

    # 添加主机
    h1 = net.addHost('h1', ip="10.0.0.1")
    h2 = net.addHost('h2', ip="10.0.0.2")
    h3 = net.addHost('h3', ip="10.0.0.3")

    # 连接交换机和主机
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    # 启动拓扑
    net.build()
    c0.start()
    s1.start([c0])

    # 打开命令行界面
    CLI(net)

    # 关闭拓扑
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    createCustomTopology()