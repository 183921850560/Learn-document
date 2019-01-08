# coding=utf-8
from locust import *
class MyTest(TaskSet):
    # def on_start(self):
    #     self.index=0
    @task(weight=1)
    def manual01(self):
        # device = self.locust.duSerial_list[self.index]
        # print('device: %s' %device)
        # self.index = (self.index + 1) % len(self.locust.duSerial_list)
        # ff = self.client.get(device)
        # print(ff)
        param ={
            "duSerial":"139615610",
            "channel":1,
            "snapType":0,
            "frequency":5
             }

        response = self.client.post(name='manual', url='/api/v2/picture/snap/manual', json=param, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

class Run(HttpLocust):
    task_set = MyTest
    host = 'http://eag-test.yun-ti.com:8100'
    # duSerial_list = ["150561034", "139615610", "150562273", "150561768", "752641570", "780246491", "150562391","150560553",
    #                  "150562323","139615688", "150561787", "139615748", "150561772", "150560560", "139615592", "150562100",
    #                  "150561379", "139615589"]

    max_wait = 20000
    min_wait = 10000

# from locust import TaskSet, task, HttpLocust
# class UserBehavior(TaskSet):
#     def on_start(self):
#         self.index = 0
#     @task
#     def test_visit(self):
#         url = self.locust.share_data[self.index]
#         print('visit url: %s' % url)
#         self.index = (self.index + 1) % len(self.locust.share_data)
#         self.client.get(url)
# class WebsiteUser(HttpLocust):
#     host = 'http://debugtalk.com'
#     task_set = UserBehavior
#     share_data = ['url1', 'url2', 'url3', 'url4', 'url5']
#     min_wait = 1000
#     max_wait = 3000
