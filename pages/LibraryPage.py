from driver_interactions.ElementsInteractions import ElementsInteractions

class LibraryPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    page_name = "Random To-do list generator"

    class_title_task = "task-title"

    def validate_page_name(self):
        self.verify_page(self.page_name)

    def get_title_task(self):
        elements = self.get_all_elements(self.class_title_task, "class")
        list_title_task = []
        for element in elements:
            list_title_task.append(element.text.split("\n")[0])
        self.log.info(list_title_task)
        return list_title_task
