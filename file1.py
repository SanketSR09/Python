def count_lines(file_name):
    try:
        with open(file_name,'r') as file:
            content=file.read()

            n_lines=len(content.splitlines())
            n_words=len(content.split())
            n_char=len(content)

            print(n_lines)
            print(n_words)
            print(n_char)

    except FileNotFoundError:
        print(f"Error :File'{file_name}' not Found")
    
    except Exception as e:
        print(e)

if __name__=="__main__":
    file_name=input("Enter the File name: ")

    count_lines(file_name)