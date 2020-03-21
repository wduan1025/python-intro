def show_complex(x):
    printed_real = str(x.real)
    if not x.img == 0:
        printed_img = str(x.img)+'i'
    else:
        printed_img = ""
    return printed_real + printed_img