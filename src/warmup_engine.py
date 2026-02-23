import yaml
from feed_navigator import FeedNavigator
from profile_interactor import ProfileInteractor
from rate_controller import RateController

class WarmupEngine:
    def __init__(self, driver):
        self.driver = driver
        self.feed = FeedNavigator(driver)
        self.profile = ProfileInteractor(driver)
        self.rate = RateController()

    def load_config(self):
        with open("config/warmup.yaml", "r") as f:
            return yaml.safe_load(f)

    def run(self):
        config = self.load_config()
        max_scroll = config["warmup"]["max_scroll_actions"]

        for _ in range(max_scroll):
            self.feed.scroll_feed()
            self.rate.wait()