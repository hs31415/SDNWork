from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel


def createCustomTopology():
    net = Mininet(controller=RemoteController)

    # 添加控制器
    c0 = net.addController('c0', ip='127.0.0.1', port=6633,protocols="tcp")

    # 添加交换机
    s1 = net.addSwitch('s1', protocols='OpenFlow13')
    s2 = net.addSwitch('s2', protocols='OpenFlow13')
    s3 = net.addSwitch('s3', protocols='OpenFlow13')
    s4 = net.addSwitch('s4', protocols='OpenFlow13')
    s5 = net.addSwitch('s5', protocols='OpenFlow13')
    s6 = net.addSwitch('s6', protocols='OpenFlow13')
    s7 = net.addSwitch('s7', protocols='OpenFlow13')
    s8 = net.addSwitch('s8', protocols='OpenFlow13')

    # 添加主机
    h1 = net.addHost('h1', ip="10.0.0.1")
    h2 = net.addHost('h2', ip="10.0.0.2")
    h3 = net.addHost('h3', ip="10.0.0.3")
    h4 = net.addHost('h4', ip="10.0.0.4")
    h5 = net.addHost('h5', ip="10.0.0.5")
    h6 = net.addHost('h6', ip="10.0.0.6")
    h7 = net.addHost('h7', ip="10.0.0.7")
    h8 = net.addHost('h8', ip="10.0.0.8")

    # 连接交换机和主机
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)
    net.addLink(s2, s3)
    net.addLink(s2, s4)
    net.addLink(s3, s5)
    net.addLink(s3, s6)
    net.addLink(s3, s7)
    net.addLink(s3, s8)
    net.addLink(s4, s5)
    net.addLink(s4, s6)
    net.addLink(s4, s7)
    net.addLink(s4, s8)
    
    net.addLink(s5, h1)
    net.addLink(s5, h2)
    net.addLink(s6, h3)
    net.addLink(s6, h4)
    net.addLink(s7, h5)
    net.addLink(s7, h6)
    net.addLink(s8, h7)
    net.addLink(s8, h8)

    # 启动拓扑
    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])
    s5.start([c0])
    s6.start([c0])
    s7.start([c0])
    s8.start([c0])

    # 打开命令行界面
    CLI(net)

    # 关闭拓扑
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    createCustomTopology()
