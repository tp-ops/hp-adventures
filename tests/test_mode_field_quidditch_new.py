from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_game_logic(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'
    
    def _start_game(self):
        """Starting a game and progress through house_theme_selection and skill_shot mode."""

        # Start game and select a house_theme
        for i in range(2):
            self.hit_and_release_switch("s_start_button")
            self.advance_time_and_run(1)

        # Progress through skill_shot mode
        self.release_switch_and_run("s_plunger_lane", 30)

    def _drain_one_ball(self):
        """Drain one ball and progress through skill_shot mode"""

        # Drain ball
        self.drain_one_ball()
        self.advance_time_and_run(5)
        
        # Plunge ball 2 and advance skillshot platform
        self.release_switch_and_run("s_plunger_lane", 30)

    def test_mode_start_logic(self):
        """Test mode start requirements."""

        # Start a game
        self._start_game()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Ensure that mode field_quidditch_statium is running
        self.assertModeRunning("field_quidditch_stadium")

        # Ensure that shots are in proper state
        for shot in ['sh_pop_left_qualify', 'sh_pop_right_qualify', 'sh_pop_bottom_qualify']:
            self.assertTrue(self.machine.shots[shot].enabled)
            self.assertEqual("qualifying", self.machine.shots[shot].state_name)

        for shot in ['sh_pop_left', 'sh_pop_right', 'sh_pop_bottom', 'sh_quidditch_stadium', 'sh_quidditch_orbit']:
            self.assertFalse(self.machine.shots[shot].enabled)
            self.assertEqual("unlit", self.machine.shots[shot].state_name)

        # Initially the qualifying accrual should be enabled with values to false
        qualify_accrual = self.machine.accruals["lb_quidditch_statium_qualifying_accrual"]
        self.assertTrue(qualify_accrual.enabled)
        for i in range(3):
            self.assertEqual(False,qualify_accrual.value[i])

        # Are the pop bumper shot counter disabled and count 0
        for counter in ['lb_pop_left_shot_counter', 'lb_pop_right_shot_counter', 'lb_pop_bottom_shot_counter']:
            self.assertFalse(self.machine.counters[counter].enabled)
            self.assertEqual(0, self.machine.counters[counter].value)

        # Initially the quidditch stadium accrual should be disabled with values to false
        quidditch_accrual = self.machine.accruals["lb_quidditch_stadium_accrual"]
        self.assertFalse(quidditch_accrual.enabled)
        for i in range(3):
            self.assertEqual(False,quidditch_accrual.value[i])

    def test_qualifying_accrual_completion(self):
        """Hitting all 3 pop qualify shots should complete the qualifying accrual."""

        # Mock events
        for ev in ['sh_pop_left_qualify_hit', 'sh_pop_right_qualify_hit', 'sh_pop_bottom_qualify_hit',
                   'logicblock_lb_quidditch_statium_qualifying_accrual_complete']:
            self.mock_event(ev)

        # Start a game
        self._start_game()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Hit qualify shots
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run(1)

        for ev in ['sh_pop_left_qualify_hit', 'sh_pop_right_qualify_hit', 'sh_pop_bottom_qualify_hit']:
            self.assertEventCalled(ev)

        for shot in ['sh_pop_left_qualify', 'sh_pop_right_qualify', 'sh_pop_bottom_qualify']:
            self.assertEqual("qualified", self.machine.shots[shot].state_name)

        # Qualifying accrual should now be complete and qualifying shots disabled
        self.assertEventCalled('logicblock_lb_quidditch_statium_qualifying_accrual_complete')
        for shot in ['sh_pop_left_qualify', 'sh_pop_right_qualify', 'sh_pop_bottom_qualify']:
            self.assertFalse(self.machine.shots[shot].enabled)

    def test_qualifying_shots_persist_state(self):

        # Start a game
        self._start_game()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Hit left and right qualifying pop shot
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit']:
            self.post_event(ev)
            self.advance_time_and_run(1)
        
        # Check qualifying shots state
        for shot in ['sh_pop_left_qualify', 'sh_pop_right_qualify']:
            self.assertEqual("qualified", self.machine.shots[shot].state_name)
        self.assertEqual("qualifying", self.machine.shots["sh_pop_bottom_qualify"].state_name)

        # Drain one ball
        self._drain_one_ball()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Check qualifying shots state
        for shot in ['sh_pop_left_qualify', 'sh_pop_right_qualify']:
            self.assertEqual("qualified", self.machine.shots[shot].state_name)
        self.assertEqual("qualifying", self.machine.shots["sh_pop_bottom_qualify"].state_name)

    def test_qualifying_accrual_persist_state(self):

        # Start a game
        self._start_game()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Hit left and right qualifying pop shot
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit']:
            self.post_event(ev)
            self.advance_time_and_run(1)
        
        # Check accrual state
        for i in range(2):
            self.assertEqual(True,self.machine.accruals["lb_quidditch_statium_qualifying_accrual"].value[i])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_statium_qualifying_accrual"].value[2])

        # Drain one ball
        self._drain_one_ball()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Check qualifying accrual state
        for i in range(2):
            self.assertEqual(True,self.machine.accruals["lb_quidditch_statium_qualifying_accrual"].value[i])
        self.assertEqual(False,self.machine.accruals["lb_quidditch_statium_qualifying_accrual"].value[2])

    def test_pop_counters_and_stadium_accrual(self):
        """After qualifying, hitting 16 shots per pop should complete the stadium accrual."""

        # Mock events
        self.mock_event("logicblock_lb_quidditch_stadium_accrual_complete")

        # Start a game
        self._start_game()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Qualify first
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run(1)

        # Counters should now be enabled
        for counter in ['lb_pop_left_shot_counter', 'lb_pop_right_shot_counter', 'lb_pop_bottom_shot_counter']:
            self.assertTrue(self.machine.counters[counter].enabled)

        # Hitting 15 times per pop bumper
        for i in range(15):
            for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
                self.post_event(ev)
                self.advance_time_and_run(1)

        for counter in ['lb_pop_left_shot_counter', 'lb_pop_right_shot_counter', 'lb_pop_bottom_shot_counter']:
            self.assertEqual(self.machine.counters[counter].value, 15)

        # Last hit per pop bumper
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run(1)

        # Check if stadium accrual completed
        self.assertEventCalled('logicblock_lb_quidditch_stadium_accrual_complete')

    def test_final_orbit_completion(self):
        """Orbit shot after stadium completion should complete final accrual."""

        # Mock events
        self.mock_event("you_are_a_quidditch_player")

        # Start a game
        self._start_game()
        self.assertBallsOnPlayfield(1, playfield='playfield')

        # Qualify first
        for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
            self.post_event(ev)
            self.advance_time_and_run(1)

        # Complete pop counters to finish stadium accrual
        for i in range(16):
            for ev in ['sh_core_pop_left_hit', 'sh_core_pop_right_hit', 'sh_core_pop_bottom_hit']:
                self.post_event(ev)
                self.advance_time_and_run(1)

        # Now orbit shot should be lit
        orbit_shot = self.machine.device_manager.collections['shots']['sh_quidditch_orbit']
        self.assertEqual(orbit_shot.state_name, 'lit')

        # Hit orbit
        self.post_event('sq_shot_orbit_big_left_hit')
        self.advance_time_and_run(1)

        # Should complete final accrual
        self.assertEventCalled('you_are_a_quidditch_player')