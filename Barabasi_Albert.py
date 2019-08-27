import random as r
from graph import Graph
from itertools import combinations


def write_json(data):
    fo = open("network.json", "w+")
    fo.write(data)


def init_cond(initNode, threshold):
    node = []
    for i in range(1, initNode+1):
        network.add_vertex(i)
        node.append(i)

    comb = list(combinations(node, 2))

    for j in range(len(comb)):
        prob = r.random()
        if prob > threshold:
            network.add_edge({comb[j][0], comb[j][1]})

    return network


def cal_pi(node_i):
    kj = len(network.edges())
    ki = network.vertex_degree(node_i)
    pi = ki / (2*kj)
    return pi


def generate_ba(initNode, baNode):
    node = list(network.vertices())

    for newNode in range(baNode):
        N = newNode + initNode + 1
        network.add_vertex(N)
        node_list = r.sample(node, initNode)
        prob = r.random()
        for i in range(len(node_list)):
            pi = cal_pi(node_list[i])
            if prob > pi:
                network.add_edge((N, node_list[i]))
            else:
                pass
        node.append(N)
    return network


def generate_json_text():
    data = ''
    for link in range(len(network.edges())):
        node = str(network.edges()[link])
        v1 = (node.split("{"))[1].split(",")[0]
        v2 = (node.split(" "))[1].split("}")[0]
        data += ("[{\"host\":\"n%s\",\"net_id\":%d,\"label\":\"N%d\"}," % (v1, int(v1), int(v1)))
        data += ("{\"host\":\"n%s\",\"net_id\":%d,\"label\":\"N%d\"}]" % (v2, int(v2), int(v2)))
        if link != len(network.edges()) - 1:
            data += ","
        else:
            pass
        data = data + "\n"
    data = "[" + "\n" + data + "]"
    return data


if __name__ == "__main__":
    net = {}
    network = Graph(net)
    m0 = int(input("Input initNode: "))
    t = float(input("Input threshold level: "))
    n = int(input("Input numNode: "))
    init_cond(m0, t)
    print(generate_ba(m0, n))
    write_json(generate_json_text())
