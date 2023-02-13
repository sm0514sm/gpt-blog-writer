class Category:
  def __init__(self, _id, name, parent, label, entries, entriesInLogin):
    self.id: str = _id
    self.name: str = name
    self.parent: str = parent
    self.label: str = label
    self.entries: str = entries
    self.entriesInLogin: str = entriesInLogin


def __str__(self):
  return f"{self.id=}, {self.use=}, {self.topic_name=}, {self.published_count=} {self.created_count=}"
