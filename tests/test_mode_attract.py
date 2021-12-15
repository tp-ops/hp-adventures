from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_mode_attract(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_mode_attract(self):

        self.get_options()
        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()
        

        self.start_game()
        self.advance_time_and_run(1)

        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")
        self.assertGameIsRunning()

        self.stop_game()
        self.advance_time_and_run(1)

        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")
        self.assertGameIsNotRunning()
