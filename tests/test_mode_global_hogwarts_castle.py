from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_global_hogwarts_castle(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_startup_state_level1(self):
        """Test that the state machine starts at level 1 on game start."""
        self.start_game()
        self.assertModeRunning('global_hogwarts_castle')

        # Check that the state machine is at level1
        sm = self.machine.device_manager.collections['state_machines']['sm_hogwarts_castle']
        self.assertEqual(sm.state, 'level1')

        # Check that the right field mode started
        self.assertModeRunning('field_hogwarts_castle_level1')

    def test_level_up_to_level2(self):
        """Test transition from level1 to level2."""
        self.start_game()

        # Trigger level-up event
        self.post_event('ce_levelup_hogwarts_castle_to_level2')
        self.advance_time_and_run()

        sm = self.machine.device_manager.collections['state_machines']['sm_hogwarts_castle']
        self.assertEqual(sm.state, 'level2')

        # Verify field level1 mode stopped and level2 started
        self.assertModeNotRunning('field_hogwarts_castle_level1')
        self.assertModeRunning('field_hogwarts_castle_level2')

    def test_multiball_lock_and_start(self):
        """Test locking two balls triggers multiball start and mission mode."""
        self.start_game()

        lock = self.machine.multiball_locks['mbl_hogwarts_castle_lvl1_subway_left_and_right_buffers']

        # Simulate locking first ball
        self.add_ball_to_lock(lock)
        self.assertEqual(lock.locked_balls, 1)

        # Simulate locking second ball
        self.add_ball_to_lock(lock)
        self.advance_time_and_run()
        self.assertEqual(lock.locked_balls, 2)

        # Check multiball started
        self.assertTrue(self.machine.multiballs['mb_hogwarts_castle_lvl1_2ball'].active)
        # Check mission mode started and field mode stopped
        self.assertModeRunning('mission_hogwarts_castle_lvl1')
        self.assertModeNotRunning('field_hogwarts_castle_level1')

    def test_multiball_end_levels_up(self):
        """Test ending multiball triggers level-up to level2."""
        self.start_game()

        # Lock both balls and start multiball
        lock = self.machine.multiball_locks['mbl_hogwarts_castle_lvl1_subway_left_and_right_buffers']
        self.add_ball_to_lock(lock)
        self.add_ball_to_lock(lock)
        self.advance_time_and_run()

        self.post_event('multiball_mb_hogwarts_castle_lvl1_2ball_ended')
        self.advance_time_and_run()

        sm = self.machine.device_manager.collections['state_machines']['sm_hogwarts_castle']
        self.assertEqual(sm.state, 'level2')

