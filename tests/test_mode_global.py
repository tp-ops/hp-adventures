from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_game_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_castle_state_machine(self):

        self.get_options()