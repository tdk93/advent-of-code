ip_file = '1_ip.txt'

try:
    with open(ip_file,'r') as file:
        content = file.read()

        print(content)



except FileNotFoundError:
    print(f"File '{file_path}' not found")
except Exception as e:
    print(f"An error occured: {str(e)}")
