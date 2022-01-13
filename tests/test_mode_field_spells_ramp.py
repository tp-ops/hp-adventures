from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_game_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\Source Code\\hp-adventures'

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

    def test_counter_with_drain(self):

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

        # Ensure that mode field_orbits is running
        self.assertModeRunning("field_spells_ramp")

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)

        # Make 3 spells ramp shot
        for i in range(3):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(1)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(3, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Drain ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 2 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(3, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Make 3 spells ramp shot
        for i in range(3):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(1)

        self.assertEqual(6, self.machine.counters["lb_spells_light_qualify_counter"].value)   

    def test_spells_light_with_drain(self):

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

        # Ensure that mode field_orbits is running
        self.assertModeRunning("field_spells_ramp")

        # Make 10 spells ramp shot
        for i in range(10):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(1)

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Drain ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 2 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Make ramp light shot
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_wire_ramp_small")

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Advance time for 14 seconds
        self.advance_time_and_run(14)
        self.assertEqual(14, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

    def test_timer_reset(self):

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

        # Ensure that mode field_orbits is running
        self.assertModeRunning("field_spells_ramp")

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)

        # Make 10 spells ramp shot
        for i in range(10):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(1)

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)

        # Make ramp light shot
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_wire_ramp_small")

        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Advance time for 14 seconds
        self.advance_time_and_run(14)
        self.assertEqual(14, self.machine.timers["right_ramp_light_qualify_timer"].ticks)
        
        # Advance time for last second
        self.mock_event("timer_right_ramp_light_qualify_timer_complete")
        self.advance_time_and_run(1)
        self.assertEventCalled("timer_right_ramp_light_qualify_timer_complete")
        self.reset_mock_events()

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check level state_machine
        self.assertEqual("level_2", self.machine.state_machines["sm_spells_level"].state)

    def test_timer_with_drain(self):

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

        # Ensure that mode field_orbits is running
        self.assertModeRunning("field_spells_ramp")

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)

        # Make 10 spells ramp shot
        for i in range(10):
            self.hit_and_release_switch("s_spells_ramp_entry")
            self.advance_time_and_run(1)
            self.hit_and_release_switch("s_right_wire_ramp_small")
            self.advance_time_and_run(1)

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)

        # Make ramp light shot
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_wire_ramp_small")

        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Advance time for 3 seconds
        self.advance_time_and_run(3)
        self.assertEqual(3, self.machine.timers["right_ramp_light_qualify_timer"].ticks)
        
        # Drain ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 2 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Check level state_machine
        self.assertEqual("level_2", self.machine.state_machines["sm_spells_level"].state)