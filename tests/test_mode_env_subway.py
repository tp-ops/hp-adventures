from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_mode_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_start_logic(self):

        self.get_options()

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # Center state
        self.assertModeRunning("env_subway")
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)

    def test_sm_center_to_flipper_state(self):

        self.get_options()
        
        # Mock events
        self.mock_event("test_event_back_to_center")

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # center to flipper left
        self.hit_and_release_switch("s_fl_left_a")
        self.assertEqual("flipper_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.hit_and_release_switch("s_fl_left_a")
        self.assertEqual("flipper_left", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # back to center
        self.post_event("test_event_back_to_center", run_time=1)
        self.assertEqual("center", self.machine.state_machines["sm_subway_vuk_selector"].state)

        # center flipper right
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("flipper_right", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.hit_and_release_switch("s_fl_right_a")
        self.assertEqual("flipper_right", self.machine.state_machines["sm_subway_vuk_selector"].state)

    
    def test_sm_flipper_to_flipper_state(self):

        self.get_options()

    def test_sm_flipper_to_custom_state(self):

        self.get_options()

    def test_sm_center_to_custom_state(self):

        self.get_options()

    def test_sm_custom_to_custom_state(self):

        self.get_options()


    def test_sm_block_custom_to_flipper(self):

        self.get_options()

        # Mock events
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_left")
        self.mock_event("ce_sm_subway_vuk_selector_set_custom_right")

        # Starting a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.advance_time_and_run(15)

        # custom left
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        
        # custom right
        self.post_event("ce_sm_subway_vuk_selector_set_custom_left", run_time=1)
        self.assertEqual("custom_left", self.machine.state_machines["sm_subway_vuk_selector"].state)
        # again
        self.post_event("ce_sm_subway_vuk_selector_set_custom_right", run_time=1)
        self.assertEqual("custom_right", self.machine.state_machines["sm_subway_vuk_selector"].state)


    def test_mode_start_logic(self):

        self.get_options()


    def test_ball_eject_flipper_left(self):

        self.get_options()

        #and servo pos


    def test_ball_eject_flipper_right(self):

        self.get_options()


    def test_ball_eject_custom_left(self):

        self.get_options()
        

    def test_ball_eject_custom_right(self):

        self.get_options()