from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_global_hogwarts_castle(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_castle_state_machine(self):

        self.get_options()