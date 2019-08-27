def extract_data(node):
    info = {}
    for trf in range(len(data) - 1):
        if node in data[trf] and data[trf][0] == "r":
            time = float((data[trf].split(" "))[1])
            pktSize = float((data[trf].split("length: "))[1].split(" ")[0])
            info.__setitem__(time, pktSize)
        else:
            pass
    return info


def cal_throughput(interval, info):
    time = sorted(info.keys());
    start = 0
    end = interval
    size = 0
    for lg in range(len(info)):
        #print(time[lg], info[time[lg]])
        pktSize = info[time[lg]]
        #print(pktSize)
        if time[lg] > end or lg == len(info) -1:
            size += pktSize
            throughput = size / interval
            #print("size, tp = " + str(size), str(throughput))
            print(throughput)
            start += interval
            end += interval
            size = 0
        elif start <= time[lg] <= end:
            size += pktSize


if __name__ == "__main__":
    filename = str(input("Filename: "))
    rx = str(input("NodeList/? : "))
    interval = float(input("Sampling rate (per second): "))
    with open(filename, "r") as myfile:
        data = myfile.read().split('\n')
    info_rx = extract_data("NodeList/1") #receiver
    cal_throughput(interval, info_rx)
