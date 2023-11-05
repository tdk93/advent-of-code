import heapq

def process_input():
    ip_file = '1_ip_test.txt'
    with open(ip_file, encoding="utf-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(int,elf.strip().split("\n"))) for elf in elves]

def main():
    x = process_input()
    print("what is x", x)

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


