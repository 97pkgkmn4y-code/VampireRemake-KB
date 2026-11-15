---
id: SM-27
map: sm_bailbonds_1
reference: Unofficial Patch Plus 12.0
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-27 — Kilpatrick's Bail Bonds

**Роль.** Интерьер Arthur и терминалов для цепей [[../../Quests/Arthur's_Introduction|Arthur]], [[../../Quests/Bail_Hustler_Quest|Bail Hustler]], [[../../Quests/Bail_Jumper_Quest|Bail Jumper]] и [[../../Quests/Knox_Quest|Knox]]. Диалоговые ветки уже разобраны там; этот паспорт фиксирует карту, I/O и последствия смерти. Установленный UP BSP имеет 74 entities.

## Пространство, переход, участники

`bailbondsdoor.OnFullyOpen → BailBondsTeleport1.ChangeNow`; переход ведёт в `sm_hub_1` через landmark `bailbonds1` (BSP entity lump). Вход из Hub указан в [[../../Space/Transitions|реестре]]. VMF/BSP содержат `Arthur` (`npc_VDialogPedestrian`, `dlg/Santa Monica/Arthur.dlg`) и скрытого `plus_Arthur`. Наличие двух entities не означает двух одновременно видимых Arthur. `logic_auto.OnMapLoad` вызывает `unhidePlus()` и через 1.1 s запускает `plus_Arthur_sit.BeginSequence`; последовательность прячет обычного Arthur, вызывает `arthurPhones()`, позже убирает `plus_Arthur` и показывает обычного Arthur. `vamputil.py:1065–1072` проигрывает одну из двух аудиореплик и ставит `G.Arthur_Phoned=1` при первом вызове. Фактический показ, камера и звук `RUNTIME PENDING`.

## Терминалы и квестовые последствия

- BSP содержит два `prop_hacking`: обычный с `vdata/HackTerminals/Krime_computer.txt` и скрытый `plus_computer` с `vdata/HackTerminals/kilpatricks_computer.txt`. В Plus-терминале есть `email_username=Arthur`, `email_password=freedom`, меню Bonds с `password=money`. Это данные исходного файла, а не подтверждение доступности меню в игре.
- Krimeputer содержит две версии записи Virgil Crumb с `dependency=G.Knox_Quest>=5` и `<5`; одна вызывает `virgilViewed()`. Это пример условного терминального содержимого, связанного с Knox, но выполнение функции при выборе строки ещё не проверено.
- `Arthur.OnDeath → kilpatrickDeath()` (BSP). `santamonica.py:391–399`: если журнал `Arthur Knox` не 0 и не 5, ставит 7; если `Bail Jumper` не 0/3/4, ставит 5. Это **состояния журнала**, а не прямые записи в `G.Knox_Quest`/`G.Arthur_BJ`. Достижимость убийства Arthur и других последствий не установлена.

**Пространство и поведение после постановки.** По UP BSP от дверного порога `(2912,949)` до позиции Arthur `(3080,900)` и обоих терминалов выборочные грани 297, 293 и 298 подтверждают уровень Z=-320. Krimeputer расположен у `(3299.8,930.16,-283.779)`, `plus_computer` рядом с постановочной копией у `(3050.06,889.585,-280.3)`. По окончании `plus_Arthur_sit` через 7 c удаляются копия и её стул, раскрываются Arthur и `chair`; через 7.5 c включается `Arthur.UseInteresting(1)`. Отдельный вход `plus_Arthur.OnDamaged` запускает `arthurPhones()`, отмену последовательности через 10 с и замену копии через 1 с. `intersting_place` с именами `table`/ `computer` по `OnNPCArrived` переключают доступность следующей точки. `plus_computer.OnUseBegin/End` выключает/включает интерес к точке `computer`; движок должен разрешить совпадение имён у сущностей разных классов. В терминале Virgil только запись `Knox_Quest>=5` вызывает `virgilViewed()`, подготавливая морг и ключ Foxy Boxes (см. [[../vamparena/SM-30_Foxy_Boxes_Passport|SM-30]]).

## Источники и ограничения

| Источник от корня установленной игры | SHA-256 |
| --- | --- |
| `SDKContent/MapSrc/up sources/sm_bailbonds_1_d.vmf` | `5e0fd8adfc1bab9c466184254f37e0444261d293d24baf50d71421a832197250` |
| `Unofficial_Patch/maps/sm_bailbonds_1.bsp` | `2ea16c217cb418f6f84e2e5100b51604f5a2dd0bcd567e4a76b6ca62b07f71b7` |
| `Unofficial_Patch/vdata/HackTerminals/Krime_computer.txt` | `e247b2c2f3da87597ae135f24dcfe49d3e9b13c80ed69fef499b371fe8541028` |
| `Unofficial_Patch/vdata/HackTerminals/kilpatricks_computer.txt` | `b0a34499aa32713927416399a098f0c9fe4bbbd69d4fcbf62e8808e37273c3fa` |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` |
| `Unofficial_Patch/python/vamputil.py` | `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491` |

Выборочно сверены важные entities, I/O и опорные грани установленного BSP. Открыты полная планировка, коллизия, два варианта терминала, последовательность Arthur и последствия его смерти в runtime.
