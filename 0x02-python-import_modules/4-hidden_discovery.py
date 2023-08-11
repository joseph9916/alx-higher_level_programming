#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden = sorted(dir(hidden_4))
    for name in hidden:
        if name[0:2] != "__":
            print("{:s}".format(name))
