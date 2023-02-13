class Post:
  def __init__(self, _id, title, topic, status, body, created_dts, published_dts, post_id):
    self.id: str = _id
    self.title: str = title
    self.topic: str = topic
    self.status: str = status
    self.body: str = body
    self.created_dts: str = created_dts
    self.published_dts: str = published_dts
    self.post_id: str = post_id

  def __str__(self):
    return f"{self.id=}, {self.title=}, {self.topic=}, {self.status=}, {self.created_dts}, {self.published_dts}"
