---
id: SM-13-ENTITIES
map: sm_asylum_1
status: extracted from source VMF
---
# SM-13.02 — Сущности и интерактивность

## 1. Структура файла

[F] `542` entity blocks, `48` разных `classname`; `368` world solids и суммарно `982` solid blocks, если учитывать `entity` solids. Детали и объекты не следует приравнивать по количеству к отдельным «комнатам»: один лифт, дверь или световой декор могут состоять из множества сущностей.

### Счётчик классов [F]

| classname | count | значение для анализа |
|---|---:|---|
| `prop_static` | 103 | мебель, освещение, декор, сценические инструменты |
| `func_detail` | 57 | геометрия деталей, не самостоятельные комнаты |
| `info_node` | 48 | узлы потенциальной NPC-навигации, не прямое свидетельство проходимости игрока |
| `light_spot` | 47 | направленный свет |
| `env_sprite` | 37 | световые/декоративные спрайты |
| `intersting_place` | 34 | точки поведения NPC/игрока; написание в исходнике именно `intersting_place` |
| `light` | 25 | локальный свет |
| `prop_dynamic` | 22 | динамический реквизит |
| `func_door` | 16 | части лифтовых дверей |
| `npc_VPedestrian` | 16 | посетители, танцоры и дополнительные NPC |
| `infodecal` | 14 | декали |
| `env_cubemap` | 14 | отражения |
| `ambient_generic` | 11 | музыка, диалоги, звуки лифта, полиция |
| `func_brush` | 9 | управление браш-геометрией |
| `logic_relay` | 8 | последовательности логики |
| `scripted_sequence` | 6 | кинематические/поведенческие сцены |
| `func_illusionary` | 6 | особая геометрия без обычной твердотельности, точный режим движка требует проверки |
| `trigger_multiple` | 5 | повторяемые зоны-триггеры |
| `trigger_once` | 5 | однократные зоны-триггеры |
| `logic_timer` | 5 | световые таймеры и idle |
| `env_fade` | 5 | затемнения, в том числе цепочка Jeanette |
| `func_door_rotating` | 4 | вход и два частных дверных объекта |
| `prop_button` | 4 | лифт |
| `logic_auto` | 3 | события загрузки |
| `npc_VVampire` | 3 | Jeanette, Therese, Tourette |
| `ambient_soundscheme` | 3 | группы звуков |
| `intersting_place_conversation` | 3 | точки диалогового поведения |
| `point_teleport` | 2 | перенос Jeanette |
| `prop_hacking` | 2 | терминалы Jeanette/Therese |
| `camera_cinematic` | 2 | камеры Jeanette/Tourette |
| `events_player` | 2 | player callbacks |
| `point_target` | 2 | вспомогательные цели |
| `env_particle` | 2 | частицы |
| `math_counter` | 2 | счета лифтовых дверей |
| `params_particle` | 2 | параметры частиц |
| `func_elevator` | 1 | лифт |
| `info_landmark` | 1 | возвращение в hub |
| `trigger_changelevel` | 1 | смена карты |
| `info_player_start` | 1 | старт |
| `npc_VHuman` | 1 | Cal |
| `npc_VDialogPedestrian` | 1 | Chunk |
| `item_g_ring_gold` | 1 | Gold Ring |
| `inspection_node` | 1 | подсказка к кольцу |
| `env_shake` | 1 | вибрация лифта |
| `prop_sign` | 1 | записка Voerman |
| `prop_dynamic_ornament` | 1 | оружие Tourette |
| `trigger_electric_bugaloo` | 1 | танец игрока |
| `events_world` | 1 | мировые события |

## 2. NPC и их потенциальные роли [F]

| targetname | classname | примечания |
|---|---|---|
| `Cal` | `npc_VHuman` | бармен, `dialogname=dlg/Santa Monica/Cal.dlg`, `OnDialogBegin → jeanetteGoesUp()`; L38748 |
| `Jeanette` | `npc_VVampire` | `dialogname=dlg/Santa Monica/Jeanette.dlg`, сцены лифта и разговоров; L38858 |
| `Therese` | `npc_VVampire` | `dialogname=dlg/Santa Monica/Therese.dlg`; L38923 |
| `Tourette` | `npc_VVampire` | `dialogname=dlg/Santa Monica/Tourette.dlg`, `item_w_thirtyeight`, особая камера; L40080 |
| `Doll1` | `npc_VPedestrian` | `OnDeath → G.Doll1_Dead = 1`; L37456 |
| `Danielle` | `npc_VPedestrian` | `OnDeath → G.Danielle_Dead = 1`, `OnDialogEnd → danielleDialog()`; L38317 |
| `Chunk` | `npc_VDialogPedestrian` | `StartHidden=1`; L40167 |
| `Knox_basic` | `npc_VPedestrian` | одна позиция Knox в нижнем клубе; L42549 |
| `Knox_plus` | `npc_VPedestrian` | альтернативная позиция Knox на балконе; L46495 |

