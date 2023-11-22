class Contact:
    def __init__(self, user, country_code, phone_number):
        self.user = user
        self.country_code = country_code
        self.phone_number = phone_number


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def get_contacts_by_country(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]

    def get_contacts_by_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]


class User:
    def __init__(self, login, first_name, last_name):
        self.login = "@" + login
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []
        self.phone_books = {}

    def add_friend(self, user):
        self.friends.append(user)

    def remove_friend(self, user):
        self.friends.remove(user)

    def add(self, contact, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook()
        self.phone_books[tag].add_contact(contact)

    def share(self, user, tag):
        if user not in self.friends:
            print("This user is not your friend.")
        elif tag not in self.phone_books:
            print("You don't have a phone book with this tag.")
        else:
            user.phone_books[tag] = self.phone_books[tag]
            print("You shared phone book.")
