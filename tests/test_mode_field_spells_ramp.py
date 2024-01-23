from mpf.tests.MpfGameTestCase import MpfGameTestCase
# ------------------
#  Mode Description
# ------------------
# * Step 1 - Make 10 right Ramp Shots to complete qualify counter and advance the Spells Light to lit.
# - Step 2 - Make another Right Ramp Shot to advance the Spells Light to active, advance the Right Ramp Light to lit and 
#            start a qualifying timer.
# - Step 3 - Make another Right Ramp Shot before the timer ends to complete the Spells Light qualification, 
#            reset both Light shots to unlit, advance the state_machine to next level and collect a bonus.
# - Step X - When the timer ends - Reset both Light shots to unlit, reset counter, reset timer and advance state_machine to
#            next level without a bonus.
# - Step X - When a ball drains when Spells Light is unlit - Persist counter state_value.
# - Step X - When a ball drains when Spells Light is lit - Persist Spells Light shot_state to lit.
# - Step X - When a ball drains when Spells Light is active - Reset both Light shots to unlit, reset counter, reset timer and
#            advance state_machine to next level without a bonus.

class test_mode_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'
    
    def test_mode_start_logic(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Ensure that mode field_spells_ramp is running
        self.assertModeRunning("field_spells_ramp")

        # Check ramp diverter hagrids place
        self.assertEqual(False, self.machine.diverters.div_hagrid_place.enabled)
        self.assertEqual(False, self.machine.diverters.div_hagrid_place.active) # checken

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
        self.assertEqual("Spell 1", self.machine.state_machines["sm_spells_level"].state)

    def test_drain_ball(self):
        
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        
        # Drain a ball
        self.assertBallNumber(1)
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 2 and advance skillshot platform
        self.assertBallNumber(2)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        
        # Ensure that mode field_spells_ramp is running
        self.assertModeRunning("field_spells_ramp")

    def test_right_ramp_sq_shot(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make sequence shot in time and check hit event
        self.mock_event("sq_shot_spells_ramp_hit")
        self.mock_event("sq_shot_spells_ramp_timeout")
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.hit_and_release_switch("s_right_wire_ramp_small")
        self.assertEventNotCalled("sq_shot_spells_ramp_timeout")
        self.assertEventCalled("sq_shot_spells_ramp_hit")
        self.reset_mock_events()

        # Fail to make sequence shot in time and check timeout event
        self.mock_event("sq_shot_spells_ramp_hit")
        self.mock_event("sq_shot_spells_ramp_timeout")
        self.hit_and_release_switch("s_spells_ramp_entry")
        self.advance_time_and_run(4)
        self.assertEventNotCalled("sq_shot_spells_ramp_hit")
        self.assertEventCalled("sq_shot_spells_ramp_timeout")
        self.reset_mock_events()

    def test_counter_completion(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 9 Right Ramp Shots and check counter value
        for i in range(9):
            self.mock_event("ce_counting_qualifying_shots")
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
            self.assertEventCalled("ce_counting_qualifying_shots")
            self.reset_mock_events()
            self.assertEqual(i+1, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Shot 10
        self.mock_event("ce_counting_qualifying_shots")
        self.mock_event("ce_lb_spells_light_qualify_counter_completed")
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        self.assertEventCalled("ce_counting_qualifying_shots")
        self.assertEventCalled("ce_lb_spells_light_qualify_counter_completed")
        self.reset_mock_events()

        # Check qualify counter
        self.assertEqual(False, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Ensure that shots are in proper shot_state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
        
    def test_counter_persist_state(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 3 Right Ramp Shots
        for i in range(3):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check qualify counter
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(3, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Drain aball, plunge ball 2 and advance skillshot platform
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)

        # Check qualify counter persist state
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(3, self.machine.counters["lb_spells_light_qualify_counter"].value)
        
        # Make another 3 Right Ramp Shots and check counter value
        for i in range(3):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
            self.assertEqual(3+(i+1), self.machine.counters["lb_spells_light_qualify_counter"].value)
    
    def test_spells_light_state(self):
    
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Make 10 Right Ramp Shots to complete counter and advance Spells Light to lit
        for i in range(10):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Make a shot to advance Spells Light to active
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("active", self.machine.shots["sh_spells_light"].state_name)

    def test_spells_light_persist_state(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

        # Make 10 Right Ramp Shots to complete counter and advance Spells Light to lit
        for i in range(10):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Drain aball, plunge ball 2 and advance skillshot platform
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)

        # Check Spells Light persist_state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_spells_light"].state_name)

        # Make a shot to advance Spells Light to active
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check Spells Light persist_state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("active", self.machine.shots["sh_spells_light"].state_name)

        # Drain aball, plunge ball 2 and advance skillshot platform
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(3)

        # Check Spells Light persist_state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

    def test_spells_light_counter_reset(self):    

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 10 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check qualify counter
        self.assertEqual(False, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("active", self.machine.shots["sh_spells_light"].state_name)

        # Make last shot and check counter reset event
        self.mock_event("ce_reset_spells_light_qualify_counter")
        self.assertEventNotCalled("ce_reset_spells_light_qualify_counter")
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        self.assertEventCalled("ce_reset_spells_light_qualify_counter")
        self.reset_mock_events()

        # Check qualify counter reset
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(0, self.machine.counters["lb_spells_light_qualify_counter"].value)

        # Right Ramp Shot 
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Drain a ball and check counter_reset event
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)

        # Check qualify counter reset
        self.assertEqual(True, self.machine.counters["lb_spells_light_qualify_counter"].enabled)
        self.assertEqual(1, self.machine.counters["lb_spells_light_qualify_counter"].value)

        # Check Spells Light shot and state
        self.assertTrue(self.machine.shots["sh_spells_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_spells_light"].state_name)

    def test_right_ramp_light_state(self):
        
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 10 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(10):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check Right Ramp Light state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)

        # Make a shot to advance Right Ramp Light to lit
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check Right Ramp Light state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_right_ramp_light"].state_name)

    def test_right_ramp_light_non_persist_state(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check Right Ramp Light state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertEqual("lit", self.machine.shots["sh_right_ramp_light"].state_name)

        # Drain a ball and check counter_reset event
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)

        # Check Right Ramp Light state
        self.assertTrue(self.machine.shots["sh_right_ramp_light"].enabled)
        self.assertEqual("unlit", self.machine.shots["sh_right_ramp_light"].state_name)
    
    def test_timer_start(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 10 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(10):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)
        
        # Make a shot to advance Right Ramp Light to lit and check for the start the timer event
        self.mock_event("ce_start_qualifying_timer")
        self.assertEventNotCalled("ce_start_qualifying_timer")
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        self.assertEventCalled("ce_start_qualifying_timer")
        self.reset_mock_events()

        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(1, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Run for 13 seconds and check timer ticks
        self.advance_time_and_run(13)
        self.assertEqual(14, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Last second before timer ends and check timer
        self.advance_time_and_run(1)

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

    def test_timer_drain_reset(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(1, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        self.mock_event("ce_reset_qualifying_timer")
        self.assertEventNotCalled("ce_reset_qualifying_timer")

        # Drain a ball
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)
        
        # Check timer reset event and timer itself
        self.assertEventCalled("ce_reset_qualifying_timer")
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)
        self.reset_mock_events()

    def test_timer_completion_and_reset(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(1, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        self.mock_event("ce_reset_qualifying_timer")
        self.mock_event("timer_right_ramp_light_qualify_timer_complete")
        self.assertEventNotCalled("ce_reset_qualifying_timer")
        self.assertEventNotCalled("timer_right_ramp_light_qualify_timer_complete")

        # Run for 14 seconds and check timer complete and reset events
        self.advance_time_and_run(14)
        self.assertEventCalled("ce_reset_qualifying_timer")
        self.assertEventCalled("timer_right_ramp_light_qualify_timer_complete")
        self.reset_mock_events()

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

    def test_timer_counter_reset(self):
        
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check qualify counter
        self.mock_event("ce_reset_qualifying_timer")
        self.mock_event("timer_right_ramp_light_qualify_timer_complete")
        self.assertEventNotCalled("ce_reset_qualifying_timer")
        self.assertEventNotCalled("timer_right_ramp_light_qualify_timer_complete")

        # Run for 14 seconds and check timer complete and reset events
        self.advance_time_and_run(14)
        self.assertEventCalled("ce_reset_qualifying_timer")
        self.assertEventCalled("timer_right_ramp_light_qualify_timer_complete")
        self.reset_mock_events()

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

    def test_state_machine_succes(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check level state_machine
        self.assertEqual("Spell 1", self.machine.state_machines["sm_spells_level"].state)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check level state_machine
        self.assertEqual("Spell 1", self.machine.state_machines["sm_spells_level"].state)

        # Check qualify timer
        self.assertEqual(True, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(1, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Make last Right Ramp Shot to complete and check timer reset and stop events
        self.mock_event("ce_qualification_completed_succesfully")
        self.mock_event("ce_advance_spells_level_sate_machine")
        self.mock_event("ce_stop_qualifying_timer")
        self.mock_event("ce_reset_qualifying_timer")
        self.assertEventNotCalled("ce_qualification_completed_succesfully")
        self.assertEventNotCalled("ce_advance_spells_level_sate_machine")
        self.assertEventNotCalled("ce_stop_qualifying_timer")
        self.assertEventNotCalled("ce_reset_qualifying_timer")
        self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        self.assertEventCalled("ce_qualification_completed_succesfully")
        self.assertEventCalled("ce_advance_spells_level_sate_machine")
        self.assertEventCalled("ce_stop_qualifying_timer")
        self.assertEventCalled("ce_reset_qualifying_timer")
        self.reset_mock_events()

        # Check qualify timer
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)

        # Check level state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)

        # Advance some time
        self.advance_time_and_run(30)

        # Check qualify timer and state_machine
        self.assertEqual(False, self.machine.timers["right_ramp_light_qualify_timer"].running)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].start_value)
        self.assertEqual(0, self.machine.timers["right_ramp_light_qualify_timer"].ticks)
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)

    def test_state_machine_timer_timeout(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check level state_machine
        self.assertEqual("Spell 1", self.machine.state_machines["sm_spells_level"].state)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check level state_machine
        self.assertEqual("Spell 1", self.machine.state_machines["sm_spells_level"].state)

        # Advance some time
        self.mock_event("timer_right_ramp_light_qualify_timer_complete")
        self.mock_event("ce_advance_spells_level_sate_machine")
        self.assertEventNotCalled("timer_right_ramp_light_qualify_timer_complete")
        self.assertEventNotCalled("ce_advance_spells_level_sate_machine")
        self.advance_time_and_run(30)

        # Check for timer complete event and state_machine level up event
        self.assertEventCalled("timer_right_ramp_light_qualify_timer_complete")
        self.assertEventCalled("ce_advance_spells_level_sate_machine")

        # Check level state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)

        # Advance some time
        self.advance_time_and_run(30)

        # Check qualify timer and state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)
    
    def test_state_machine_persist_state(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Check level state_machine
        self.assertEqual("Spell 1", self.machine.state_machines["sm_spells_level"].state)

        # Make 11 Right Ramp Shots to complete counter and advance Spells Light to active
        for i in range(12):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check level state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)

        # Drain a ball
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)

        # Check level state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)
        
        # Drain a ball
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(3)

        # Check level state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)
    
class test_mode_score(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'
    
    def test_counter_hit_score(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Award 10 points when counter_complete event is posted
        for i in range(9):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
            self.assertPlayerVarEqual(10*(i+1),"var_score")

        # Check if score is 80
        self.assertPlayerVarEqual(90,"var_score")
    
    def test_counter_complete_score(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Award 10 points when counter_complete event is posted
        # Award 1,500 points when counter_complete event is posted
        for i in range(10):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check if score is 1,600 (10*10+1500)
        self.assertPlayerVarEqual(1600,"var_score")
        
    
    def test_spells_light_active_hit_score(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Award 10 points when counter_complete event is posted
        # Award 1,500 points when counter_complete event is posted
        # Award 25,000 points when spells_light_active_hit is posted
        for i in range(12):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check if score is 1,600 (10*10+1500+25000)
        self.assertPlayerVarEqual(26600,"var_score")

    def test_spells_light_active_timeout_score(self):

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Award 10 points when counter_complete event is posted
        # Award 1,500 points when counter_complete event is posted
        # Award 25,000 points when spells_light_active_hit is posted
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Advance some time to timeout timer
        self.advance_time_and_run(20)

        # Check if score is 1,600 (10*10+1500)
        self.assertPlayerVarEqual(1600,"var_score")

class test_scenario(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'
    
    def test_case(self):

        # Ball 1 - Spell 1 and Spell 2
        # Ball 2 - 5 shots of Spell 3
        # Ball 3 - 7 shots (5+2) of Spell 3 and 11 shots (10+1+timer_timeout) of Spell 4

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Make 12 Right Ramp Shots
        for i in range(12):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check score
        self.assertPlayerVarEqual(26600,"var_score")

        # Check level state_machine
        self.assertEqual("Spell 2", self.machine.state_machines["sm_spells_level"].state)

        # Make 11 Right Ramp Shots
        for i in range(12):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)
        
        # Check score
        self.assertPlayerVarEqual(53200,"var_score")

        # Check level state_machine
        self.assertEqual("Spell 3", self.machine.state_machines["sm_spells_level"].state)

        # Drain a ball
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(2)

        # Check level state_machine
        self.assertEqual("Spell 3", self.machine.state_machines["sm_spells_level"].state)

        # Make 5 Right Ramp Shots
        for i in range(5):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check score
        self.assertPlayerVarEqual(53250,"var_score")
        
        # Drain a ball
        self.drain_one_ball()
        self.advance_time_and_run(5)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)
        self.assertBallNumber(3)

        # Check level state_machine
        self.assertEqual("Spell 3", self.machine.state_machines["sm_spells_level"].state)

        # Make 7 Right Ramp Shots
        for i in range(7):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check score
        self.assertPlayerVarEqual(79800,"var_score")

        # Check level state_machine
        self.assertEqual("Spell 4", self.machine.state_machines["sm_spells_level"].state)

        # Make 11 Right Ramp Shots
        for i in range(11):
            self.post_event("sq_shot_spells_ramp_hit", run_time=1)

        # Check score
        self.assertPlayerVarEqual(81400,"var_score")

        # Advance some time
        self.advance_time_and_run(20)    

        # Check level state_machine
        self.assertEqual("Spell 5", self.machine.state_machines["sm_spells_level"].state)

        # Check score
        self.assertPlayerVarEqual(81400,"var_score")