# need to run from cmdline: docker run --rm --add-host host.docker.internal:host-gateway -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py TestUser
# or: docker run --rm --add-host host.docker.internal:host-gateway -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py AlwaysConnectedUserBBCOne AlwaysConnectedUserBBCTwo OcassionallyConnectedUserBBCOne OcassionallyConnectedUserBBCTwo

# configure host with value "http://host.docker.internal:7071" when running within local container
# to run this at scale, please check: https://github.com/yorek/locust-on-azure

import time, uuid
from locust import HttpUser, task, between

class TestUser(HttpUser):
    weight = 100
    wait_time = between (1,1)
    devicename= ""

    def on_start(self):
        self.devicename = "device-" + str(uuid.uuid1())

    @task(1)
    def sendTelemetry1(self):
        self.client.get("https://xstof-asc-gateway.azuremicroservices.io/WEATHER-SERVICE/weather/city?name=Paris%2C%20France")
