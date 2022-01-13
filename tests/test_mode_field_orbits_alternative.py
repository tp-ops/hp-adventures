from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_shots(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\Source Code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_auto_stop_mode(self):

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

        # Stop default running mode field_orbits 
        self.stop_mode("field_orbits")
        self.assertModeNotRunning("field_orbits")

        # Start mode field_orbit_alternative
        self.start_mode("field_orbits_alternative")

        # Ensure that mode field_orbits_alternative is running and field_orbits is not running
        self.assertModeRunning("field_orbits_alternative")

        # Start mode field_orbit
        self.start_mode("field_orbits")

        # Ensure that mode field_orbits is running and field_orbits_alternative is not running
        self.assertModeRunning("field_orbits")
        self.assertModeNotRunning("field_orbits_alternative")

    def test_left_orbit_big_alt(self):

        self.get_options()

        # Mock events
        self.mock_event("enable_div_castle")
        self.mock_event("enable_div_forest")
        self.mock_event("enable_sh_left_orbit_lane_alt")
        self.mock_event("enable_sh_right_orbit_lane_alt")
        self.mock_event("enable_sh_castle_orbit_lane_alt")
       
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

        # Stop mode field_orbits and start mode field_orbits_alternative
        self.stop_mode("field_orbits")
        self.advance_time_and_run(1)
        self.start_mode("field_orbits_alternative")

        # Ensure that mode field_orbits is running and that enable_events for diverter and lane shots are fired
        self.assertModeRunning("field_orbits_alternative")
        self.assertEventCalled("enable_div_castle")
        self.assertEventCalled("enable_div_forest")
        self.assertEventCalled("enable_sh_left_orbit_lane_alt")
        self.assertEventCalled("enable_sh_right_orbit_lane_alt")
        self.assertEventCalled("enable_sh_castle_orbit_lane_alt")
        self.reset_mock_events()

        # Ensure that diverters and lane shots are enabled
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)  
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Test sequence time-out
        # Hit s_orbit_left switch (left orbit lane alt) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.assertEventCalled("activate_div_castle")
        self.reset_mock_events()
        
        # Other lanes shots will be disabled
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(True, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another second and diverter should be deactivated (2 seconds after lane shot is hit)
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
        self.mock_event("sq_shot_left_orbit_big_alt_timeout")
        self.advance_time_and_run(2)
        self.assertEventCalled("sq_shot_left_orbit_big_alt_timeout")
        self.reset_mock_events()

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
        
        # Test sequence hit
        # Hit s_orbit_left switch (left orbit lane alt) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_left")
        self.advance_time_and_run(1)
        self.assertEventCalled("activate_div_castle")
        self.reset_mock_events()
        
        # Other lanes shots will be disabled
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(True, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another second and diverter should be deactivated (2 seconds after lane shot is hit)
        self.mock_event("deactivate_div_castle")
        self.advance_time_and_run(1)
        self.assertEventCalled("deactivate_div_castle")
        self.reset_mock_events()

        # Check diverter state
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
  
        # Hit s_orbit_right switch to complete left_orbit_big_alt sequence before sequence time-out is reached
        self.mock_event("sq_shot_left_orbit_big_alt_hit")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)
        self.assertEventCalled("sq_shot_left_orbit_big_alt_hit")
        self.reset_mock_events()

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

    def test_left_orbit_small_alt(self):

        self.get_options()

        # Mock events
        self.mock_event("enable_div_castle")
        self.mock_event("enable_div_forest")
        self.mock_event("enable_sh_left_orbit_lane_alt")
        self.mock_event("enable_sh_right_orbit_lane_alt")
        self.mock_event("enable_sh_castle_orbit_lane_alt")
       
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

        # Stop mode field_orbits and start mode field_orbits_alternative
        self.stop_mode("field_orbits")
        self.advance_time_and_run(1)
        self.start_mode("field_orbits_alternative")

        # Ensure that mode field_orbits is running and that enable_events for diverter and lane shots are fired
        self.assertModeRunning("field_orbits_alternative")
        self.assertEventCalled("enable_div_castle")
        self.assertEventCalled("enable_div_forest")
        self.assertEventCalled("enable_sh_left_orbit_lane_alt")
        self.assertEventCalled("enable_sh_right_orbit_lane_alt")
        self.assertEventCalled("enable_sh_castle_orbit_lane_alt")
        self.reset_mock_events()

        # Ensure that diverters and lane shots are enabled
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)  
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Test sequence time-out
        # Hit s_div_castle switch (castle orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(1)
        self.assertEventNotCalled("activate_div_castle")
        self.reset_mock_events()
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.mock_event("sq_shot_left_orbit_small_alt_timeout")
        self.advance_time_and_run(2)
        self.assertEventCalled("sq_shot_left_orbit_small_alt_timeout")
        self.reset_mock_events()

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
        
        # Test sequence hit
        # Hit s_div_castle switch (castle orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(1)
        self.assertEventNotCalled("activate_div_castle")
        self.reset_mock_events()
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Diverter forest still deactive and diverter castle will be active
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Hit s_orbit_right switch to complete left_orbit_small sequence before sequence time-out is reached
        self.mock_event("sq_shot_left_orbit_small_alt_hit")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(0.1)
        self.assertEventCalled("sq_shot_left_orbit_small_alt_hit")
        self.reset_mock_events()

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

    def test_right_orbit_small_alt(self):

        self.get_options()

        # Mock events
        self.mock_event("enable_div_castle")
        self.mock_event("enable_div_forest")
        self.mock_event("enable_sh_left_orbit_lane_alt")
        self.mock_event("enable_sh_right_orbit_lane_alt")
        self.mock_event("enable_sh_castle_orbit_lane_alt")
       
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

        # Stop mode field_orbits and start mode field_orbits_alternative
        self.stop_mode("field_orbits")
        self.advance_time_and_run(1)
        self.start_mode("field_orbits_alternative")

        # Ensure that mode field_orbits is running and that enable_events for diverter and lane shots are fired
        self.assertModeRunning("field_orbits_alternative")
        self.assertEventCalled("enable_div_castle")
        self.assertEventCalled("enable_div_forest")
        self.assertEventCalled("enable_sh_left_orbit_lane_alt")
        self.assertEventCalled("enable_sh_right_orbit_lane_alt")
        self.assertEventCalled("enable_sh_castle_orbit_lane_alt")
        self.reset_mock_events()

        # Ensure that diverters and lane shots are enabled
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)  
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Test sequence time-out
        # Hit s_orbit_right switch (right orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
        self.assertEventNotCalled("activate_div_castle")
        self.reset_mock_events()
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Both diverters should be deactive
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Advance for another two seconds to test sequence time-out (3 seconds after lane shot is hit)
        self.mock_event("sq_shot_right_orbit_small_alt_timeout")
        self.advance_time_and_run(2)
        self.assertEventCalled("sq_shot_right_orbit_small_alt_timeout")
        self.reset_mock_events()

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)
        
        # Test sequence hit
        # Hit s_orbit_right switch (right orbit lane) and advance for 1 second (sequence time-out is 3 seconds)
        self.mock_event("activate_div_castle")
        self.hit_and_release_switch("s_orbit_right")
        self.advance_time_and_run(1)
        self.assertEventNotCalled("activate_div_castle")
        self.reset_mock_events()
        
        # Other lanes shots will be disabled
        self.assertFalse(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertFalse(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Both diverters should be deactive
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)

        # Hit s_div_castle switch to complete right_orbit_small sequence before sequence time-out is reached
        self.mock_event("sq_shot_right_orbit_small_alt_hit")
        self.hit_and_release_switch("s_div_castle")
        self.advance_time_and_run(0.1)
        self.assertEventCalled("sq_shot_right_orbit_small_alt_hit")
        self.reset_mock_events()

        # Check lane shots states, should all be enabled again
        self.assertTrue(self.machine.shots["sh_left_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_right_orbit_lane_alt"].enabled)
        self.assertTrue(self.machine.shots["sh_castle_orbit_lane_alt"].enabled)

        # Check diverter states
        self.assertEqual(True, self.machine.diverters.div_castle.enabled)
        self.assertEqual(True, self.machine.diverters.div_forest.enabled)
        self.assertEqual(False, self.machine.diverters.div_castle.active)
        self.assertEqual(False, self.machine.diverters.div_forest.active)