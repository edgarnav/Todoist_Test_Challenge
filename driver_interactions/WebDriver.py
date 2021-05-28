from selenium import webdriver
import utilities.Logger as Log
import config_file.ConfigFile as Configs

class WebDriver:

    log = Log.func_logger()

    def init_web_driver(self):
        self.log.info("Running test in Chrome")
        return webdriver.Chrome(Configs.path_chrome_driver)
