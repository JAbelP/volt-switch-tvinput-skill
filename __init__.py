from mycroft import MycroftSkill, intent_file_handler


class VoltSwitchTvinput(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tvinput.switch.volt.intent')
    def handle_tvinput_switch_volt(self, message):
        self.speak_dialog('tvinput.switch.volt')


def create_skill():
    return VoltSwitchTvinput()

