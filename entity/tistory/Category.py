class Category:
  def __init__(self, _id, name, parent, label, entries):
    self.id: str = _id
    self.name: str = name
    self.parent: str = parent
    self.label: str = label
    self.entries: str = entries

  def __repr__(self):
    return f"Category={{{self.id=}, {self.name=}, {self.parent=}, {self.label=} {self.entries=}}}"

  @staticmethod
  def map_to_category(result):
    return Category(
      _id=result['id'],
      name=result['name'],
      parent=result['parent'],
      label=result['label'],
      entries=result['entries']
    )
