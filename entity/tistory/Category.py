class Category:
  def __init__(self, _id, name, parent, label, entries):
    self.id: str = _id
    self.name: str = name
    self.parent: str = parent
    self.label: str = label
    self.entries: str = entries


def __str__(self):
  return f"{self.id=}, {self.name=}, {self.parent=}, {self.label=} {self.entries=}"
