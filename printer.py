for a in range(1, 6):
    for b in range(1, 17):
        print 'self.push_' + str(a) + '_' + str(b) + '.clicked.connect(lambda: self.changeColor('+str(a)+','+str(b)+'))'