# ==== unittest ====

def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err
        # we can also raise the error
        # raise err
