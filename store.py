class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

posts = []

class PostStore:
    def get_all(self):
        # get all posts
        return posts

    def add(self, post):
        # append post
        posts.append(post)

    def get_by_id(self, id):
        # search for post by id
        result = None

        for post in posts:
            if post.id == id:
                result = post
                break

        return result

    def update(self, id, fields):
       # update post data
       instance = self.get_by_id(id)

       instance.photo_url = fields['photo_url']
       instance.name = fields['name']
       instance.body = fields['body']

    def delete(self, id):
        # delete post by id
        instance = self.get_by_id(id)
        posts.remove(instance)
post1 = Post(id=1,
         photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
         name='Sara',
         body='Lorem Ipsum')
post2 = Post(id=2,
         photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
         name='John',
         body='Lorem Ipsum')
print(post1.name)
store = PostStore()
store.add(post1)
store.add(post2)
print(store.get_by_id(1).name)

