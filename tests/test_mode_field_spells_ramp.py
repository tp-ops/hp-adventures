from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_mode_field_spells_ramp(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_mode_field_spells_ramp(self):

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

        # Ensure that mode field_orbits is running
        self.assertModeRunning("field_spells_ramp")

        # Check ramp diverter hagrids place
        self.assertEqual(False, self.machine.diverters.div_hagrid_place.enabled)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)

        # Check level state_machine
        self.assertEqual("level_1", self.machine.state_machines["sm_spells_level"].state)

        # Make 9 spells ramp shot
        for i in range(9):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(1)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(9, self.machine.counters["lb_spells_light_qualify_counter"].value)

        # Shot 10
        self.mock_event("lb_spells_light_qualify_counter_completed")
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_wire_ramp_small")
        self.advance_time_and_run(1)
        self.assertEventCalled("lb_spells_light_qualify_counter_completed")
        self.reset_mock_events()

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify counter
        self.assertEqual(False, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)

        # Check level state_machine
        self.assertEqual("level_1", self.machine.state_machines["sm_spells_level"].state)

        # Make ramp light shot
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_wire_ramp_small")

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify counter
        self.assertEqual(False, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Check level state_machine
        self.assertEqual("level_1", self.machine.state_machines["sm_spells_level"].state)

        # Advance time for 15 seconds
        self.mock_event("timer_right_ramp_light_qualify_timer_complete")
        self.advance_time_and_run(15)
        self.assertEventCalled("timer_right_ramp_light_qualify_timer_complete")
        self.reset_mock_events()

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Check level state_machine
        self.assertEqual("level_2", self.machine.state_machines["sm_spells_level"].state)


        # Another level
        for i in range(11):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(15)
        
        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Check level state_machine
        self.assertEqual("level_3", self.machine.state_machines["sm_spells_level"].state)