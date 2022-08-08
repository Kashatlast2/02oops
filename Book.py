#Book
class Book:
    def __init__(self, name, copies = 0):
        self.name = name
        self.copies = copies
    def increase_copies(self, how_much):
        self.copies += how_much
    def decrease_copies(self, how_much):
        self.copies -= how_much

hyena = Book('Hyena', 50)
how_to_think_like_leo = Book('How To Think Like Leonardo Da Vinci')
permanent_record = Book('Permanent Record')

hyena.name = 'Hyena'
how_to_think_like_leo.name = 'How To Think Like Leonardo Da Vinci'
permanent_record.name = 'Permanent Record'


print(hyena.name)
print(how_to_think_like_leo.name)
print(permanent_record.name)

hyena.increase_copies(25)
hyena.decrease_copies(10)

print(hyena.copies)