import heapq

class TestCase:
    def __init__(self):
        self.ip = "1\n2\n3\n\n1\n2"


def main():
    tc = TestCase()
    print(tc.ip)

    ip_file = '1_ip.txt'
    current_sum = 0
    heap = []
    try:
        with open(ip_file,'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    current_sum += int(line)
                else:
                    if (len(heap) < 3):
                        heapq.heappush(heap,current_sum)
                    else:
                        heap_min = heapq.heappop(heap)
                        to_insert = max(heap_min,current_sum)
                        heapq.heappush(heap,to_insert)
                    current_sum = 0
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except Exception as e:
        print(f"An error occured: {str(e)}")
    print(sum(heap))


if __name__=="__main__":
    main()


