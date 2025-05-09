from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_mode_attract(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

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

        # Start
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        self.stop_game()
        self.advance_time_and_run(1)

        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")
        self.assertGameIsNotRunning()
