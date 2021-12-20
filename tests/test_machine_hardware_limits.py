from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class test_hardware_limits(MpfMachineTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\TP-OPS\\Desktop\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_clock_tower_diverters(self):

        self.get_options()

        self.mock_event("enable_div_tower_entry")
        self.mock_event("activate_div_tower_entry")
        self.mock_event("deactivate_div_tower_entry")
        self.mock_event("disable_div_tower_entry")
        
        self.mock_event("diverter_div_tower_entry_enabling")
        self.mock_event("diverter_div_tower_entry_activating")
        self.mock_event("diverter_div_tower_entry_deactivating")
        self.mock_event("diverter_div_tower_entry_disabling")

        self.mock_event("enable_div_tower_pensieve")
        self.mock_event("activate_div_tower_pensieve")
        self.mock_event("deactivate_div_tower_pensieve")
        self.mock_event("disable_div_tower_pensieve")

        self.mock_event("diverter_div_tower_pensieve_enabling")
        self.mock_event("diverter_div_tower_pensieve_activating")
        self.mock_event("diverter_div_tower_pensieve_deactivating")
        self.mock_event("diverter_div_tower_pensieve_disabling")
        
        self.assertEqual(False, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(False, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)

        self.post_event("enable_div_tower_entry")
        self.post_event("enable_div_tower_pensieve")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("diverter_div_tower_entry_enabling")
        self.assertEventCalled("diverter_div_tower_pensieve_enabling")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(False, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        # Ensure that div_tower_entry can not be disabled when it is active
        self.post_event("activate_div_tower_entry")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("diverter_div_tower_entry_activating")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        self.post_event("disable_div_tower_entry")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("disable_div_tower_entry")
        self.assertEventNotCalled("diverter_div_tower_entry_disabling")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        # Ensure that div_tower_pensieve can not be activated while div_tower_entry is deactive
        self.post_event("deactivate_div_tower_entry")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("diverter_div_tower_entry_deactivating")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(False, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        self.post_event("activate_div_tower_pensieve")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("activate_div_tower_pensieve")
        self.assertEventNotCalled("diverter_div_tower_pensieve_activating")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(False, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        # Ensure that div_tower_pensieve can not be disabled when it is active
        self.post_event("activate_div_tower_entry")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("diverter_div_tower_entry_activating")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(False, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        self.post_event("activate_div_tower_pensieve")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("diverter_div_tower_pensieve_activating")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        self.post_event("disable_div_tower_pensieve")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("disable_div_tower_pensieve")
        self.assertEventNotCalled("diverter_div_tower_pensieve_disabling")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()

        # Ensure that div_tower_entry can not be deactivated while div_tower_pensieve is active
        self.post_event("deactivate_div_tower_entry")
        self.advance_time_and_run(1)
        
        self.assertEventCalled("deactivate_div_tower_entry")
        self.assertEventNotCalled("diverter_div_tower_entry_deactivating")
        self.assertEqual(True, self.machine.diverters.div_tower_entry.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.enabled)
        self.assertEqual(True, self.machine.diverters.div_tower_entry.active)
        self.assertEqual(True, self.machine.diverters.div_tower_pensieve.active)
        self.reset_mock_events()