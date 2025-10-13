# Field mode - Hogwarts Castle

## Mode Description
First time in Hogwarts Castle you get intro about the greatest wizards. (maybe at this point you have to choose a house).<br />
After the intro you get an overview of your progress towards Hogwarts Castle, this will be shown everytime afterwards.<br />

There are four levels and for simplicity, readability and future expansions each level has its own `field_hogwarts_castle_level` mode for either there own purpuse and dependencies.
The four levels modes are;

- Mode `field_hogwarts_castle_level1` - Greatest wizard and witches (This mode)
- Mode `field_hogwarts_castle_level2` - You know who
- Mode `field_hogwarts_castle_level3` - Dark Magic
- Mode `field_hogwarts_castle_level4` - Horcrux overview

## Playfield position
Hogwarts Castle is a combination of the 1-bank droptarget at the top of the playfield and the sinkhole behind the droptarget.<br />

## Detailed description

#### Level 1 - Greatest wizard and witches

1. Get inside `Hogwarts Castle`.
2. Ball will be **locked** and you get a **new ball**.
3. Get inside `Hogwarts Castle`.
4. Start 2-ball 'Multiball'.

Award: 2-ball multiball.

> [!NOTE] **Level 1 - Get inside `Hogwarts Castle`.**
> - `Hit` droptarget `hogwarts castle door` in `unlit` state. 
>   - Shot advanced to `lit`.
>   - Drop target resets.
> - `Hit` droptarget `hogwarts castle door` in `lit` state.
>   - Shot advanced to `open`.
>   - Drop target stays down (open).
> - 'Shoot' ball inside hogwarts castle 
>   - Shot restarts
>   - Drop target resets
  
#### Level 2 - You know who

1. Get inside `Hogwarts Castle`.
2. Ball will be **locked** and you get a **new ball**.
3. Get inside `Hogwarts Castle`.
4. Ball will be **locked** and you get a **new ball**.
5. Get inside `Hogwarts Castle`.
6. Ball will **not** be **locked** and will be **returned**.
7. Lock one ball in `chamber of secrets`.
8. Start a 3-ball multiball.

Award: 3-ball multiball.

> [!NOTE] **Level 2 - Get inside `Hogwarts Castle`.**
> - `Hit` droptarget `hogwarts castle door` in `first_unlit` state.
>   - Advance shot to `last_unlit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `last_unlit` state.
>   - Advance shot to `first_lit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `first_lit` state.
>   - Advance shot to `last_lit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `last_lit` state.
>   - Advance shot to `open`.
>   - Drop target stays down (open).
> - 'Shoot' ball inside hogwarts castle 
>   - Shot restarts
>   - Drop target resets

#### Level 3 - Dark Magic

1. Get inside `Hogwarts Castle`.
2. Ball will be **locked** and you get a **new ball**.
3. Get inside `Hogwarts Castle`.
4. Ball will be **locked** and you get a **new ball**.
5. Get inside `Hogwarts Castle`. (Now open for x seconds only)
6. Ball will **not** be **locked** and will be **returned**.
7. Lock one ball in `Forbidden Forrest`.
8. Start a 3-ball multiball.

Award: 3-ball multiball.

> [!NOTE] **Level 3 - Get inside `Hogwarts Castle`.**
> - `Hit` droptarget `hogwarts castle door` in `first_unlit` state.
>   - Advance shot to `last_unlit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `last_unlit` state.
>   - Advance shot to `first_lit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `first_lit` state.
>   - Advance shot to `last_lit`.
>   - Reset drop target.
> - `Hit` droptarget `hogwarts castle door` in `last_lit` state.
>   - Advance shot to `open`.
>   - Drop target stays down (open for x seconds only).
> - 'Shoot' ball inside hogwarts castle 
>   - Shot restarts
>   - Drop target resets

#### Level 4 - Horcrux overview

`Horcruxes` overview