**Не трактовать как одновременное количество живых NPC.** Даже `Jeanette`, `Therese` и `Tourette` одновременно описаны в исходнике как сущности, однако управление их активностью уходит в скрипты. `plus_raver` и `basic_raver`, `Knox_basic` и `Knox_plus` требуют определения версионных условий.

В VMF есть два `point_teleport`, `bring_Jeanette_down` (`−904.223,420.837,−280.691`) и `bring_Jeanette_up` (`−823.676,412,−14.894`): наличие именно двух точек подтверждает сценарное перемещение между высотами; **не подтверждает, что игрок видит оба перехода**.

## 3. Объекты исследования, инвентаря и взаимодействия [F]

- `jeanette_laptop` (`prop_hacking`, L41130): `difficulty=4`, `hack_file=vdata/HackTerminals/jeanette_laptop.txt`, origin `−930.787 255.972 13.5879`.
- `therese_pc` (`prop_hacking`, L41159): `difficulty=4`, `hack_file=vdata/HackTerminals/therese_pc.txt`, origin `−760.568 600.732 20`.
- `wedding_ring` (`item_g_ring_gold`, L41105): origin `−1016 744 −8`; `inspection_node` присоединён к `wedding_ring` (L41117).
- `voerman_note` (`prop_sign`, L41398): origin `−1061.77 743.168 21.909`, `OnReadBegin → murderPaperRead()`.

**Граница:** наличие `hack_file` не раскрывает содержимое компьютера; `difficulty=4` не позволяет без игровых правил делать вывод о фактическом пороге по навыку и наградах.

## 4. Музыка, осветительная сцена и переходы [F]

- Музыкальный источник `targetname=music`: `Music/Licenced/05. Chiasm - Isolated.mp3` (`ambient_generic`, L39892).
- Таймеры `blue_timer`, `red_timer`, `green_timer`, `yellow_timer`: `UseRandomTime=1`, bounds `1…5`, `OnTimerLow → *_stage_light TurnOn`, `OnTimerHigh → *_stage_light TurnOff` (L39762–L39825).
- `sound_default` и `sound_override_1` — два `ambient_soundscheme` (L39317, L39330), между которыми управляют три `trigger_multiple` возле верхней части лифта.
- `fade_in_hall` (`L39013`): `sound_default FadeIn 3`, музыка `Volume 6`.
- `fade_out_all` (`L39114`): обе схемы `FadeOut 5`, музыка `Volume 4`.
- `fade_in_office` (`L39216`): `sound_override_1 FadeIn 3`, музыка `Volume 2`.
- Дополнительные `trigger_multiple` регулируют громкость до `1` и `8` (L42205, L42304).

**Интерпретация [I]:** звучание клуба не просто «включено на всю карту»: через пространственные trigger volumes создаются переходы между музыкальной, переходной и частной зонами. Но точные уровни громкости и их интерпретация движком отдельно не проверены.

## 5. Интерактивный танец игрока [F]

`trigger_electric_bugaloo targetname=player_dance_trigger` (L42686) реализует:

| Event | Target action |
|---|---|
| `OnUseBegin` | `dance_spot Disable`, `dance_spot_player Enable`, `G.No_Idle = 1` |
| `OnUseEnd` | `dance_spot_player Disable`, `dance_spot Enable`, `G.No_Idle = 0` |

**[I]** Танцевальные позиции NPC и игрока исключают одновременное использование одних и тех же мест; дополняет клуб как социальную интерактивную площадку. **[?]** Точная animation/state machine пока неизвестна.

## 6. Полиция / внешние реакции [F]

- `events_world targetname=world` (L46650) содержит `OnCopsOutside → cops_relay.Trigger`.
- `cops_relay` (L40973) включает `cops_arrive`, а также отсроченные `cops_yell` (9 секунд) и `cops_outside FadeIn` (9 секунд).
- Условия срабатывания `OnCopsOutside` **не раскрыты** в VMF; они зависят от глобального игрового события.
