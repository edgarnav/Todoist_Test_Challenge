from driver_interactions.ElementsInteractions import ElementsInteractions

class LoginPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    page_name = "Iniciar sesión en Todoist"

    id_email_input = "email"
    id_password_input = "password"
    class_login_button = "submit_btn"

    def go_to_login_page(self, url):
        self.launch_web_page(url)

    def validate_page_name(self):
        self.verify_page(self.page_name)

    def send_user_password(self, email, password):
        self.send_text(email, self.id_email_input, "id")
        self.send_text(password, self.id_password_input, "id")

    def click_login_button(self):
        self.click_element(self.class_login_button, "class")


