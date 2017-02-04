from locust import HttpLocust, TaskSet


# def login(l):
#     l.client.post("/login", {"username": "ellen_key", "password": "education"})


def index(l):
    l.client.get("/")


# def profile(l):
#     l.client.get("/profile")


class UserBehavior(TaskSet):
    tasks = {index: 1}

    def on_start(self):
        index(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
