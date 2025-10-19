from mpf.tests.MpfGameTestCase import MpfGameTestCase

class TestFieldQuidditchStadium(MpfGameTestCase):

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

    def test_qualifying_accrual_completion(self):
        """Hitting all 3 pop qualify shots should complete the qualifying accrual."""
        self._start_game()
        self.advance_time_and_run(1)

        # Start the mode
        #self.post_event('start_mode_field_quidditch_stadium')
        #self.advance_time_and_run(1)
        self.assertModeRunning('field_quidditch_stadium')

        # Initially the qualifying accrual should be enabled
        lb = self.device.logic_blocks['lb_quidditch_statium_qualifying_accrual']
        self.assertTrue(lb.enabled)

        # Hit each qualifying pop shot
        self.post_event('sh_core_pop_left_hit')
        self.advance_time_and_run()
        self.post_event('sh_core_pop_right_hit')
        self.advance_time_and_run()
        self.post_event('sh_core_pop_bottom_hit')
        self.advance_time_and_run()

        # Qualifying accrual should now be complete
        self.assertEventPosted('logicblock_lb_quidditch_statium_qualifying_accrual_complete')
        self.assertTrue(lb.completed)

    def test_pop_counters_and_stadium_accrual(self):
        """After qualifying, hitting 16 shots per pop should complete the stadium accrual."""
        self._start_game()
        self.post_event('start_mode_field_quidditch_stadium')
        self.advance_time_and_run(1)

        # Qualify first
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run()

        # Counters should now be enabled
        left_counter = self.machine.counters['lb_pop_left_shot_counter']
        right_counter = self.machine.counters['lb_pop_right_shot_counter']
        bottom_counter = self.machine.counters['lb_pop_bottom_shot_counter']

        self.assertTrue(left_counter.enabled)
        self.assertTrue(right_counter.enabled)
        self.assertTrue(bottom_counter.enabled)

        # Simulate hitting 16 times per pop
        for i in range(16):
            self.post_event('sh_core_pop_left_hit')
            self.post_event('sh_core_pop_right_hit')
            self.post_event('sh_core_pop_bottom_hit')
            self.advance_time_and_run()

        self.assertEqual(left_counter.value, 16)
        self.assertEqual(right_counter.value, 16)
        self.assertEqual(bottom_counter.value, 16)

        # Check if stadium accrual completed
        self.assertEventPosted('logicblock_lb_quidditch_stadium_accrual_complete')

    def test_final_orbit_completion(self):
        """Orbit shot after stadium completion should complete final accrual."""
        self._start_game()
        self.post_event('start_mode_field_quidditch_stadium')
        self.advance_time_and_run(1)

        # Qualify first
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run()

        # Complete pop counters to finish stadium accrual
        for i in range(16):
            self.post_event('sh_core_pop_left_hit')
            self.post_event('sh_core_pop_right_hit')
            self.post_event('sh_core_pop_bottom_hit')
            self.advance_time_and_run()

        # Now orbit shot should be lit
        orbit_shot = self.machine.device_manager.collections['shots']['sh_quidditch_orbit']
        self.assertEqual(orbit_shot.state_name, 'lit')

        # Hit orbit
        self.post_event('sq_shot_orbit_big_left_hit')
        self.advance_time_and_run()

        # Should complete final accrual
        self.assertEventPosted('you_are_a_quidditch_player')

    def test_mode_stop_resets(self):
        """Stopping the mode should disable counters and reset states."""
        self._start_game()
        self.post_event('start_mode_field_quidditch_stadium')
        self.advance_time_and_run(1)

        # Qualify
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run()

        self.post_event('stop_mode_field_quidditch_stadium')
        self.advance_time_and_run()

        self.assertFalse(self.machine.counters['lb_pop_left_shot_counter'].enabled)
        self.assertFalse(self.get_mode().active)

