# SDNWork

这是一个SDN课程的大作业。



## 部署方法

#### 环境：ubuntu20.04，mininet，opendaylight控制器，java 1.8.0，python3，node.js

1、先启动opendaylight控制器，构建拓扑(Backend文件夹下的Topology.py)并连接到odl控制器。

2、运行Backend文件夹下的Backend.py。

3、在Frontend文件夹下执行npm install之后npm run dev。（需要安装npm，使用了vue）

4、第三步运行结束后进入出现的网址即可。

ps：可能出现端口冲突，换一个或者关闭原有的端口就行。

## 目前实现的功能：

## 1、拓扑搭建

​	选择了拓扑一，单交换机，三主机的拓扑。主机ip分别为10.0.0.1、10.0.0.2、10.0.0.3

## 2、网络测量

#### 	1、数据包构建

​		每次可发送100个数据包。

#### 	2、流量统计

​		可查看三个主机间的数据包，包含源 IP、目的 IP、源端口、目的端口、传输层协议，并统计每条流出现	的次数

## 3、系统集成

#### 	1、拓扑查看

​		可在web前端查看拓扑

#### 	2、流量统计

​		可查看每条流出现的次数

#### 	3、流量分析

​		将拓扑主机间的数据包根据流量排序
