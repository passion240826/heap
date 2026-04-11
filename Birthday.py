class Birthday:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)
    
    def __le__(self, other):
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)

    def __ge__(self, other):
        return (self.year, self.month, self.day) >= (other.year, other.month, other.day)
    
    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __str__(self):
        return self.name

    @staticmethod
    def parse_csv(csv_text: str):
        result = []
        lines = csv_text.strip().split("\n")

        for line in lines[1:]:
            parts = line.split(",")
            if len(parts) != 4:
                continue

            name = parts[0].strip()
            year = int(parts[1].strip())
            month = int(parts[2].strip())
            day = int(parts[3].strip())

            result.append(Birthday(name, year, month, day))

        return result