---
id: SM-20-SYSTEMS
maps: [sm_oceanhouse_1, sm_oceanhouse_2]
---
# SM-20.02 — Системы и постановка

## Граф состояний: Hotel и Therese

| Источник | Явная запись | Статус |
| --- | --- | --- |
| `therese.dlg` ID 231 | `G.Therese_Quest=1; pc.SetQuest("Hotel",1)` | `VERIFIED_STATIC`; достижимость реплики UNVERIFIED |
| `pendant.OnPlayerPickup` и `Level_Finished.OnTrigger` → `oceanhouseQuestComplete()` | `pc.SetQuest("Hotel",2); G.Therese_Quest=2` (`santamonica.py:1465–1467`) | VMF/BSP I/O и PY `VERIFIED_STATIC`; порядок и повтор вызова UNVERIFIED |
| `therese.dlg` ID 521 | `Hotel=3; Release the Spirit=3` | `VERIFIED_STATIC` для DLG, условия перехода и runtime отдельно |
| `therese.dlg` ID 271 | `Hotel=6; Release the Spirit=2` | `VERIFIED_STATIC` для DLG; это альтернативная запись, а не следующая числовая стадия |

`Therese_Quest` и состояния журналов `Hotel`/`Release the Spirit` — разные поля. Python `spirtQuestAssign()` ставит `Release the Spirit=1`, `spirtQuestComplete()` — 3 (`santamonica.py:1461–1472`). В VMF2 `OH_diary.OnPlayerPickup` вызывает `spirtQuestAssign()` в контексте запуска звука `sound_whisper_helpme`, затем ещё один шёпот через 10 секунд и `logic_rattlers` через 12 секунд (L162029–162042). Нужна runtime проверка выполнения встроенного вызова.

## Граф событий: проверенные связи

1. `pendant` (`item_g_ghost_pendant`, VMF2:151552–151558) на подборе вызывает `oceanhouseQuestComplete()` и показывает `Return_Teleport_Trigger` с задержкой 0.5 s.
2. `Return_Teleport_Trigger.OnStartTouch → Level_Finished.Trigger` (VMF2:153726–153735).
3. `Level_Finished.OnTrigger` повторно вызывает `oceanhouseQuestComplete()`, удаляет `Leave_OH_Block`, разблокирует ручку входной двери и удаляет часть haunted entities (VMF2:158729–158750). Выборочные строки сохранены также в установленном BSP entity lump.

Это два возможных статических вызова одной функции; механизм защиты от повтора в показанной функции отсутствует. Без runtime нельзя утверждать, сколько раз изменение журнала реально выполняется.

## Направление и опасности

**Внешний ключ и Plus-сцена.** В UP BSP `Key_Button.OnPressed` выдаёт `item_k_oh_front_key`, меняет стойки ключей, убирает подсветку и запускает `plus_check.Test`. Условие `Patch_Plus == 1` включает `door_trailer.Lock`, меняет `bobcat_before/after`, запускает звук через 1 с, удар через 5 с и shake через 5.1 с. `Unlock` той же двери запланирован через 10 с. `front_door_1_knob` содержит ключ и `difficulty=5`. `OnSkillSuccess` убирает `Key_Button` и `inspect_key`; эту ветку следует сравнить с получением ключа при проверке сцены. `trigger_trigger_changelevel` имеет `StartDisabled=1` и один вызов `Leave_Teleport.ChangeNow` по touch, дверь содержит отдельный вызов по `OnOpen`. Положение створки при `Lock` и порядок показа сцены остаются открытыми. [[SM-20_Ocean_House_01_Spatial]]

| Запуск → цепь | Статическое свидетельство | Неизвестно |
| --- | --- | --- |
| `trigger_ghost` (`trigger_look`) → `logic_ghost_lobby` → `ghost_stand-in.ScriptUnhide` | BSP entity lump; VMF2 именованные связи | Требуемый угол взгляда, частота и видимость в игре |
| `trigger_ghost_basement_1` → `logic_ghost_2` → `ghost_stand-in_2.ScriptUnhide` | BSP entity lump | Позиция игрока и фактический показ |
| `NightStandKey.OnItemRemove` → `logic_ghost_walkway` → `ghost_stand-in_3.ScriptUnhide` | BSP entity lump | Достижимость и визуальная последовательность |
| `Boiler_Event_C.OnTrigger` → `RivetC.ShakeAndFling` → `Boiler_Steam1_Trigger.ScriptUnhide` | BSP entity lump; последний объект `trigger_hurt` | Длительность, урон и обход в игре |
| `OH_diary.OnPlayerPickup` → `sound_whisper_helpme.PlaySound`, delayed `sound_whisper_hescoming2.PlaySound`, `logic_rattlers.Trigger` | VMF2:162029–162042 | Реальное воспроизведение и контроль игрока |

**После рубильника.** В UP BSP `BreakerBox.OnUse` показывает группу `Boiler_Events_Trigger` и вызывает `Boiler_Poltergiest_Relay_ON`. Тот активирует `trigger_elev_to_basement *89`, который начинается с `StartDisabled=1`. При первом входе в объём вызванный relay отправляет `elevator.GotoFloor 2` (позиция Z=−128). У самого триггера есть отдельный выход для удаления через 0,9 с. У лифта `OnReachFloor2` открывает `basementelevb`. Это включение доступно по цепи рубильника, даже если игрок у самого рубильника ещё не сел в кабину.

**Паровые объёмы.** `Boiler_Event_C/F` вызывают `RivetC/F.ShakeAndFling`; только `RivetC/F.OnFling` показывает `Boiler_Steam1/2_Trigger` и включает соответствующие звук и струю. У обоих обычных `trigger_hurt` зафиксированы `StartHidden=1`, `StartDisabled=0`, `damage=1`. Парного выключающего выхода к этим двум целям в entity lump не найдено. У отдельной цепи `trigger_steamevent → plus_logic_steamy` есть `plus_steamgout_hurt.Enable` через 0,2 с и `Disable` через 10 с. Эти задержки взяты от запуска соответствующего relay. Фактическая длительность и урон обычных потоков остаются для игры.

**Вентиляция.** Разрушение `ventdoorb *44` скрывает обычную кабину через `elevator_hide_relay`, показывает два объекта `elev_fall_event_trigger` разных классов (`trigger_look *289` и `trigger_once *292`) и закрывает `elev2`. Оба объекта вызывают `ElevFall_Relay` и через 0,05 с адресуют `Kill` общему имени. Relay двигает отдельную модель `elev_falling`, включает тряску и звук. Кто из двух триггеров сработает первым, зависит от фактического подхода.

VMF2 содержит `SunRoom_Music` с `Music/Stems/Mid_Short cutscene27.wav` (L151535–151548) и `Sound_Of_The_Clifs` с seagull/storm cue (L151565–151600). Наличие файловых ссылок и I/O не устанавливает слышимый микс или точную режиссуру кадра. Источник camera shot и изменение контроля игрока для этих сцен пока не установлен.

## Отношение к Therese DLG

DLG ID 493/496/513/515 проверяют `item_g_ghost_pendant`, удаляют его и содержат Plus-ветки с `item_g_oh_diary`; ID 495 записывает `Hotel=3` и `Release the Spirit=3` при собственной проверке предмета. ID 271 содержит альтернативную запись `Hotel=6`. Эти записи не позволяют без моделирования всех входов DLG и runtime объявить один универсальный исход. Подробные социальные ветки уже рассматриваются в [[../../Characters/SM-13_Asylum_07_Therese_Dialogue|исследовании Therese]].
