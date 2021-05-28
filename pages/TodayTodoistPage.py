from driver_interactions.ElementsInteractions import ElementsInteractions
import time

class TodayTodoistPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    page_name = "Hoy: Todoist"
    class_add_button = "plus_add_button"
    class_task_input = "public-DraftEditor-content"
    class_add_task_button = "ist_button_red"
    class_avatar_button = "settings_avatar"
    id_close_session_button = "id-0vgue8-9"

    def validate_page_name(self):
        self.verify_page(self.page_name)

    def click_add_button(self):
        self.click_element(self.class_add_button, "class")

    def send_text_task(self, text_task):
        self.send_text(text_task, self.class_task_input, "class")

    def click_add_task_button(self):
        self.click_element(self.class_add_task_button, "class")

    def repeat_cycle_add_task(self, list_title_task):
        self.click_add_button()
        for task in list_title_task[:5]:
            self.send_text_task(task)
            time.sleep(.1)
            self.click_add_task_button()
