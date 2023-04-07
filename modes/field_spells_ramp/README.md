
# Field mode - Spells Ramp

This mode will let you learn spells. When you complete the last qualifying shot in time you get a bonus

## Setup

## --------------------
## | Mode Explanation |
## --------------------

# - Step 1 - Make 10 right Ramp Shots to complete qualify counter and advance the Spells Light to lit.
# - Step 2 - Make another Right Ramp Shot to advance the Spells Light to active, advance the Right Ramp Light to lit and 
#            start a qualifying timer.
# - Step 3 - Make another Right Ramp Shot before the timer ends to complete the Spells Light qualification, 
#            reset both Light shots to unlit, advance the state_machine to next level and collect a bonus.
# - Step X - When the timer ends - Reset both Light shots to unlit, reset counter, reset timer and advance state_machine to
#            next level without a bonus.
# - Step X - When a ball drains when Spells Light is unlit - Persist counter state_value.
# - Step X - When a ball drains when Spells Light is lit - Persist Spells Light shot_state to lit.
# - Step X - When a ball drains when Spells Light is active - Reset both Light shots to unlit, reset counter, reset timer and
#            advance state_machine to next level without a bonus.

## Achievements
