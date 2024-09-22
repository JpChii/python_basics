def print_with_new_line(text):
    try:
        if text != "":
            print(text)
        print("-"*100)
    except Exception as e:
        print(e)
        print("-"*100)