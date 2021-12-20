from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_game_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_mode_field_diagon_alley(self):

        self.get_options()

        # Ensure that Attract mode is running and game mode not
        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()
        
        # Hit 'Start' button to start a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.game.num_players)
        self.assertPlayerCount(1)
        self.advance_time_and_run(1)

        # Ensure that Mode env_house_theme_selection is running
        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertGameIsRunning()
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")

        # Advance skillshot platform
        self.post_event("sh_skill_shot_platform_lit_hit")
        self.advance_time_and_run(1)

        # Ensure that mode field_diagon_alley is running
        self.assertModeRunning("field_diagon_alley")

        # Ensure that shots are enabled with proper shot_states
        self.assertTrue(self.machine.shots["sh_light_diagon_alley"].enabled)
        self.assertTrue(self.machine.shots["sh_diagon_alley"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_diagon_alley"].state_name)

        # When shot sh_light_diagon_alley is made ensure that it stays "unlit" and that sh_diagon_alley stays "lit"
        self.mock_event("playfield_active")
        self.mock_event("sh_light_diagon_alley_unlit_hit")
        self.hit_and_release_switch("s_tar_light_diagon_alley")
        self.advance_time_and_run(1)
        self.assertEventCalled("playfield_active")
        self.assertEventCalled("sh_light_diagon_alley_unlit_hit")
        self.assertEqual("unlit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_diagon_alley is made ensure that it state change to "unlit" and that sh_light_diagon_alley state is advance to "lit"
        self.mock_event("playfield_active")
        self.mock_event("sh_diagon_alley_lit_hit")
        self.hit_and_release_switch("s_diagon_alley")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_vuk_top")
        self.advance_time_and_run(1)
        self.assertEventCalled("playfield_active")
        self.assertEventCalled("sh_diagon_alley_lit_hit")
        self.assertEqual("lit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_diagon_alley is made ensure that it stays "unlit" and that sh_light_diagon_alley stays "lit"
        self.mock_event("playfield_active")
        self.mock_event("sh_diagon_alley_unlit_hit")
        self.hit_and_release_switch("s_diagon_alley")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_vuk_top")
        self.advance_time_and_run(1)
        self.assertEventCalled("playfield_active")
        self.assertEventCalled("sh_diagon_alley_unlit_hit")
        self.assertEqual("lit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()

        # When shot sh_light_diagon_alley is made ensure that it state changes to "unlit" and that sh_diagon_alley state is advance to "lit"
        self.mock_event("playfield_active")
        self.mock_event("sh_light_diagon_alley_lit_hit")
        self.hit_and_release_switch("s_tar_light_diagon_alley")
        self.advance_time_and_run(1)
        self.assertEventCalled("playfield_active")
        self.assertEventCalled("sh_light_diagon_alley_lit_hit")
        self.assertEqual("unlit", self.machine.shots["sh_light_diagon_alley"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_diagon_alley"].state_name)
        self.reset_mock_events()