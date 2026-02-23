import time

class FeedNavigator:
    def __init__(self, driver):
        self.driver = driver

    def scroll_feed(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)