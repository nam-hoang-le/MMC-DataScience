def doc_file(file_path,mode):
    with open(file_path, mode) as f:
        data = f.read()
    return data

