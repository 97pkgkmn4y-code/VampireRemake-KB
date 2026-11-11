# SM-18 — системы, диалоги и состояния

## Цепь I/O

| Источник | Условие/выход | Действие |
|---|---|---|
| `logic_auto` ID 1133 | [VMF] OnMapLoad | `controller.RemoveDisciplinesNow`; через 2 c `Stan_Gimble.StartPlayerDialog`. Это заданное I/O, а не наблюдаемая гарантия разговора. |
| `Stan_Gimble` ID 994 | [VMF] OnDialogEnd, L16815 | `controller.CreateControllerNPC`; `gimble_leave_check.test`. |
| `gimble_leave_check` ID 1169 | [VMF] `python_script=G.Gimble_Vandal == 0`, L23745–49 | True → `gimble_leave`; False → `gimble_leave2`, через 4 c удалить controller, отпереть `gimbledoor3`, `Stan_Gimble.Kill`. |
| `gimble_leave` ID 63609 / `gimble_leave_end` ID 995 | [VMF] конец последовательности L43648, L16840 | Затем `gimble_teleport.Teleport` к `(-1252.53,-456.944,-380)`. |
| `Stan_Gimble` ID 994 | [VMF] OnDeath L16816–17 | `gimble_dead_relay.Trigger` и Python `gimbleDeath()`. |
| `gimble_dead_relay` ID 1139 | [VMF] OnTrigger L23164–72 | Отпереть `gimbledoor1/2`, разрешить `Carson_free_relay`, снять дисциплины, fade, телепортировать игрока к `(-858.12,-459.276,-380)`, создать controller, запустить `player_release_carson`, камеру. |
| `player_release_carson` ID 1142 → `_2` ID 1143 | [VMF] L23229, L23252–53 | При начале `carson_switch.Deactivate` через 0.5 c; по завершении второго фрагмента `Carson.StartPlayerDialog` и удалить controller. |
| `carson_switch` ID 1138 | [VMF] OnDeactivate L23145–46 | `celldoor4.Unlock`, затем `Open`. |
| `Carson` ID 1041 | [VMF] OnDialogEnd L17939, L17942 | `carson_free_relay.Trigger`, `gimble_attack_check.test`. |
| `gimble_attack_check` ID 1168 | [VMF] `python_script=G.Gimble_Vandal == 0`, L23726–28 | True → `gimble_attack_relay`; False → `Stan_Gimble.Kill` и явный `gimble_dead_relay.Trigger`. |
| `gimble_attack_relay` ID 1045 | [VMF] L18079–82 | Остановить разговор Stan, отпереть `gimbledoor3`, начать `gimble_attack`, установить отношение к игроку `D_HT 5`. |
| `carson_free_relay` ID 1144 | [VMF] L23271–75 | Disable `Carson prot brush`, camera/controller, `carson_free_sequence` и `player_release_carson_3`. Конец `carson_free_sequence` ID 1146 удаляет controller, завершает камеру и `Carson.Kill` (L23317–19). |
| `Carson` ID 1041 | [VMF] OnDeath L17940–41 | Python `carsonDeath()` и `gimble_dead_relay.Kill`. |

[PY] `santamonica.py:411–423`: `carsonDeath()` задаёт `Arthur Knox=8`, отпирает `carson_switch`, удаляет `Carson prot brush` при наличии; `gimbleDeath()` задаёт `Arthur Knox=3`, `G.Gimble_Dead=1`. Движковое `Kill` сущности и `OnDeath` различаются: вызов последнего для scripted `Kill` без наблюдения не гарантирован.

## DLG: Stan Gimble

- [DLG] Телефон: ID 1 задаёт `G.Gimble_Phone=1`; IDs 2/3 различают `G.Patch_Plus=0/1`, обе ведут к ID 11. IDs 12→51→52→61 (предложение моделирования) задают `G.Gimble_Model=1`, `G.Gimble_Buzzer=1`. IDs 13→21→32→41 (расспрос) задают `G.Gimble_Questions=1`, `G.Gimble_Buzzer=1`. ID 71 задаёт `Arthur Knox=6`.
- [DLG] Начальные условия подвала IDs 282–285: Nosferatu с `G.Gimble_Phone=1` → 81; `G.Gimble_Model=1` → 91; `G.Gimble_Questions=1` → 96; `npc.times_talked==1` → 211. Приоритет движка между одновременно истинными условиями не подтверждён.
- [DLG] В подвале ID 101 предлагает ID 102→111 при `G.Gimble_Model=1` (ID 111 задаёт `G.Gimble_Leave=1`), ID 103→171 при `G.Gimble_Questions=1`; расспрос ID 171→181→191→201 ведёт к ожиданию. ID 202→251 только при `G.Gimble_Vandal=0`, ID 251 задаёт `G.Gimble_Leave=1`.
- [DLG] Plus ветка: ID 162 или 193 доступны при `Persuasion 5`, `G.Vandal_Quest=1`, `G.Patch_Plus=1`, переходят к 255. IDs 256/257 при Humanity ≥4 / <4 задают `G.Vandal_Quest=3`, `G.Gimble_Vandal=1`, `Danielle=7`; ID 256 дополнительно уменьшает Humanity на 1 и ставит `G.Gimble_Humanity=1`. Оба → 201, где ID 203 завершает разговор при `G.Gimble_Vandal=1`. Соседство строк без `next` не использовано как переход.

## DLG: Carson

- [DLG] Начальные условия IDs 112–114: `G.Carson_Rescued=1` → 71; Nosferatu и `G.Gimble_Dead=1` → 61; `G.Gimble_Dead=1` → 21. Начало ID 1→2→11; ответы ID 12/13/14 при разных состояниях `G.Gimble_Vandal` ведут к 0. ID 13 при `G.Gimble_Humanity=1` возвращает Humanity +1, ставит `G.Gimble_Dead=1`, `Arthur Knox=3`; ID 14 ставит последние два состояния без Humanity.
- [DLG] ID 21 задаёт `G.Carson_Rescued=1`; Nosferatu ID 61 делает то же. Цепь 22→31→32→41→42→51 сообщает об утрате пальца и ставит `G.Arthur_Knox=3`. Ветка Malkavian 23→36→37→41. Завершение 71→72 возвращает 0. DLG факт спасения не доказывает фактическое завершение scripted sequence.
