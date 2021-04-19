from mycroft import MycroftSkill, intent_file_handler


class SirenAlarm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alarm.siren.intent')
    def handle_alarm_siren(self, message):
        self.speak_dialog('alarm.siren')


def create_skill():
    return SirenAlarm()

