from locust import HttpUser, between, constant, task

class WebsiteUser(HttpUser):
    wait_time = between(3, 5)

    @task(10)
    def index(self):
        self.client.get("/posts")

    @task(7)
    def showPost(self):
        self.client.get("/posts/1")

    @task(6)
    def showPostComments(self):
        self.client.get("/posts/1/comments")

    @task(4)
    def createPostComment(self):
        self.client.post("/posts/1/comments", {
            "body": "iop",
            "postId": 1
        })

    @task(2)
    def createPost(self):
        self.client.post("/posts", {
            "title": "qwe",
            "author": "asd"
        })