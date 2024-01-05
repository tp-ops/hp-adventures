from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_mode_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_mode_start_logic(self):

        # Mock events
        self.mock_event("enable_div_castle")
        self.mock_event("enable_div_forest")
        self.mock_event("enable_sh_orbit_lane_left_opt1")
        self.mock_event("enable_sh_orbit_lane_right_opt1")
        self.mock_event("enable_sh_orbit_lane_center_opt1")

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 
        self.assertModeRunning("field_orbits_option1")
        self.assertModeNotRunning("field_orbits_option2")
        self.assertModeNotRunning("field_orbits_option3")

        # Ensure that enable_events for diverter and lane shots are fired
        self.assertEventCalled("enable_div_castle")
        self.assertEventCalled("enable_div_forest")
        self.assertEventCalled("enable_sh_orbit_lane_left_opt1")
        self.assertEventCalled("enable_sh_orbit_lane_right_opt1")
        self.assertEventCalled("enable_sh_orbit_lane_center_opt1")
        self.reset_mock_events()

        # Ensure that diverters and lane shots are enabled
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)  
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_left_long_hit(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 
        
        # Hit s_orbit_left switch (left orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(2)
  
        # Hit s_orbit_right switch to complete orbit_left_long sequence before sequence time-out is reached
        self.mock_event("sq_shot_orbit_left_long_opt1_hit")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)
        self.assertEventCalled("sq_shot_orbit_left_long_opt1_hit")
        self.reset_mock_events()
    
    def test_orbit_left_long_hit_lanes(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 
        
        # Hit s_orbit_left switch (left orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        
        # Other lanes shots then left will be disabled
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

        # Hit s_orbit_right switch to complete orbit_left_long sequence before sequence time-out is reached
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)

        # Check lane shots states, should be all enabled again
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_left_long_hit_diverters(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 
        
        # Hit s_orbit_left switch (left orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.assertEventCalled("activate_div_castle")
        self.reset_mock_events()
  
        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(True, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another second and diverter should be disactivated (2 seconds after lane shot is hit)
        self.mock_event("deactivate_div_castle")
        self.advance_time_and_run(1)
        self.assertEventCalled("deactivate_div_castle")
        self.reset_mock_events()

        # Check diverter state
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
  
        # Hit s_orbit_right switch to complete orbit_left_long sequence before sequence time-out is reached
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

    def test_orbit_left_long_timeout(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_left switch (left orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(2)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.mock_event("sq_shot_orbit_left_long_opt1_timeout")
        self.advance_time_and_run(2)
        self.assertEventCalled("sq_shot_orbit_left_long_opt1_timeout")
        self.reset_mock_events()

    def test_orbit_left_long_timeout_lanes(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_left switch (left orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        
        # Other lanes shots will be disabled
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

        # Advance for another 3 seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.advance_time_and_run(3)

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_left_long_timeout_diverters(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_left switch (left orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.assertEventCalled("activate_div_castle")
        self.reset_mock_events()

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(True, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another second and diverter should be disactivated (2 seconds after lane shot is hit)
        self.mock_event("deactivate_div_castle")
        self.advance_time_and_run(1)
        self.assertEventCalled("deactivate_div_castle")
        self.reset_mock_events()

        # Check diverter state
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.advance_time_and_run(2)
        
        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)


    def test_orbit_right_long_hit(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 
        
        # Hit s_orbit_right switch (right orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(2)
  
        # Hit s_orbit_left switch to complete orbit_right_long sequence before sequence time-out is reached
        self.mock_event("sq_shot_orbit_right_long_opt1_hit")
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(0.1)
        self.assertEventCalled("sq_shot_orbit_right_long_opt1_hit")
        self.reset_mock_events()

    def test_orbit_right_long_hit_lanes(self):

        self.get_options()
               
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_right switch (right orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(2)
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

        # Hit s_orbit_left switch to complete orbit_right_long sequence before sequence time-out is reached
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(0.1)

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_right_long_hit_diverters(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_right switch (right orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
        self.assertEventCalled("activate_div_castle")
        self.reset_mock_events()

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(True, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another second and diverter should be disactivated (2 seconds after lane shot is hit)
        self.mock_event("deactivate_div_castle")
        self.advance_time_and_run(1)
        self.assertEventCalled("deactivate_div_castle")
        self.reset_mock_events()

        # Check diverter state
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
  
        # Hit s_orbit_left switch to complete right_orbit_big sequence before sequence time-out is reached
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(0.1)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

    def test_orbit_right_long_timeout(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_right switch (right orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(2)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.mock_event("sq_shot_orbit_right_long_opt1_timeout")
        self.advance_time_and_run(2)
        self.assertEventCalled("sq_shot_orbit_right_long_opt1_timeout")
        self.reset_mock_events()

    def test_orbit_right_long_timeout_lanes(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_right switch (right orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)

        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

        # Advance for another 3 seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.advance_time_and_run(3)

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_right_long_timeout_diverters(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_orbit_right switch (right orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
        self.assertEventCalled("activate_div_castle")
        self.reset_mock_events()

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(True, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another second and diverter should be disactivated (2 seconds after lane shot is hit)
        self.mock_event("deactivate_div_castle")
        self.advance_time_and_run(1)
        self.assertEventCalled("deactivate_div_castle")
        self.reset_mock_events()

        # Check diverter state
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.advance_time_and_run(2)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

    def test_orbit_center_short_hit(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_div_castle switch (castle orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(2)

        # Hit s_orbit_right switch to complete orbit_center_short sequence before sequence time-out is reached
        self.mock_event("sq_shot_orbit_center_short_opt1_hit")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)
        self.assertEventCalled("sq_shot_orbit_center_short_opt1_hit")
        self.reset_mock_events()

    def test_orbit_center_short_hit_lanes(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_div_castle switch (castle orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(2)
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

        # Hit s_orbit_right switch to complete orbit_center_short sequence before sequence time-out is reached
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_center_short_hit_diverters(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_div_castle switch (castle orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(1)
        self.assertEventNotCalled("activate_div_castle")
        self.reset_mock_events()

        # Both diverters should be still deactive
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
        
        # Hit s_orbit_right switch to complete left_orbit_small sequence before sequence time-out is reached
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

    def test_orbit_center_short_timeout(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_div_castle switch (castle orbit lane) and advance for 2 seconds (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(2)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.mock_event("sq_shot_orbit_center_short_opt1_timeout")
        self.advance_time_and_run(2)
        self.assertEventCalled("sq_shot_orbit_center_short_opt1_timeout")
        self.reset_mock_events()
        
    def test_orbit_center_short_timeout_lanes(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_div_castle switch (castle orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(1)
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertFalse(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

        # Advance for another 3 seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.advance_time_and_run(3)

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_orbit_lane_left_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_right_opt1"].enabled)
        self.assertTrue(self.machine.shots["sh_orbit_lane_center_opt1"].enabled)

    def test_orbit_center_short_timeout_diverters(self):

        self.get_options()
       
        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Transition manually to mode option1
        self.post_event("ce_change_field_orbits_to_option1")
        self.advance_time_and_run(1) 

        # Hit s_div_castle switch (castle orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(1)
        self.assertEventNotCalled("activate_div_castle")
        self.reset_mock_events()

        # Both diverters should be deactive
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.advance_time_and_run(2)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)