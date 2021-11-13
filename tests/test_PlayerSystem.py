from mpf.tests.MpfGameTestCase import MpfGameTestCase

class TestPlayerSystem(MpfGameTestCase):

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return 'C:\\Users\\Tom\\Desktop\\hp-adventures'

    def get_platform(self):
        return 'smart_virtual'

    def test_SinglePlayerGame(self):

        self.get_options()
        
        # Ensure that Attract mode is running and game mode not
        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()
        
        # Hit 'Start' button to start a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.game.num_players)
        self.assertPlayerCount(1)
        self.advance_time_and_run(1)

        # Ensure that Mode env_house_theme_selection is running
        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertGameIsRunning()
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")

        # Three ball loop
        for i in range(3):
            self.assertBallNumber(i+1)
            self.release_switch_and_run("s_plunger_lane", 11)
            self.assertBallsOnPlayfield(1, playfield='playfield')
            self.drain_one_ball()
            self.advance_time_and_run(10)

        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()

    def test_MultiPlayerGame(self):

        self.get_options()
        
        # Ensure that Attract mode is running and game mode not
        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()
        
        # Hit 'Start' button to start a game
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.game.num_players)
        self.assertPlayerCount(1)
        self.advance_time_and_run(1)

        # Ensure that Mode env_house_theme_selection is running
        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertGameIsRunning()
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")

        # Hit 'Start' button to add another player
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertEqual(2, self.machine.game.num_players)
        self.assertPlayerCount(2)
        self.advance_time_and_run(1)

        # Player 1 - Ball 1      
        self.assertPlayerNumber(1)
        self.assertBallNumber(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.drain_one_ball()
        self.advance_time_and_run(10)

        # Player 2 - Ball 1
        self.assertPlayerNumber(2)
        self.assertBallNumber(1)

        # Ensure that Mode env_house_theme_selection is running
        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertGameIsRunning()
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")

        # Still two player game?
        self.assertPlayerCount(2)

        # Still Player 2 - Ball 1?
        self.assertPlayerNumber(2)
        self.assertBallNumber(1)

        # Can still add players?
        # Hit 'Start' button twice to add another two players
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertEqual(3, self.machine.game.num_players)
        self.assertPlayerCount(3)
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertEqual(4, self.machine.game.num_players)
        self.assertPlayerCount(4)
        self.advance_time_and_run(1)

        # Still Player 2 - Ball 1
        self.assertPlayerNumber(2)
        self.assertBallNumber(1)
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.drain_one_ball()
        self.advance_time_and_run(10)

         # Player 3 - Ball 1
        self.assertPlayerNumber(3)
        self.assertBallNumber(1)

        # Ensure that Mode env_house_theme_selection is running
        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertGameIsRunning()
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")

        # Still Player 3 - Ball 1?
        self.assertPlayerNumber(3)
        self.assertBallNumber(1)   
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.drain_one_ball()
        self.advance_time_and_run(10)

         # Player 4 - Ball 1
        self.assertPlayerNumber(4)
        self.assertBallNumber(1)

        # Ensure that Mode env_house_theme_selection is running
        self.assertModeNotRunning("attract")
        self.assertModeRunning("game") 
        self.assertGameIsRunning()
        self.assertModeRunning("env_house_theme_selection")
        self.assertModeNotRunning("base")

        # Hit 'Start' button to select a theme
        self.hit_and_release_switch("s_start_button")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("env_house_theme_selection")
        self.assertModeRunning("base")

        # Still Player 4 - Ball 1?
        self.assertPlayerNumber(4)
        self.assertBallNumber(1)    
        self.release_switch_and_run("s_plunger_lane", 11)
        self.assertBallsOnPlayfield(1, playfield='playfield')
        self.drain_one_ball()
        self.advance_time_and_run(10)

        # Loop balls per player
        for b in range(2):
            self.assertBallNumber(b+2)
            for p in range(4):
                self.assertPlayerNumber(p+1)
                self.release_switch_and_run("s_plunger_lane", 11)
                self.assertBallsOnPlayfield(1, playfield='playfield')
                self.drain_one_ball()
                self.advance_time_and_run(10)

        self.assertModeRunning("attract")
        self.assertModeNotRunning("game")
        self.assertGameIsNotRunning()