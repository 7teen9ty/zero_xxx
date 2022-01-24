class Crest:
    pos_crest = 0

    def position(self):
        self.pos_crest = int(input('Выберите позиция для вашего хода: '))

    def cheker_x(self):
        if self.pos_crest in Pit.pit['0'] or self.pos_crest in Pit.pit['X']:
            print('Данное место уже занято')
            self.position()
            self.cheker_x()
        else:
            Pit.pit['X'].append(self.pos_crest)


class Zero:
    pos_zero = 0

    def position(self):
        self.pos_zero = int(input('Выберите позиция для вашего хода: '))

    def cheker_z(self):
        if self.pos_zero in Pit.pit['0'] or self.pos_zero in Pit.pit['X']:
            print('Данное место уже занято')
            self.position()
            self.cheker_z()
        else:
            Pit.pit['0'].append(self.pos_zero)

class Pit:
    pit = {'0': [], 'X': []}
    pit['0'], pit['X'] = sorted(pit['0']), sorted(pit['X'])

    def winner(self):
        if len(self.pit['0']) >= 3 and isinstance(self.pit['0'][2], int) or len(self.pit['X']) >= 3 and isinstance(self.pit['X'][2], int):
            if sum(self.pit['0'][0:3]) == 6 or sum(self.pit['0'][0:3]) == 12 or sum(self.pit['0'][0:3]) == 15 or sum(self.pit['0'][0:3]) == 24 or sum(self.pit['0'][0:3]) == 18:
                print('Победа Ноликов')
                return False
            if sum(self.pit['X'][0:3]) == 6 or sum(self.pit['X'][0:3]) == 12 or sum(self.pit['X'][0:3]) == 15 or sum(self.pit['X'][0:3]) == 24 or sum(self.pit['X'][0:3]) == 18:
                print('Победа Крестиков')
                return False


class Table:
    z = 0

    def position(self):
        self.z = 0
        for i in range(1, 4):
            for j in range(3):
                self.z += 1
                a = self.z
                for i_zero in Pit.pit['0']:
                    if i_zero == self.z:
                        self.z = '0'
                for i_crest in Pit.pit['X']:
                    if i_crest == self.z:
                        self.z = 'X'
                print(self.z, end='\t')
                self.z = a
            print()

table = Table()
crest = Crest()
zero = Zero()
pit = Pit()
table.position()
while True:
    crest.position()
    crest.cheker_x()
    table.position()
    if pit.winner() == False:
        break
    zero.position()
    zero.cheker_z()
    table.position()
    if pit.winner() == False:
        break
