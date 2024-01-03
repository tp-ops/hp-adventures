
# Field mode - Orbits option 1

This mode will let you learn spells. When you complete the last qualifying shot in time you get a bonus


## Mode description

- **Step 1:** Make 10 right Ramp Shots to complete qualify counter and advance the Spells Light to lit.
- **Step 2:** Make another Right Ramp Shot to advance the Spells Light to active, advance the Right Ramp Light to lit and start a qualifying timer.
- **Step 2:** Make another Right Ramp Shot before the timer ends to complete the Spells Light qualification, reset both Light shots to unlit, advance the state_machine to next level and collect a bonus.
- **Step X:** When the timer ends - Reset both Light shots to unlit, reset counter, reset timer and advance state_machine to next level without a bonus.
- **Step X:** When a ball drains when Spells Light is unlit - Persist counter state_value.
- **Step X:** When a ball drains when Spells Light is lit - Persist Spells Light shot_state to lit.
- **Step X:** When a ball drains when Spells Light is active - Reset both Light shots to unlit, reset counter, reset timer and advance state_machine to next level without a bonus.


## Badges

This pinball machine has for possible orbits, these are;
  - Left long orbit    - Left lane to right lane (long orbit)
  - Right long orbit   - Right lane to left lane (long orbit)
  - Center short orbit - Center lane to right lane (short orbit)
  - Right short orbit  - Right lane to center lane (short orbit)

Below is a schematic drawings of the orbit lanes and the diverters.
Both diverters shown as "/" and are in DEACTIVE state
The left diverter is div_forrest and the right diverter is div_castle.
<pre>
| |______________
|/ ____/  ____  |
| |    | |    | |
| |           | |
| |           | |
</pre>

> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.


IMPORTANT - div_forrest and div_castle CAN'T BE ACTIVE AT THE SAME TIME, THIS IS BY HARDWARE LIMITS AND DESIGN.
IMPORTANT - When div_forrest is ACTIVATED, div_castle MUST BE DEACTIVE because the left orbit lane is now used by mission_forbidden_forrest and therefor you can't use the left long and right long orbits.
<pre>
IMPORTANT - SO THIS OPTION BELOW IS PROHIBITED BY HARDWARE LIMITS AND DESIGN.
IMPORTANT - Left diverter shown as "|" and the right diverter as "__".
IMPORTANT -  | |_____________ 
IMPORTANT -  | |___________  |
IMPORTANT -  | |    | |    | |
IMPORTANT -  | |           | |
IMPORTANT -  | |           | |
</pre>
DEPENDICE - Left long orbit     - div_forrest must be DEACTIVE and div_castle has to be ACTIVE
DEPENDICE - Right long orbit    - div_forrest must be DEACTIVE and div_castle has to be ACTIVE
DEPENDICE - Center short orbit  - div_forrest can be ACTIVE and div_castle has to be DEACTIVE
DEPENDICE - Right short orbit   - div_forrest can be ACTIVE and div_castle has to be DEACTIVE

For simplicity, readability and future expansions there are multiple field_orbits_option modes for either there own purpuse and dependencies.
  - field_orbits_option1 - Default mode                         - div_forrest DEACTIVE and div_castle will be ACTIVATED from left and right orbit lane
  - field_orbits_option2 - Advanced mode, Gringotts Bank mode   - div_forrest DEACTIVE and div_castle will be only ACTIVATED from left orbit lane
  - field_orbits_option3 - Forbidden Forrest mode               - div_forrest ACTIVE thus div_castle MUST BE DEACTIVE - IMPORTANT -

Mode field_orbits_option1 - Default mode (Right long) - THIS MODE
  - Left long orbit    - sq_shot_orbit_left_long_opt1
  - Center short orbit - sq_shot_orbit_center_short_opt1
  - Right long orbit   - sq_shot_orbit_right_long_opt1

Mode field_orbits_option2 - Advanced mode, Gringotts Bank mode (Right short)
  - Left long orbit    - sq_shot_orbit_left_long_opt2
  - Center short orbit - sq_shot_orbit_center_short_opt2
  - Right short orbit  - sq_shot_orbit_right_short_opt2

Mode field_orbits_option3 - Forbidden forrest mode (Only short, no long)
  - Center short orbit - sq_shot_orbit_center_short_opt3
  - Right short orbit  - sq_shot_orbit_right_short_opt3


