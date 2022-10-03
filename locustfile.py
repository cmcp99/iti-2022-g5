from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/create/ola")
        self.client.get("/createdouble/ola/40")
        self.client.get("/file/7.pdf")