from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/other")
        self.client.get(f"{self.base_url}/other?page=6")
        self.client.get(f"{self.base_url}/exp?value=6")