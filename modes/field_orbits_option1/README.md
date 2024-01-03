
# Field mode - Orbits option 1

This mode has three possible orbit shots, these are:<br />
- Left long orbit shot<br />
- Center short orbit shot<br />
- Right long orbit shot<br />

> [!NOTE]
> This pinball machine has four possible orbit shots, these are:<br />
> - Left long orbit    - Left lane to right lane (long orbit)<br />
> - Right long orbit   - Right lane to left lane (long orbit)<br />
> - Center short orbit - Center lane to right lane (short orbit)<br />
> - Right short orbit  - Right lane to center lane (short orbit)<br />

## Mode description

Below is a schematic drawings of the orbit lanes and the diverters.<br />
Both diverters shown as "/" and are in DEACTIVE state.<br />
The left diverter is div_forrest and the right diverter is div_castle.<br />

<pre>
| |______________
|/ ____/  ____  |
| |    | |    | |
| |           | |
| |           | |
</pre>

> [!CAUTION]
> `div_forrest` and `div_castle` can't be ACTIVE at the same time.<br />
> This is by design and it's hardware limits.<br />

> [!CAUTION]
> When `div_forrest` is ACTIVATED, `div_castle` MUST BE DEACTIVE because the left orbit lane is now used by `mission_forbidden_forrest` and therefor you can't use the left long and right long orbits.<br />

<pre>
IMPORTANT - SO THIS OPTION BELOW IS PROHIBITED BY HARDWARE LIMITS AND DESIGN.
IMPORTANT - Left diverter shown as "|" and the right diverter as "__".
IMPORTANT -  | |_____________ 
IMPORTANT -  | |___________  |
IMPORTANT -  | |    | |    | |
IMPORTANT -  | |           | |
IMPORTANT -  | |           | |
</pre>

> [!TIP]
> DEPENDICE - Left long orbit     - div_forrest must be DEACTIVE and div_castle has to be ACTIVE
> DEPENDICE - Right long orbit    - div_forrest must be DEACTIVE and div_castle has to be ACTIVE
> DEPENDICE - Center short orbit  - div_forrest can be ACTIVE and div_castle has to be DEACTIVE
> DEPENDICE - Right short orbit   - div_forrest can be ACTIVE and div_castle has to be DEACTIVE

For simplicity, readability and future expansions there are multiple field_orbits_option modes for either there own purpuse and dependencies.
  - field_orbits_option1 - Default mode                         - div_forrest DEACTIVE and div_castle will be ACTIVATED from left and right orbit lane
  - field_orbits_option2 - Advanced mode, Gringotts Bank mode   - div_forrest DEACTIVE and div_castle will be only ACTIVATED from left orbit lane
  - field_orbits_option3 - Forbidden Forrest mode               - div_forrest ACTIVE thus div_castle MUST BE DEACTIVE - IMPORTANT -

Mode field_orbits_option1 - Default mode (Right long) - THIS MODE
  - Left long orbit    - sq_shot_orbit_left_long_opt1
  - Center short orbit - sq_shot_orbit_center_short_opt1
  - Right long orbit   - sq_shot_orbit_right_long_opt1

# Other Orbit modes

Mode field_orbits_option2 - Advanced mode, Gringotts Bank mode (Right short)
  - Left long orbit    - sq_shot_orbit_left_long_opt2
  - Center short orbit - sq_shot_orbit_center_short_opt2
  - Right short orbit  - sq_shot_orbit_right_short_opt2

Mode field_orbits_option3 - Forbidden forrest mode (Only short, no long)
  - Center short orbit - sq_shot_orbit_center_short_opt3
  - Right short orbit  - sq_shot_orbit_right_short_opt3


