import random as r


def write_json(data):
    fo = open("network.json", "w+")
    fo.write(data)


def generate_random_network(numNode, threshold):
    connection = []
    for i in range(1, numNode+1):
        for j in range(1, numNode+1):
            prob = r.random()
            if i != j and prob > threshold and ([j, i] not in connection):
                connection.append([i, j])
    network = str(generate_json_text(connection))

    return network


def generate_json_text(connection):
    data = ''
    for link in range(len(connection)):
        node = connection[link]
        data += ("[{\"host\":\"n%s\",\"net_id\":%d,\"label\":\"N%d\"}," % (node[0], node[0], node[0]))
        data += ("{\"host\":\"n%s\",\"net_id\":%d,\"label\":\"N%d\"}]" % (node[1], node[1], node[1]))
        if link != len(connection) - 1:
            data += ","
        else:
            pass
        data = data + "\n"
    data = "[" + "\n" + data + "]"
    return data


if __name__ == "__main__":
    numNode = int(input("Insert number of nodes: "))
    threshold = float(input("Insert threshold level (x.xx): "))
    con = generate_random_network(numNode, threshold)
    write_json(con)
