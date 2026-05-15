class Medication:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.taken = False

    def mark_as_taken(self):
        self.taken = True

    def __str__(self):
        status = "Tomado" if self.taken else "Pendente"
        return f"{self.name} às {self.time} - {status}"