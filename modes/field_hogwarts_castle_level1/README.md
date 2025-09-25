# Field - Hogwarts Castle

First time in Hogwarts Castle you get intro about the greatest wizards. (maybe at this point you have to choose a house).<br />
After the intro you get an overview of your progress towards Hogwarts Castle, this will be shown everytime afterwards.<br />

There are four levels and for simplicity, readability and future expansions each level has its own `field_hogwarts_castle_level` mode for either there own purpuse and dependencies.
The four levels modes are;

- Mode `field_hogwarts_castle_level1` - Greatest wizard and witches
- Mode `field_hogwarts_castle_level2` - You know who
- Mode `field_hogwarts_castle_level3` - Dark Magic
- Mode `field_hogwarts_castle_level4` - Horcrux overview

## Mode description

**level 1 - Greatest wizard and witches**

1. Get inside `Hogwarts Castle`.
2. Ball will be **locked** and you get a **new ball**.
3. Get again inside `Hogwarts Castle`.
4. Start 2-ball 'Multiball'

Award: 2-ball multiball or 3 or 4-ball multiball mission mode x.

> [!NOTE]
> **level 1 - Get inside castle.**
> - `Hit` droptarget `hogwarts castle door` in `unlit` state.
>   - Advance shot to `lit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `lit` state.
>   - Advance shot to `open`.
>   - Left drop target down.
> - 'Shoot' ball inside hogwarts castle 
    - lock ball 1
    - show greatest wizard info
  
**level 2 - You know who**

1. Get inside `Hogwarts Castle` (**without** magnet grab and fling support).
2. Ball will **not** be **locked** and will be **returned**.
3. Lock one ball in `chamber of secrets`.
4. Lock one ball in `forbidden forrest`.
5. Get inside `Hogwarts Castle` (**without** magnet grab and fling support) to start a 3-ball multiball.

Award: 3-ball multiball mission mode x.<br />

> [!NOTE]
> **Level 2 - Get inside castle (without magnet grab and fling support - door left open when missed, less points).**<br />
> - `Hit` droptarget `hogwarts castle door` in `unlit` state.
>   - Advance shot to `lit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `lit` state.
>   - Advance shot to `open`.
>   - Left drop target down.
> - `Grap` the ball with `left flipper`.
> - `Fling` the ball with `left flipper` into entrance shot.
>   - When shot is made with magnet fling, adward points.
>   - When shot is missed, left door open until shot is made with flippers.
>   - When shot is made with flippers, adward points butt less.
> - Reset droptarget `hogwarts castle door` shot to `unlit`.
> - Reset drop target.

**level 3 - Dark Magic**<br />

1. Get inside `Hogwarts Castle` (**without** magnet grab and fling support).
2. Ball will **not** be **locked** and will be **returned**.
3. Lock one ball in `pensieve`.
4. Lock one ball in `gringotts bank`.
5. Lock one ball in `ministry of magic`.
6. Get inside `Hogwarts Castle` (**without** magnet grab and fling support) to start a 3-ball multiball.

Award: 4-ball multiball mission mode x.<br />

> [!NOTE]
> **Level 3 - Get inside castle (without magnet grab and fling support - door will be closed when missed, each new try is less points).**<br />

**level 4 - Horcrux overview**<br />

`Horcruxes` overview<br />