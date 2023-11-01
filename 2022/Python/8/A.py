
def solve():
    with open('input.txt','r') as file:
        lines = file.readlines() 
        lines = [list(entry.strip()) for entry in lines]
        lines = list(filter(lambda x: len(x) != 0,lines))
        print(lines)

def main():
    solve()

if __name__=="__main__":
    main()
