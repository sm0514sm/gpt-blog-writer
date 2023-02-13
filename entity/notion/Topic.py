class Topic:
  def __init__(self, _id, use, topic_name, published_count=0, created_count=0):
    self.id: str = _id
    self.use: bool = use
    self.topic_name: str = topic_name
    self.published_count: int = published_count
    self.created_count: int = created_count

  def __str__(self):
    return f"{self.id=}, {self.use=}, {self.topic_name=}, {self.published_count=} {self.created_count=}"

  @staticmethod
  def map_to_topic(result):
    properties = result['properties']

    return Topic(
      _id=result['id'],
      use=properties['use']['checkbox'],
      topic_name=properties['topic_name']['title'][0]['plain_text'].strip(),
      published_count=0 if properties['published_count']['number'] is None else properties['published_count']['number'],
      created_count=0 if properties['created_count']['number'] is None else properties['created_count']['number'],
    )