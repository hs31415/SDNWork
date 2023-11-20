import asyncio
import uvicorn
import scapy
import threading
from scapy.layers.inet import *
from fastapi import FastAPI, Body
from scapy.sendrecv import send, sniff, AsyncSniffer
from pydantic import BaseModel
from CountMinSketch import CountMinSketch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# 添加跨域请求中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源的跨域请求，也可以设置为特定的来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头
)
tableSize = 1000
hashFuncCount = 5
count = 100
address = ["10.0.0.1", "10.0.0.2", "10.0.0.3","10.0.0.4","10.0.0.5","10.0.0.6","10.0.0.7","10.0.0.8"]
port = {
    "10.0.0.1": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.2": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.3": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.4": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.5": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.6": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.7": {
        "sport": 1234,
        "dport": 1234
    },
    "10.0.0.8": {
        "sport": 1234,
        "dport": 1234
    }
}

sketch = CountMinSketch(tableSize, hashFuncCount)


class Item(BaseModel):
    src: str
    dst: str
    sport: str
    dport: str


def Callback(packet):
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        sport = str(packet[TCP].sport)
        dport = str(packet[TCP].dport)
        key = src_ip + '-' + dst_ip + '-' + sport + '-' + dport + '-TCP'
        print(key)
        sketch.add(key)


@app.get("/send")
async def Send():
    packets = []
    for _ in range(0, count):
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        while i == j:
            j = random.randint(0, 7)

        package = IP(src=address[i], dst=address[j]) / TCP(sport=port[address[i]]["sport"],
                                                           dport=port[address[j]]["dport"])
        send(package)
        packets.append(package)


async def start_sniffing():
    sniff(filter="tcp", prn=Callback)


@app.get("/sniff")
async def Sniff():
    t = AsyncSniffer(store=0, prn=lambda x: Callback(x))
    t.start()


@app.get("/clear")
async def Clear():
    sketch = CountMinSketch(tableSize, hashFuncCount)


@app.post("/sketch")
async def Sketch(item: Item = Body(...)):
    key = item.src + '-' + item.dst + '-' + item.sport + '-' + item.dport + '-TCP'
    return {"Key": key, "Value": sketch.get(key)}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True)
