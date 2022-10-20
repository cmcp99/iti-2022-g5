from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/create/abc")
        self.client.post("/createdouble/abc/50")