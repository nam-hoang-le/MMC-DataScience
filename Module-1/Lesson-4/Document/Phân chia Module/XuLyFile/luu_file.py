def luu_file(du_lieu, ten_file, mode):
    with open(ten_file, mode) as file:
        file.write(str(du_lieu))
