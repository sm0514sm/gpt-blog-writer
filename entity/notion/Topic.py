class Topic:
  def __init__(self, _id, use, topic_name, published_count=0, created_count=0):
    self.id: str = _id
    self.use: bool = use
    self.topic_name: str = topic_name
    self.published_count: int = published_count
    self.created_count: int = created_count

  def __str__(self):
    return f"{self.id=}, {self.use=}, {self.topic_name=}, {self.published_count=} {self.created_count=}"
