
# Field mode - House Cup                                                         

This mode represents the four houses and the yearly house cup competition.
Complete all four house mission modes and a mini wizird mode will start.

## Setup
Used four shots based on captiva_ball core shot. One shot profile is available for each of the four shots. This shot profile, sp_house_cup, has four states.
Each time this mode start the next shot advance to lit. Another way to advance the next shot to lit is trough to event master_of_death, see that mode for more info on that.
To track this a counter lb_house_cup_to_lit_count is used.
When you hit core shot captive_ball all lit shots advance to active and will start mission modes. When the ball drains all active shots will advance to 
played and the mission modes will also stop, whether completed or not.

## Achievements
