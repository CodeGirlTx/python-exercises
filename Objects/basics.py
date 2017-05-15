
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique = 0
        self.greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        if other_person not in self.greeted:
            self.unique += 1
            self.greeted.append(other_person)
        self.greeting_count += 1

    def print_contact_info(self):
        print(self.email, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def add_num(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: {} {}'.format(self.name, self.phone)

    def num_unique_people_greeted(self):
        print(self.unique)






person1 = Person('Sonny', 'sonny@hotmail.com', '999-999-999')
person2 = Person('Jordan', 'jordan@aol.com', '888-888-888')

person1.add_friend(person2)
person1.add_num()

person2.greet(person1)
person1.greet(person2)
print(person1.greeting_count)
print(str(person2))
person1.num_unique_people_greeted()


#person1.print_contact_info()
#print(person1.email, person1.phone)
#print(person2.email, person2.phone)
