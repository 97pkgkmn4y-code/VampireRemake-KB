---
id: SM-28-SYSTEMS
map: sm_junkyard_1
---
# Junkyard — системы и Serial

## Сущности и постановка

UP BSP entity lump: `worldspawn.levelscript=santamonica`; 530 entities, включая шесть `npc_VVampire` (основной `Killer` и пять постановочных экземпляров), `Night Watchman` (`npc_BaseVampAI`), `watchman` (`npc_VLasombra`) и `plus_dog` (`npc_VDog`). Основной Killer имеет `dialogname=dlg/Santa Monica/Killer.dlg`; Night Watchman ссылается на `Santa Monica/Nightwatchman.dlg`, отдельный loose DLG в установленном каталоге UP не найден — доступность через другие источники не установлена. Наличие шаблонов и Plus-имён не доказывает одновременное появление NPC.

| Выход в установленном BSP | Непосредственная связь |
|---|---|
| `first_killer_trigger.OnStartTouch` | `flee_into_junkyard.BeginSequence`; её `OnBeginSequence → first_car_impact.Impact` |
| `second_killer_trigger.OnStartTouch` | `first_killer.Kill`, `second_killer.ScriptUnhide`, `second_killer_init.BeginSequence` с 0.2 с |
| `third_killer_trigger.OnStartTouch` | `second_killer.Kill`, `third_killer.ScriptUnhide`, `throw_third_car.BeginSequence` |
| `fourth_killer_trigger.OnStartTouch` | `third_killer.Kill`, `fourth_killer.ScriptUnhide`, `tip_car_stack.BeginSequence`; `car_stack_tipper.OnOpen` запускает конвертацию, взрыв и impact damage |
| `fifth_killer_trigger.OnStartTouch` | `fourth_killer.Kill`, `fifth_killer.ScriptUnhide` |
| `conflagration.OnStartTouch` | `killer_start_fire.BeginSequence`; её `OnBeginSequence → fire_relay.Trigger` |
| `kindling_ground_trigger.OnStartTouch` | `kindling_lands_relay.Trigger → explosion_relay.Trigger` через 3 с; реле включает огонь и преобразует/ударяет car tunnel |
| `real_killer_trigger.OnStartTouch` | Направляет `ScriptUnhide` к `Killer_double` и `Killer`; entity с именем `Killer_double` в установленном entity lump не найдена, динамическое создание и результат UNVERIFIED |
| `killer_confront.OnStartTouch` | `controller.CreateControllerNPC`, снятие дисциплин и `player_to_killer.BeginSequence`; `player_to_killer.OnEndSequence → Killer.StartPlayerDialog` |
| `Killer.OnDialogEnd` / `OnDeath` | Вызывают соответственно `killerHostileCheck()` / `killerDeath()`; при смерти дополнительно выключается огненная стена |

Это прямые выходы entity lump, не доказательство обязательного последовательного прохождения. Некоторые `scripted_sequence` удаляют соответствующий постановочный экземпляр; не считать каждую entity отдельным действующим персонажем.

## Python и выходы

`santamonica.py:1428–1437`: `killerDeath()` при `GetQuestState("Serial") != 9` вызывает `ChangeMasqueradeLevel(-1)` и `SetQuest("Serial",8)`; при наличии визитки планирует её удаление через секунду и запускает `player_leave_relay`. Последний через 5 с выполняет `JunkyardTeleport2.ScriptUnhide`, блокирует `jnkshkb`, запускает fade и через 3 с удаляет `Killer`. Это не прямой вызов `ChangeNow`.

`santamonica.py:1440–1453`: после диалога `killerHostileCheck()` при истинном `G.Killer_Hostile` запускает fade, меняет модель, пишет `G.Killer_Attacks=1`, запускает `killer_attack`; иначе при наличии планирует удаление визитки и запускает выходное реле. `killer_attack.OnBeginSequence` включает огненную стену, а `OnEndSequence` задаёт враждебность и дисциплины. `killerTransform()` L1456–1458 отдельно меняет модель; прямой вызов этой функции в проверенной локальной I/O-цепи не установлен.

`santamonica.py:2032–2035` содержит `junkyardOpen()`: при `G.Killer_Lucky==1` вызывает `Unlock` у `junkyardgate`; сама функция не устанавливает факт вызова или доступности входа. `vamputil.py:3584–3586` содержит `sm_junkyard_1_patch()` с планированием `hunterStats()`, но точка вызова и последствия здесь не установлены. См. также [[../diner1/SM-15_Diner_02_Systems|Diner]] о раннем появлении Killer и [[../coffee1/SM-17_Coffee_00_Index|Scott laptop]] о текстовом упоминании Junkyard; текст не доказывает посещение.

## DLG и стадии Serial

Ниже — буквальные поля `killer.dlg`; `Humanity 5` и `Humanity -5` оставлены в синтаксисе DLG, поскольку правила интерпретации и достижимость не проверены. Все перечисленные конечные строки имеют next `0`.

| DLG ID | Условие / переход | Действие |
|---|---|---|
| 214 / 215 | `Killer_Lucky==0 && npc.times_talked>1 → 193`; `Killer_Lucky==1 && Killer_Freed==0 → 11` | Стартовые условия; приоритет между допустимыми строками неизвестен |
| 35,46,56,119,127,133–136,149–150,154–155 | Разные условия Humanity, клана, `Bertram_Caitiff` и Plus | `G.Killer_Hostile=1`; в Plus строки 135/136 дополнительно `HumanityAdd(-1)` |
| 137 / 138 | `Humanity 5` / `Humanity -5` | `G.Killer_Freed=1; SetQuest("Serial",10)` |
| 152 / 153 | `Humanity 5` / `Humanity -5` | `G.Killer_Freed=1; SetQuest("Serial",9)` |
| 156 | `Humanity 5 & G.Patch_Plus==1` | `Killer_Nines=1; Killer_Freed=1; Serial=9` |

`quests_santamonica.txt:527–551` связывает журнальные ID 7 с визиткой, 8 с убийством, 9 и 10 с разными исходами разговора. Это тексты/настройки стадий, не доказательство их последовательности. Влияние `Killer_Nines` на другие карты здесь не прослежено. Доступность веток, порядок DLG и фактические последствия не проверены в игре.
