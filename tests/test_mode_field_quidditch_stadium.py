from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_game_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\Source Code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_quilify_one_ball(self):

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

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")

        # Ensure that shots are enabled with proper shot_states
        self.assertTrue(self.machine.shots["sh_pop_left_qualify"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_right_qualify"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_bottom_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_left"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_right"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_bottom"].enabled)
        self.assertFalse(self.machine.shots["sh_quidditch_stadium"].enabled)
        self.assertFalse(self.machine.shots["sh_quidditch_orbit"].enabled)
        self.assertTrue(self.machine.shots["sh_mis_quidditch"].enabled)

        self.assertEqual("lit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Are both counter quidditch_pop_bumper_count and accrual quidditch_accrual disabled ?
        self.assertFalse(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertFalse(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Qualify to enable shots for quidditch stadium - hit all three pops
        self.hit_and_release_switch("s_pop_left")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)
     
        self.hit_and_release_switch("s_pop_right")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)
        
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Chech that qualify shots are disabled and normal pop shots are enabled
        self.assertFalse(self.machine.shots["sh_pop_left_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_right_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_bottom_qualify"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_left"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_right"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_bottom"].enabled)

        # Check that stadium and orbit shots are enabled now
        self.assertTrue(self.machine.shots["sh_quidditch_stadium"].enabled)
        self.assertTrue(self.machine.shots["sh_quidditch_orbit"].enabled)
        self.assertTrue(self.machine.shots["sh_mis_quidditch"].enabled)

        # Are both counter quidditch_pop_bumper_count and accrual quidditch_accrual enabled ?
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

    def test_quilify_with_drain(self):

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

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")

        self.assertEqual("lit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)

        # Make one qualify shot
        self.hit_and_release_switch("s_pop_left")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)

        # Drain ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 2 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check qualify shots (all three lit again)
        self.assertEqual("lit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)

        # Make all three qualify shot
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        
        # Check counter and accrual
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])
        
        # Shot states
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

    def test_accrual_one_ball(self):

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

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")

        # Qualify to enable shots for quidditch stadium - hit all three pops
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Chech that qualify shots are disabled and normal pop shots are enabled
        self.assertFalse(self.machine.shots["sh_pop_left_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_right_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_bottom_qualify"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_left"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_right"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_bottom"].enabled)

        # Check that stadium and orbit shots are enabled now
        self.assertTrue(self.machine.shots["sh_quidditch_stadium"].enabled)
        self.assertTrue(self.machine.shots["sh_quidditch_orbit"].enabled)
        self.assertTrue(self.machine.shots["sh_mis_quidditch"].enabled)

        # Are both counter quidditch_pop_bumper_count and accrual quidditch_accrual enabled ?
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Make 9 pop bumper shots and one left orbit shot to advance
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual(3, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual(6, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual(9, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])
        
        # Shot 10
        self.mock_event("quidditch_pop_bumper_count_completed")
        self.hit_and_release_switch("s_pop_left")
        self.advance_time_and_run(1)
        self.assertEventCalled("quidditch_pop_bumper_count_completed")
        self.reset_mock_events()

        # Counter completed and disabled
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertFalse(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        
        # Accrual updated
        self.assertEqual(True,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])
        
        # Shot state changes
        self.assertEqual("hit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Make one left orbit shot
        self.mock_event("you_are_a_quidditch_player")
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
      
        # Shot state changes
        self.assertEqual("hit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Accrual completed ?
        self.assertEventCalled("you_are_a_quidditch_player")
        self.reset_mock_events()
        
        # Shot state changes
        self.assertEqual("hit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

    def test_accrual_pop_with_drain(self):

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

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")

        # Qualify to enable shots for quidditch stadium - hit all three pops
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Chech that qualify shots are disabled and normal pop shots are enabled
        self.assertFalse(self.machine.shots["sh_pop_left_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_right_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_bottom_qualify"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_left"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_right"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_bottom"].enabled)

        # Check that stadium and orbit shots are enabled now
        self.assertTrue(self.machine.shots["sh_quidditch_stadium"].enabled)
        self.assertTrue(self.machine.shots["sh_quidditch_orbit"].enabled)
        self.assertTrue(self.machine.shots["sh_mis_quidditch"].enabled)

        # Are both counter quidditch_pop_bumper_count and accrual quidditch_accrual enabled ?
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Make 6 pop bumper shots
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)

        # Shot states
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)
        self.assertEqual(6, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])
      
        # Drain ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 3 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check qualify shots (all three lit again)
        self.assertEqual("lit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)

        # Make all three qualify shot
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        
        # Check if counter still is at 7 (last qulify shot counts too so it will be 7 instead of 6)
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(7, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Shot states
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Make 3 pop bumper shots
        self.mock_event("quidditch_pop_bumper_count_completed")
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)

        # Check counter is completed and disabled
        self.assertEventCalled("quidditch_pop_bumper_count_completed")
        self.assertFalse(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.reset_mock_events()
        
        # Check accrual state
        self.assertEqual(True,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Shot states
        self.assertEqual("hit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Drain ball
        self.assertBallNumber(2)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 3 and advance skillshot platform
        self.assertBallNumber(3)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make all three qualify shot
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)

        # Shot states
        self.assertEqual("hit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)        
        
        # Check if counter still is completed and disabled
        self.assertFalse(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(True,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Shot states
        self.assertEqual("hit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)        

    def test_accrual_orbit_with_drain(self):

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

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")

        # Qualify to enable shots for quidditch stadium - hit all three pops
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_left"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_right"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_pop_bottom"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

        # Chech that qualify shots are disabled and normal pop shots are enabled
        self.assertFalse(self.machine.shots["sh_pop_left_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_right_qualify"].enabled)
        self.assertFalse(self.machine.shots["sh_pop_bottom_qualify"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_left"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_right"].enabled)
        self.assertTrue(self.machine.shots["sh_pop_bottom"].enabled)

        # Check that stadium and orbit shots are enabled now
        self.assertTrue(self.machine.shots["sh_quidditch_stadium"].enabled)
        self.assertTrue(self.machine.shots["sh_quidditch_orbit"].enabled)
        self.assertTrue(self.machine.shots["sh_mis_quidditch"].enabled)

        # Are both counter quidditch_pop_bumper_count and accrual quidditch_accrual enabled ?
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Make one left orbit shot
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)

        # Shot states
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)
        self.assertEqual(0, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(True,self.machine.accruals["lb_quidditch_accrual"].value[1])
      
        # Drain ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 3 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check qualify shots (all three lit again)
        self.assertEqual("lit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_pop_bottom_qualify"].state_name)

        # Make all three qualify shot
        self.hit_and_release_switch("s_pop_left")
        self.hit_and_release_switch("s_pop_right")
        self.hit_and_release_switch("s_pop_bottom")
        self.advance_time_and_run(1)
        self.assertEqual("hit", self.machine.shots["sh_pop_left_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_right_qualify"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_pop_bottom_qualify"].state_name)
        
        # Check if counter still is at 1 (last qulify shot counts too so it will be 1 instead of 0)
        self.assertTrue(self.machine.counters["lb_quidditch_pop_bumper_counter"].enabled)
        self.assertTrue(self.machine.accruals["lb_quidditch_accrual"].enabled)
        self.assertEqual(1, self.machine.counters["lb_quidditch_pop_bumper_counter"].value)
        self.assertEqual(False,self.machine.accruals["lb_quidditch_accrual"].value[0])
        self.assertEqual(True,self.machine.accruals["lb_quidditch_accrual"].value[1])

        # Shot states
        self.assertEqual("lit", self.machine.shots["sh_quidditch_stadium"].state_name)
        self.assertEqual("hit", self.machine.shots["sh_quidditch_orbit"].state_name)
        self.assertEqual("lit", self.machine.shots["sh_mis_quidditch"].state_name)

    def test_orbits_mode_connection(self):

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

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")
        self.assertModeRunning("field_orbits")
        self.assertModeNotRunning("field_orbits_alternative")

        # Mock events comming from mode field_orbits and field_orbits_alternative
        self.mock_event("sq_shot_left_orbit_big_hit")
        self.mock_event("sq_shot_left_orbit_big_alt_hit")
        
        # Test field_orbits mode connection
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
        self.assertEventCalled("sq_shot_left_orbit_big_hit")
        self.assertEventNotCalled("sq_shot_left_orbit_big_alt_hit")
        self.reset_mock_events()

        # Change active field_orbits to field_orbits_alternative
        self.stop_mode("field_orbits")
        self.start_mode("field_orbits_alternative")

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_orbits_alternative")
        self.assertModeNotRunning("field_orbits")

        # Mock events comming from mode field_orbits and field_orbits_alternative
        self.mock_event("sq_shot_left_orbit_big_hit")
        self.mock_event("sq_shot_left_orbit_big_alt_hit")
        
        # Test field_orbits mode connection
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
        self.assertEventCalled("sq_shot_left_orbit_big_alt_hit")
        self.assertEventNotCalled("sq_shot_left_orbit_big_hit")
        self.reset_mock_events()