import time

class ProfileInteractor:
    def __init__(self, driver):
        self.driver = driver

    def visit_profile(self, profile_url):
        self.driver.get(profile_url)
        time.sleep(5)