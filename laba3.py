import copy


class Editor:
    @staticmethod
    def no_1_or_2_obj(leest):
        for i in leest:
            if len(i) == 1 or len(i) == 0:
                leest.remove(i)
        return leest

    @staticmethod
    def no_special_codes(leest):
        for i in leest:
            if i is i.isspace:
                leest.remove(i)
        iterator = 0
        for i in leest:
            leest[iterator] = i.replace('\n', '', 2)
            iterator += 1
        return leest

    @staticmethod
    def make_dam_lower(leest):
        leest_2 = []
        for i in leest:
            leest_2.append(i.lower())
        return leest_2

    @staticmethod
    def make_only_alph(leest):
        leest2 = copy.copy(leest)
        iterator = 0
        for i in leest:
            if ord(i[-1]) in range(ord('а'), ord('я')):
                pass
            else:
                leest2[iterator] = i[0: -2]
            iterator += 1
        return leest2


class Main:
    def wanna_sleep(self, leest, k):
        for i in leest:
            if i[1] == k:
                print(i[0])

    def no_1_or_0(self, slova):
        for i in slova:
            if len(i) == 1 or len(i) == 0:
                return Editor.no_1_or_2_obj(slova)
            else:
                return slova

    with open('test.txt', 'r') as j:
        data = j.read()
        rechennya = data.split('.')
        slova = []
        for i in rechennya:
            temporary_list = i.split(' ')
            for k in temporary_list:
                slova.append(k)

        slova = no_1_or_0(slova)
        slova = Editor.no_special_codes(slova)
        slova = Editor.make_dam_lower(slova)
        slova = Editor.make_only_alph(slova)

        c = ['а', 'я', 'у', 'е', 'и', 'о', 'ю', 'ё']
        dicta = []
        to_know_indexes = []
        for i in slova:
            num = 0
            for j in c:
                num += i.count(j)
            dicta.append([i, num])
        for i in dicta:
            to_know_indexes.append(i[1])
        to_know_indexes = sorted(set(to_know_indexes), reverse=True)
        for i in to_know_indexes:
            wanna_sleep(True, dicta, i)


if __name__ == '__main__':
    Main()