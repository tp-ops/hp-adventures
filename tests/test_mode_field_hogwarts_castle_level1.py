from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_global_hogwarts_castle(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'D:\\Coding\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def setUp(self):
        super().setUp()
        self.start_game()
        self.start_mode('field_hogwarts_castle_level1')

    def test_drop_target_advances_unlit_to_lit(self):
        """Hit drop target with 0 locked balls -> advance from unlit to lit."""
        shot = self.machine.device_manager.collections['shots']['sh_drop1_castle_door_lvl1']
        self.assertEqual(shot.state_name, 'unlit')

        self.post_event('drop_target_bank_dtb_hogwarts_castle_down')
        self.advance_time_and_run()

        self.assertEqual(shot.state_name, 'lit')

    def test_drop_target_advances_lit_to_open(self):
        """Hit drop target when lit -> advance to open."""
        shot = self.machine.device_manager.collections['shots']['sh_drop1_castle_door_lvl1']
        shot.state_name = 'lit'
        self.post_event('drop_target_bank_dtb_hogwarts_castle_down')
        self.advance_time_and_run()
        self.assertEqual(shot.state_name, 'open')

    def test_entrance_shot_resets_drop_target(self):
        """Entrance hit should restart shot and reset drop bank."""
        shot = self.machine.device_manager.collections['shots']['sh_drop1_castle_door_lvl1']
        shot.state_name = 'open'

        self.post_event('sh_hogwarts_castle_entrance_lvl1_hit')
        self.advance_time_and_run()

        self.assertEqual(shot.state_name, 'unlit')

    def test_lock_count_behavior(self):
        """Different behavior depending on 0 or 1 locked balls."""
        lock = self.machine.multiball_locks['mbl_hogwarts_castle_lvl1_subway_left_and_right_buffers']

        # First lock
        self.add_ball_to_lock(lock)
        self.assertEqual(lock.locked_balls, 1)

        # Shot should advance from unlit to lit again
        shot = self.machine.device_manager.collections['shots']['sh_drop1_castle_door_lvl1']
        self.post_event('drop_target_bank_dtb_hogwarts_castle_down')
        self.advance_time_and_run()
        self.assertIn(shot.state_name, ['lit', 'open'])

