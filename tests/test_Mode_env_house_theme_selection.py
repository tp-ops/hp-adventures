from mpf.tests.MpfGameTestCase import MpfGameTestCase


class test_house_theme_selection(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_carousel_and_player_vars(self):

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

        # Loop through themes with flipper buttons
        # Should start with gryffindor
        self.assertPlayerVarEqual("gryffindor","house_theme_name")
        self.assertPlayerVarEqual("Gryffindor","house_theme_title")
        self.assertPlayerVarEqual("logo_gryffindor","house_theme_logo")
        self.assertPlayerVarEqual("gryffindor_led","house_theme_led")
        

        # Go right to hufflepuff
        self.hit_and_release_switch("s_fl_right_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("hufflepuff","house_theme_name")
        self.assertPlayerVarEqual("Hufflepuff","house_theme_title")
        self.assertPlayerVarEqual("logo_hufflepuff","house_theme_logo")
        self.assertPlayerVarEqual("hufflepuff_led","house_theme_led")

        # Go right to ravenclaw
        self.hit_and_release_switch("s_fl_right_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("ravenclaw","house_theme_name")
        self.assertPlayerVarEqual("Ravenclaw","house_theme_title")
        self.assertPlayerVarEqual("logo_ravenclaw","house_theme_logo")
        self.assertPlayerVarEqual("ravenclaw_led","house_theme_led")
        
        # Go right to slthiryn
        self.hit_and_release_switch("s_fl_right_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("slytherin","house_theme_name")
        self.assertPlayerVarEqual("Slytherin","house_theme_title")
        self.assertPlayerVarEqual("logo_slytherin","house_theme_logo")
        self.assertPlayerVarEqual("slytherin_led","house_theme_led")

        # Go right to get back at gryffindor
        self.hit_and_release_switch("s_fl_right_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("gryffindor","house_theme_name")
        self.assertPlayerVarEqual("Gryffindor","house_theme_title")
        self.assertPlayerVarEqual("logo_gryffindor","house_theme_logo")
        self.assertPlayerVarEqual("gryffindor_led","house_theme_led")

        # Go left to slthiryn
        self.hit_and_release_switch("s_fl_left_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("slytherin","house_theme_name")
        self.assertPlayerVarEqual("Slytherin","house_theme_title")
        self.assertPlayerVarEqual("logo_slytherin","house_theme_logo")
        self.assertPlayerVarEqual("slytherin_led","house_theme_led")

        # Go left to ravenclaw
        self.hit_and_release_switch("s_fl_left_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("ravenclaw","house_theme_name")
        self.assertPlayerVarEqual("Ravenclaw","house_theme_title")
        self.assertPlayerVarEqual("logo_ravenclaw","house_theme_logo")
        self.assertPlayerVarEqual("ravenclaw_led","house_theme_led")

        # Go left to hufflepuff
        self.hit_and_release_switch("s_fl_left_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("hufflepuff","house_theme_name")
        self.assertPlayerVarEqual("Hufflepuff","house_theme_title")
        self.assertPlayerVarEqual("logo_hufflepuff","house_theme_logo")
        self.assertPlayerVarEqual("hufflepuff_led","house_theme_led")

        # Go left to get back at gryffindor
        self.hit_and_release_switch("s_fl_left_a")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual("gryffindor","house_theme_name")
        self.assertPlayerVarEqual("Gryffindor","house_theme_title")
        self.assertPlayerVarEqual("logo_gryffindor","house_theme_logo")
        self.assertPlayerVarEqual("gryffindor_led","house_theme_led")

        # Go 2x right to select ravenclaw theme
        self.hit_and_release_switch("s_fl_right_a")
        self.hit_and_release_switch("s_fl_right_a")
        self.advance_time_and_run(1)

        # Hit 'Start' button to select ravenclaw
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")
        self.assertPlayerVarEqual("ravenclaw","house_theme_name")
        self.assertPlayerVarEqual("Ravenclaw","house_theme_title")
        self.assertPlayerVarEqual("logo_ravenclaw","house_theme_logo")
        self.assertPlayerVarEqual("ravenclaw_led","house_theme_led")

        # End game
        self.stop_game()
        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()