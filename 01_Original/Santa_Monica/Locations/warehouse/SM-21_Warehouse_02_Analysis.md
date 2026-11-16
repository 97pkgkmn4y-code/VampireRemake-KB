---
id: SM-21-ANALYSIS
map: sm_warehouse_1
---
# SM-21.02 — Ограничения и проверки

`VERIFIED_STATIC` для указанных цепочек DLG/BSP/Python. Подготовка и получение Астролита описаны в [[../apartment1/SM-16_Apartment_02_Mercurio|SM-16]]. Установленный UP BSP определяет I/O склада. В SDK VMF аргумент `beckett_check.Test` равен `2` (L132819), в UP BSP он равен `0`. Полное сравнение с базовым BSP и SDK VMF остаётся открытым.

## Вход и запись задания

- Mercurio 231 или его журнал открывают `Warehouse=2` или `6`. Все три развязки Voerman (`tourette.dlg` 671/721/761) пишут `Warehouse=3`, который даёт `Explosive01`. Знакомство с Tung (12/13 в `bertram.dlg`) задаёт 1 в Basic или 8 в Plus, оба дают `Explosive02`. Текст 1 просит обойтись без убийств, текст 8 — без обнаружения (`vdata/system/quests_santamonica.txt` L679–741).
- Цепочка Nosferatu без канализационной карты 155 → 511 выдаёт `item_g_sewerbook_1` и ставит `Bertram_Map=1`, затем 512 → 461 возвращает к выбору. 463 с картой и Астролитом выставляет `Bertram_Ready=2`. Для тех, кто отложил поездку, вход 997 ведёт к 461 при `Bertram_Go==1 && Bertram_Ready<2` (`bertram.dlg`).

## Истечение времени и ветки Beckett

- По достижении 180 секунд таймер вызывает тот же `explosion_event`, который может вызвать `beckett_trigger`. Relay сразу записывает `Warehouse=4` с `Explosive03` и вызывает `explosion_playervolume.CheckNow`. При обнаружении игрока в этом объёме включаются fade и эффект на viewmodel. Дальше relay вызывает `HurtNow` в нескольких brush-объёмах через 0,1–1,0 с. У `explosion_hurt_1/2/3/5` прописан урон 2000, у `plus_explosion_hurt_4` — 200. Предикаты отдельных эффектов привязаны к объёмам. Отдельной записи провала для таймера в этих выходах нет (UP BSP, `warehouse.py` L59–61, журнал L705–710).
- Бонус проверяется по выходу, запланированному на +2 с после `OnBombPlaced`. В Basic `Warehouse_Kills==0` даёт `Explosive04`. В Plus `Warehouse_Spotted==0` даёт `Explosive06` и выставляет `Beckett_Swap=1`. Убийства и обнаружение записываются выходами NPC. Таймер и эвакуация запускают взрыв отдельными выходами, поэтому в момент их срабатывания проверки бонуса уже не назначаются (UP BSP, `warehouse.py` L39–58, `vdata/system/experience_table.txt` L49–54). Оба relay бонуса и Sabbat запланированы на +2 с. Точный порядок между ними в движке не проверен.
- При касании `beckett_trigger` проверяется `G.Beckett_Swap==1`. `OnTrue` перемещает `beckett_wolf` через `wolf_teleport`, создаёт контроллер, включает `beckett_wolf_camera` и звук волка. `OnFalse` через 1 с запускает `logic_scene`, который перемещает игрока через `teleport_player_1` и показывает `Beckett`. Исходный `Beckett` — волк с `MorphModel` человека, `OnTransformComplete` запускает разговор. При свопе имя `Beckett` получает человеческий `Beckett_old`. У него `OnDialogEnd` запускает уход по точкам `B1 B2 B3` и ставит `toSantaMonica()` на +5 с. У исходной волчьей entity этот же вызов идёт без задержки (UP BSP, `warehouse.py` L36–57).
- У рычага `prop_switch` с моделью `SewerGateLever` соседний `trigger_multiple` показывает `game_text` с сообщением о запуске взрыва (UP BSP и SDK VMF L148339–148435). Выход рычага вызывает только `explosion_event`. Включение `beckett_trigger` и запуск бонуса остаются на выходах `OnBombPlaced`.

## Доклад Tung и LaCroix

- Выход из первого разговора с Beckett (122 в `dlg/main characters/beckett.dlg`) записывает `Story_State=5` и `Ninesintro_Open=1`. При `5<=Story_State<25` и `Bertram_Goodjob==0` вход 996 в `bertram.dlg` ведёт к 631, выставляет `Bertram_Goodjob=1` и пишет `Warehouse=7` с направлением в Venture Tower.
- `trig_nines_cutscene.OnTrigger` и `nines_mark.OnEnterMapHere` в `maps/la_hub_1.bsp` вызывают `OnNinesCutscene()`, который переводит `Story_State=5 → 10` (`python/downtown/downtown.py` L532–541). В `dlg/downtown la/prince1.dlg` старт 1072 при `Story_State==10` ведёт к 61. Ответы 62–64 переходят к 71, который повышает `Prince_Reaction` на 1 и пишет `Warehouse=5` (`success`, `Explosive05`). Эти строки доклада проверяют сюжетный флаг. Прямой проверки `Warehouse==7` в них нет.
- Если пожаловаться на Mercurio (74 вне клана Malkavian либо 76 для Malkavian), 101 выставляет `Prince_Mercurio=1`. 102 при `Mercurio_Dead==0` записывает `Mercurio_Dead=1`. Если флаг уже равен 1, доступны 103 в Basic или без журнала и особая 104 в Plus при наличии `item_g_mercurio_journal`. 104 забирает предмет, как 102/103 переходя к 111. Последующие проверки `Prince_Mercurio` убирают NPC в квартире и его машину в hub (`santamonica.py` L76–91, L1778–1780) и блокируют его появление у лодки (`beachVisitors()` L1496–1506).

## Открытые проверки

| Открытый вопрос | Статус | Ограниченный тест/исследование |
| --- | --- | --- |
| Вход, геометрия, доступные и заблокированные маршруты | `UNVERIFIED` | Разметить VMF/BSP по зонам и пройти карту в UP Plus 12.0 |
| Предмет/условие `OnBombPlaced`, жизнеспособность switch | `RUNTIME PENDING` | Saves с бомбой/без неё; зафиксировать доступность bomb site/switch и изменение журнала |
| Истечение времени и вход в Beckett trigger | `RUNTIME PENDING` | Сопоставить выживание внутри/вне объёма урона и возможность выхода при взрыве по таймеру |
| Бонус, появление Sabbat и две ветки Beckett | `RUNTIME PENDING` | Сравнить обнаруженный и незамеченный проход, учесть порядок двух relay на +2 с |
| Последствия для Mercurio и следующих этапов | `RUNTIME PENDING` | Сравнить возврат в Hub/Apartment после доклада с жалобой и без неё, проверить сдачу журнала |

Для полного переноса миссии в Unity нужны route/коллизионная карта и проверка хотя бы двух исходов взрыва. Наличие отдельных I/O не устанавливает альтернативный способ прохождения.
