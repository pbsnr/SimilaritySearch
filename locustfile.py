import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    @task
    def view_item(self):
        for item_id in range(10):
            self.client.get("/")
            time.sleep(1)

