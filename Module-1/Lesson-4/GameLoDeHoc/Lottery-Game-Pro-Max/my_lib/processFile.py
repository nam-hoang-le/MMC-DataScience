def write_file(data, path_file, mode): 
    try: 
        with open(path_file, mode) as file: 
            for line in data: 
                file.write(line)
    except Exception as e: 
        print(f"There is problem happened: {e}")

        

def read_file(path_file, mode): 
    try: 
        with open(path_file, mode) as file: 
            data = [line.strip().split(',') for line in file.readlines()]
        return data 
    except Exception as e: 
        print(f'There is problem in reading file: {e}')
        return None 
    

