from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/create/abc")
        self.client.get("/createdouble/abc/50")