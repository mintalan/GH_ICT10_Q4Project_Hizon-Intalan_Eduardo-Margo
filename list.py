from pyscript import display, document


class Student:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject


classmates = []


def add(event=None):
    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('subject').value

    person = Student(name, section, subject)

    classmates.append(person)

    display(f'Hi! my name is {person.name}, I\'m from {person.section} and my favorite subject is {person.subject}! ', target='output')


def subject(s=None):
    class Subject:
        def __init__(self, name, section, subject):
            self.name = name
            self.section = section
            self.subject = subject

    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('subject').value

    classmate1 = Subject('Sitte', 'Sapphire', 'Math')
    classmate2 = Subject('Harvey', 'Sapphire', 'Science')
    classmate3 = Subject('Vito', 'Sapphire', 'PE')
    classmate4 = Subject('Benigno', 'Sapphire', 'PE')
    classmate5 = Subject('Tessa', 'Sapphire', 'Math')
    classmate6 = Subject('Seth', 'Sapphire', 'PE')
    classmate7 = Subject('Aaron', 'Sapphire', 'PE')
    classmate8 = Subject('Euan', 'Sapphire', 'PE')
    classmate9 = Subject('Allijah', 'Sapphire', 'PE')
    classmate10 = Subject('Neriza', 'Sapphire', 'Music')
    classmate11 = Subject('Margo', 'Sapphire', 'Social Studies')
    classmate12 = Subject('Atasha', 'Sapphire', 'English')
    classmate13 = Subject('Sofie', 'Sapphire', 'Social Studies')
    classmate14 = Subject('Jillian', 'Sapphire', 'Math')
    classmate15 = Subject('Manuel', 'Sapphire', 'Science')
    classmate16 = Subject('Ishan', 'Sapphire', 'PE')
    classmate17 = Subject('Kelsey', 'Sapphire', 'PE')
    classmate18 = Subject('Selena', 'Sapphire', 'Social Studies')
    classmate19 = Subject('Michaela', 'Sapphire', 'English')
    classmate20 = Subject('Marcus', 'Sapphire', 'PE')
    classmate21 = Subject('Anakin', 'Sapphire', 'Social Studies')
    classmate22 = Subject('Adrianna', 'Sapphire', 'English')
    classmate23 = Subject('Jennifer', 'Sapphire', 'English')
    classmate24 = Subject('Francesa', 'Sapphire', 'Math')
    classmate25 = Subject('Eduardo', 'Sapphire', 'English')

    display(
        (
        f'Hi! my name is {classmate1.name}, I\'m from {classmate1.section} and my favorite subject is {classmate1.subject}! '
        f'Hi! my name is {classmate2.name}, I\'m from {classmate2.section} and my favorite subject is {classmate2.subject}! '
        f'Hi! my name is {classmate3.name}, I\'m from {classmate3.section} and my favorite subject is {classmate3.subject}! '
        f'Hi! my name is {classmate4.name}, I\'m from {classmate4.section} and my favorite subject is {classmate4.subject}! '
        f'Hi! my name is {classmate5.name}, I\'m from {classmate5.section} and my favorite subject is {classmate5.subject}! '
        f'Hi! my name is {classmate6.name}, I\'m from {classmate6.section} and my favorite subject is {classmate6.subject}! '
        f'Hi! my name is {classmate7.name}, I\'m from {classmate7.section} and my favorite subject is {classmate7.subject}! '
        f'Hi! my name is {classmate8.name}, I\'m from {classmate8.section} and my favorite subject is {classmate8.subject}! '
        f'Hi! my name is {classmate9.name}, I\'m from {classmate9.section} and my favorite subject is {classmate9.subject}! '
        f'Hi! my name is {classmate10.name}, I\'m from {classmate10.section} and my favorite subject is {classmate10.subject}! '
        f'Hi! my name is {classmate11.name}, I\'m from {classmate11.section} and my favorite subject is {classmate11.subject}! '
        f'Hi! my name is {classmate12.name}, I\'m from {classmate12.section} and my favorite subject is {classmate12.subject}! '
        f'Hi! my name is {classmate13.name}, I\'m from {classmate13.section} and my favorite subject is {classmate13.subject}! '
        f'Hi! my name is {classmate14.name}, I\'m from {classmate14.section} and my favorite subject is {classmate14.subject}! '
        f'Hi! my name is {classmate15.name}, I\'m from {classmate15.section} and my favorite subject is {classmate15.subject}! '
        f'Hi! my name is {classmate16.name}, I\'m from {classmate16.section} and my favorite subject is {classmate16.subject}! '
        f'Hi! my name is {classmate17.name}, I\'m from {classmate17.section} and my favorite subject is {classmate17.subject}! '
        f'Hi! my name is {classmate18.name}, I\'m from {classmate18.section} and my favorite subject is {classmate18.subject}! '
        f'Hi! my name is {classmate19.name}, I\'m from {classmate19.section} and my favorite subject is {classmate19.subject}! '
        f'Hi! my name is {classmate20.name}, I\'m from {classmate20.section} and my favorite subject is {classmate20.subject}! '
        f'Hi! my name is {classmate21.name}, I\'m from {classmate21.section} and my favorite subject is {classmate21.subject}! '
        f'Hi! my name is {classmate22.name}, I\'m from {classmate22.section} and my favorite subject is {classmate22.subject}! '
        f'Hi! my name is {classmate23.name}, I\'m from {classmate23.section} and my favorite subject is {classmate23.subject}! '
        f'Hi! my name is {classmate24.name}, I\'m from {classmate24.section} and my favorite subject is {classmate24.subject}! '
        f'Hi! my name is {classmate25.name}, I\'m from {classmate25.section} and my favorite subject is {classmate25.subject}! '
        ),
        target='output'
    )