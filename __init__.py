from mycroft import MycroftSkill, intent_file_handler


class Comolavar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('comolavar.intent')
    def handle_comolavar(self, message):
        self.speak_dialog('comolavar')


def create_skill():
    return Comolavar()

