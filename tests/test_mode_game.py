from mpf.tests.MpfGameTestCase import MpfGameTestCase


class test_house_theme_selection(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_player1_ball1_eject_queue_relay(self):

        self.get_options()

    def test_player2_ball2_eject_no_queue_relay(self):

        self.get_options()

    def test_player2_ball1_queue_relay(self):

        self.get_options()
        
    def test_player2_ball1_no_queue_relay(self):

        self.get_options()