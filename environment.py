from driver_interactions.WebDriver import WebDriver
from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Log
import config_file.ConfigFile as Configs

log = Log.func_logger()

def before_all(context):
    log.info("Script started")
    context.prepare_driver = WebDriver()
    context.driver = context.prepare_driver.init_web_driver()
    context.bp = ElementsInteractions(context.driver)
    context.bp.launch_web_page(Configs.url_tasks_library)

def after_all(context):
    log.info("Script ended")
    context.driver.quit()
