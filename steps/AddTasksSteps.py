from behave import given, when, then
from pages.LibraryPage import LibraryPage
from pages.LoginPage import LoginPage
from pages.TodayTodoistPage import TodayTodoistPage
import config_file.ConfigFile as Configs

class AddTasksSteps:

    list_title_task = []

    @given("Prepare classes")
    def prepare_class(context):
        context.library_page = LibraryPage(context.driver)
        context.login_page = LoginPage(context.driver)
        context.today_page = TodayTodoistPage(context.driver)

    @when("Validate library page")
    def validate_library_page(context):
        context.library_page.validate_page_name()

    @then("Get title tasks")
    def get_title_tasks(context):
        context.list_title_task = context.library_page.get_title_task()

    @given("Go to login page")
    def go_to_login_page(context):
        context.login_page.go_to_login_page(Configs.url_login)

    @when("Validate login page")
    def validate_login_page(context):
        context.login_page.validate_page_name()

    @when("Send email and password")
    def send_email_password(context):
        context.login_page.send_user_password(Configs.email, Configs.password)

    @then("Click login button")
    def click_login_button(context):
        context.login_page.click_login_button()

    @then("Add tasks")
    def add_tasks(context):
        context.today_page.repeat_cycle_add_task(context.list_title_task)
