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


    def test_start_logic(self):

        # Starting a game
        self._start_game()

        # Center state and position
        self.assertModeRunning("env_subway")
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)
        self.assertEqual(0.5, self.machine.servos["servo_subway_vuk_selector"]._position)

    def test_sm_center_to_flipper_state(self):
        
        # Mock events
        self.mock_event("unittest_event_back_to_center")

        # Starting a game
        self._start_game()

        # center to flipper left
        self.hit_and_release_switch("s_fl_left_a")
        self.assertEqual("flipper_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.hit_and_release_switch("s_fl_left_a")
        self.assertEqual("flipper_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # center flipper right
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("flipper_right", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("flipper_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)
    
    def test_sm_flipper_to_flipper_state(self):

        # Starting a game
        self._start_game()

        # set to flipper left
        self.hit_and_release_switch("s_fl_left_a")

        # flipper left to flipper right
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("flipper_right", self.machine.state_machines["sm_subway_vuk_selector"].state)
        
        # flipper right to flipper left
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("flipper_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

    def test_sm_flipper_to_custom_state(self):
        
        # Mock events
        self.mock_event("unittest_event_back_to_center")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_left")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_right")

        # Starting a game
        self._start_game()

        # set to flipper left
        self.hit_and_release_switch("s_fl_left_a")

        # flipper left to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        
        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)

        # set to flipper left
        self.hit_and_release_switch("s_fl_left_a")

        # flipper left to custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)

        # set to flipper right
        self.hit_and_release_switch("s_fl_right_a")

        # flipper right to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)

        # set to flipper right
        self.hit_and_release_switch("s_fl_right_a")

        # flipper right to custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

    def test_sm_center_to_custom_state(self):
        
        # Mock events
        self.mock_event("unittest_event_back_to_center")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_left")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_right")

        # Starting a game
        self._start_game()

        # center to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # center custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("unittest_event_back_to_center", run_time=1)
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)

    def test_sm_custom_to_custom_state(self):
        
        # Mock events
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_left")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_right")

        # Starting a game
        self._start_game()

        # set to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        
        # custom left to custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # custom left to custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

    def test_sm_block_custom_to_flipper(self):
        
        # Mock events
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_left")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_right")

        # Starting a game
        self._start_game()

        # set to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        
        # block custom left to flipper left        
        self.hit_and_release_switch("s_fl_left_a")
        # still custom left
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # block custom left to flipper right        
        self.hit_and_release_switch("s_fl_right_a")
        # still custom left
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # set to custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        
        # block custom right to flipper left        
        self.hit_and_release_switch("s_fl_left_a")
        # still custom right
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # block custom right to flipper right        
        self.hit_and_release_switch("s_fl_right_a")
        # still custom left
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

    def test_ball_eject_flipper_left(self):

        # Mock events
        self.mock_event("srv_subway_vuk_selector_pos_left")
        self.mock_event("srv_subway_vuk_selector_pos_center")
        self.mock_event("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.mock_event("balldevice_bd_subway_vuk_selector_ball_eject_success")

        # Starting a game
        self._start_game()

        # set to flipper left
        self.hit_and_release_switch("s_fl_left_a")
        self.assertEqual("idle", self.machine.ball_devices["bd_subway_vuk_selector"].state)

        # add a ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 1)
        self.advance_time_and_run(1)

        # check for events and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.assertEventCalled("srv_subway_vuk_selector_pos_left")
        self.assertEqual(0.0, self.machine.servos["servo_subway_vuk_selector"]._position)
        
        # eject ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 0)
        self.machine.switch_controller.process_switch("s_subway_vuk_left_buffer_1", 1)
        self.advance_time_and_run(1)

        # check eject_success and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ball_eject_success")
        self.assertEventCalled("srv_subway_vuk_selector_pos_center")
        self.assertEqual(0.5, self.machine.servos["servo_subway_vuk_selector"]._position)

    def test_ball_eject_flipper_right(self):

        # Mock events
        self.mock_event("srv_subway_vuk_selector_pos_right")
        self.mock_event("srv_subway_vuk_selector_pos_center")
        self.mock_event("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.mock_event("balldevice_bd_subway_vuk_selector_ball_eject_success")

        # Starting a game
        self._start_game()

        # set to flipper left
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("idle", self.machine.ball_devices["bd_subway_vuk_selector"].state)

        # add a ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 1)
        self.advance_time_and_run(1)

        # check for events and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.assertEventCalled("srv_subway_vuk_selector_pos_right")
        self.assertEqual(1.0, self.machine.servos["servo_subway_vuk_selector"]._position)
        
        # eject ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 0)
        self.machine.switch_controller.process_switch("s_subway_vuk_right_buffer_1", 1)
        self.advance_time_and_run(1)

        # check eject_success and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ball_eject_success")
        self.assertEventCalled("srv_subway_vuk_selector_pos_center")
        self.assertEqual(0.5, self.machine.servos["servo_subway_vuk_selector"]._position)

    def test_ball_eject_custom_left(self):

        # Mock events
        self.mock_event("srv_subway_vuk_selector_pos_left")
        self.mock_event("srv_subway_vuk_selector_pos_center")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_left")
        self.mock_event("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.mock_event("balldevice_bd_subway_vuk_selector_ball_eject_success")

        # Starting a game
        self._start_game()

        # set to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("idle", self.machine.ball_devices["bd_subway_vuk_selector"].state)

        # add a ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 1)
        self.advance_time_and_run(1)

        # check for events and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.assertEventCalled("srv_subway_vuk_selector_pos_left")
        self.assertEqual(0.0, self.machine.servos["servo_subway_vuk_selector"]._position)
        
        # eject ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 0)
        self.machine.switch_controller.process_switch("s_subway_vuk_left_buffer_1", 1)
        self.advance_time_and_run(1)

        # check eject_success and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ball_eject_success")
        self.assertEventCalled("srv_subway_vuk_selector_pos_center")
        self.assertEqual(0.5, self.machine.servos["servo_subway_vuk_selector"]._position)  

    def test_ball_eject_custom_right(self):

        # Mock events
        self.mock_event("srv_subway_vuk_selector_pos_right")
        self.mock_event("srv_subway_vuk_selector_pos_center")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_right")
        self.mock_event("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.mock_event("balldevice_bd_subway_vuk_selector_ball_eject_success")

        # Starting a game
        self._start_game()

        # set to custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)

        # add a ball
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 1)
        
        self.assertEqual("idle", self.machine.ball_devices["bd_subway_vuk_selector"].state)
        self.advance_time_and_run(1)

        # check for events and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ejecting_ball")
        self.assertEventCalled("srv_subway_vuk_selector_pos_right")
        self.assertEqual(1.0, self.machine.servos["servo_subway_vuk_selector"]._position)
                
        # eject ball to next target
        self.machine.switch_controller.process_switch("s_subway_vuk_selector", 0)
        self.machine.switch_controller.process_switch("s_subway_vuk_right_buffer_1", 1)
        self.advance_time_and_run(1)

        # check eject_success and servo pos
        self.assertEventCalled("balldevice_bd_subway_vuk_selector_ball_eject_success")
        self.assertEventCalled("srv_subway_vuk_selector_pos_center")
        self.assertEqual(0.5, self.machine.servos["servo_subway_vuk_selector"]._position)  