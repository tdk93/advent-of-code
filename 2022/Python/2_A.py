
def solve():
    mapping_a = {'A': 1, 'B': 2, 'C': 3}
    mapping_b = {'X': 1, 'Y': 2, 'Z': 3}

    ip_file = '2_a.txt'
    score = 0
    try:
        with open('test_file.txt','r') as file:
            for line in file:
                move = line.split()
                if len(move) != 2:
                    continue

                print(move)
                if mapping_b[move[1]] > mapping_a[move[0]]:
                    score += 6
                elif mapping_b[move[1]] == mapping_a[move[0]]:
                    score += 3 

                score += mapping_b[move[1]]
            print(score)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Received error: {e}")

def main():
    solve()

if __name__=="__main__":
    main()

