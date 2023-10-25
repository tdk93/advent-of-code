class TestCase:
    def __init__(self):
        self.ip = "1\n2\n3\n\n1\n2"


def main():
    tc = TestCase()
    print(tc.ip)

    ip_file = '1_ip.txt'
    current_sum = 0
    max_so_far = 0
    try:
        with open(ip_file,'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    current_sum += int(line)
                else:
                    max_so_far = max(max_so_far,current_sum)
                    current_sum = 0
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except Exception as e:
        print(f"An error occured: {str(e)}")
    print(max_so_far)


if __name__=="__main__":
    main()


