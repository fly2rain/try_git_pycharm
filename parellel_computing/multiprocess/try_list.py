if __name__ == '__main__':
    xx = list(range(10))
    yy = xx[2:8]
    yy[0] = 100
    yy[-1] = 1000
    print(xx, yy)