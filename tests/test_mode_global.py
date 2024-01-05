from mpf.tests.MpfGameTestCase import MpfGameTestCase

class test_global_hogwarts_castle(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_castle_state_machine(self):

        self.get_options()

class test_global_orbits(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TomHuizePenningsnet\\Desktop\\Source code\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_start_mode_option1(self):

        self.get_options()
    
    def test_start_mode_option2(self):

        self.get_options()
    
    def test_start_mode_option3(self):

        self.get_options()

    def test_mode_option1_transistions(self):

        self.get_options()

    def test_stop_other_modes(self):

        self.get_options()

    def test_state_machine_remember_state(self):

        self.get_options()

    def test_var_prev_mode(self):

        self.get_options()