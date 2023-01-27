class User:
    def __init__(self,user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 2

user_1 = User("001","yang")
user_2 = User("002","zhou")
# user_1.id = "001"
# user_1.username = "angela"

user_1.follow(user_2)
print(user_1.followers) #0
print(user_1.following) #2
print(user_2.followers) #1
print(user_2.following) #0

