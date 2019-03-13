import abc


class Message(object):
    id = 5  # type: int
    size = 10  # type: int


class PersonABC(abc.ABC):
    @property
    @abc.abstractmethod
    def age(self):
        # type: () -> int
        pass

    @abc.abstractproperty
    def profession(self):
        # type: () -> str
        pass

    @property
    @abc.abstractmethod
    def title(self) -> str:
        pass


class Emmet(PersonABC):
    _age = 21
    _location = "clifton park"
    _department = 'cv'

    @property
    def age(self):
        return self._age

    @property
    def profession(self):
        if self._location == 'clifton park':
            return 'kitware'
        else:
            return 'idk'

    @property
    def title(self):
        if self._department == 'cv':
            return 'r&d eng'
        return 'idk'

    @title.setter
    def title(self, v):
        if self._department == 'cv':
            self._title = v

class Mike(PersonABC):
    _dob = '1988/07/13'
    _profession = 'kitware'
    _title = 'engineer'

    @property
    def age(self):
        return 30

    @property
    def profession(self):
        return 'foo'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, v: str):
        self._title = v


class PersonIface(object):

    @abc.abstractstaticmethod
    def id(m):
        # type: (Message) -> int
        return m.id

    @abc.abstractstaticmethod
    def size(m):
        # type: (Message) -> int
        pass


def get_resume(p: PersonABC):
    print('{} {} {}'.format(p.age, p.profession, p.title))


if __name__ == '__main__':
    m = Message()
    mike = Mike()
    # emmett = Emmet()
    mike.title = 'god'
    get_resume(mike)
