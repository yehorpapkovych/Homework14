class Mathematician:

    def square_nums(self, list1):
        return [i*i for i in list1]

    def remove_positives(self, list1):
        return [i for i in list1 if i < 0]

    def filter_leaps(self, list1):
        return [i for i in list1 if i % 4 == 0 or i % 100 == 0]

m = Mathematician()
l = [45, -4, 7, 22, -6]
print(m.square_nums(l))
print(m.remove_positives(l))
d = [2000, 1900, 2025, 2006, 2022, 2020]
print(m.filter_leaps(d))