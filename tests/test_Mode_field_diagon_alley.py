from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_game_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_full_one_ball(self):

        self.get_options()

        # Hit 'Start' button to start a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)

        # Advance skillshot platform
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

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
        self.hit_and_release_switch("s_diagon_alley")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_vuk_top")
        self.advance_time_and_run(1)
        self.assertEventCalled("sh_diagon_alley_lit_hit")
        self.assertEqual("lit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_diagon_alley is made ensure that it stays "unlit" and that sh_light_diagon_alley stays "lit"
        self.mock_event("sh_diagon_alley_unlit_hit")
        self.hit_and_release_switch("s_diagon_alley")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_vuk_top")
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