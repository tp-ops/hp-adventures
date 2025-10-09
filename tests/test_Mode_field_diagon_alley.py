from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_mode_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'
    
    def _start_game(self):
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

    def test_mode_start(self):

        # Starting a game
        self._start_game()

        # Ensure that mode field_diagon_alley is running
        self.assertModeRunning("field_diagon_alley")

    def test_lit_light(self):
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

    def test_complete_shot(self):

        self.get_options()

    def test_relit_light(self):

        self.get_options()

    def test_full_one_ball(self):

        # Starting a game
        self._start_game()

        # Ensure that mode field_diagon_alley is running
        self.assertModeRunning("field_diagon_alley")

        # Ensure that shots are enabled with proper shot_states
        self.assertTrue(self.machine.shots["sh_light_diagon_alley"].enabled)
        self.assertTrue(self.machine.shots["sh_diagon_alley"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_diagon_alley"].state_name)

        # When shot sh_light_diagon_alley is made ensure that it stays "unlit" and that sh_diagon_alley stays "lit"
        self.mock_event("sh_light_diagon_alley_unlit_hit")
        self.hit_and_release_switch("s_tar_light_diagon_alley")
        self.advance_time_and_run(1)
        self.assertEventCalled("sh_light_diagon_alley_unlit_hit")
        self.assertEqual("unlit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_diagon_alley is made ensure that it state change to "unlit" and that sh_light_diagon_alley state is advance to "lit"
        self.mock_event("sh_diagon_alley_lit_hit")
        self.hit_and_release_switch("s_spinner_diagon_alley")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_vuk_diagon_alley")
        self.advance_time_and_run(1)
        self.assertEventCalled("sh_diagon_alley_lit_hit")
        self.assertEqual("lit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_diagon_alley is made ensure that it stays "unlit" and that sh_light_diagon_alley stays "lit"
        self.mock_event("sh_diagon_alley_unlit_hit")
        self.hit_and_release_switch("s_spinner_diagon_alley")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_vuk_diagon_alley")
        self.advance_time_and_run(1)
        self.assertEventCalled("sh_diagon_alley_unlit_hit")
        self.assertEqual("lit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_light_diagon_alley is made ensure that it state changes to "unlit" and that sh_diagon_alley state is advance to "lit"
        self.mock_event("sh_light_diagon_alley_lit_hit")
        self.hit_and_release_switch("s_tar_light_diagon_alley")
        self.advance_time_and_run(1)
        self.assertEventCalled("sh_light_diagon_alley_lit_hit")
        self.assertEqual("unlit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()