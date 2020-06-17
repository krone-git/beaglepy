

class Population:
    def __init__(self, members=(,)):
        self._members = set(members)

    def add(self, member):
        self._members.add(member)

    def remove(self, member):
        self._members.remove(member)
