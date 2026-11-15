---
id: SM-29
map: sm_pawnshop_1
reference: Unofficial Patch Plus 12.0
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-29 — Santa Monica Haven и квартира Мурьетты

Карта включает первое убежище игрока и квартиру Мэриан Мурьетты. Сущность Trip находится в [[../pawnshop2/SM-24_Pawnshop_2_Passport|магазине на sm_pawnshop_2]]. Координаты ниже даны в Source units.

## Источники

Пути относительно каталога установленной игры `Vampire - The Masquerade Bloodlines`. BSP v17, 468 записей в entity lump UP и 443 в базовой копии. VMF помечен как результат BSPSource 1.2.1 (строка 21). Точный входной BSP этой декомпиляции неизвестен.

| Источник | SHA-256 |
|---|---|
| `Unofficial_Patch/maps/sm_pawnshop_1.bsp` | `62d2c0fceca058f367e9a417a19c69340e42351b67b6cd447995d106a72b9ed2` |
| `Vampire/maps/sm_pawnshop_1.bsp` | `5e4a518f4428cb2f86ac14988bde09510125daabbcb5f65366bc3b47efb3dcc3` |
| `SDKContent/MapSrc/up sources/sm_pawnshop_1_d.vmf` | `c90eb4b753d59240256bab4489eee4b9d9c7c20697a5e085850ec58f81875ff7` |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` |
| `Unofficial_Patch/python/vamputil.py` | `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491` |
| `Unofficial_Patch/vdata/hackterminals/haven_pc.txt` | `7b8db3d8dad85c340cc86e6f5c7c24e63f9e3f784a39017a177547e6102c796d` |
| `Unofficial_Patch/dlg/Main Characters/Heather.dlg` | `be6b2e015a0328112347dc50c2bceae9a3e9752b12552b86bacb8f465b09fd11` |
| `Unofficial_Patch/dlg/Main Characters/Jack.dlg` | `78e3bb2170fd27cc42ef9344895628bc02820899ff6d400adfce3739e17aae5f` |
| `Unofficial_Patch/dlg/Generic/Mcfly.dlg` | `158249a2f01f2485bba76f8245213ec6b03038c4970683fe9cbe8a45a5d3200c` |
| `Unofficial_Patch/dlg/Generic/Newscaster.dlg` | `fb39b20b991a3b0eaca51a59c713af993c2f7d7e5a2a67049c99923267a719ab` |

## Пространство

Выборка горизонтальных полигонов world model установленного BSP сделана по плоскостям граней через face → surfedge → edge → vertex. Ниже указаны индексы граней в lump 7. Замеры локальны. Для перехода игрока существенны также дверные состояния, коллизия и ширина свободного прохода.

| Зона | Геометрия и ориентир |
|---|---|
| Вход из переулка | Обе версии двери `back_door` / `back_door_2` имеют origin `(-1747.5,-3169,-62)` и совпадающие занятую область и локальные bounds моделей `*19` / `*33`. У landmark `haven1`/ `haven2` горизонтальная грань пола 3566 на Z=-112 в точке `(-1775,-3144)`. |
| Нижний подъём | Поперечная выборка по Y=-3170 обнаруживает ступени от Z=-92 при X=-1830 до Z=24 при X=-2022. Дверь `nextdoor2` на этом уровне имеет локальный низ на Z=24, совпадающий с гранью 4206 у её pivot. |
| Верхний подъём | Вдоль X=-2060 от Y=-2962 до -2794 поверхности поднимаются Z=36, 44, 52, …, 132, 144. Грани 4174, 4172, 4171, 4150 и 3803 показывают переход к верхнему коридору. |
| Верхний коридор и убежище | Порог `havenrm` и основная поверхность убежища на Z=144, грани 3125 и 3142. `info_player_start` = `(-1981.12,-2585.93,153)`. Холодильник `(-1886,-2688,144)`, ноутбук `(-1788.7,-2475.69,182)`. |
| Квартира Мурьетты | `nextdoor` = `(-2084.5,-2559,199)`, порог Z=144 (грань 3796). За ним поверхность Z=144 под автоответчиком `(-2226,-2467.46,167.65)` (грань 3802). Ключ `murietta_key` лежит в верхнем коридоре `(-2047,-2468,157.248)`. У ручки `nextdoor` есть `key_name=item_k_murietta_key`, `delete_key=1`, `difficulty=3`. |

## Переходы и их условия

Для [[../../Space/Santa_Monica_BSP_Brush_Routes.csv|геометрических проб]] `haven-stairs` найдена последовательность из 75 точек от входа на Z≈−111 через оба подъёма до Z=144. Проба `haven-murietta` соединяет убежище с точкой у автоответчика 29 положениями корпуса. При добавлении дверной модели `nextdoor` `*20` в исходный pivot `(-2084.5,-2559,199)` та же проба исчерпала сетку без пути `haven-murietta-closed`. Условия раскрытия ключа и реакции на открывание остаются отдельными от геометрии.

- `sm_hub_1`: `haven_door.OnFullyOpen → HavenTeleport1.ChangeNow`, landmark `haven1`. Обратно `back_door.OnFullyOpen → HavenTeleport1.ChangeNow`. При выходе вызывается `mailboxExitCheck()`.
- `jackVisit()` при `Story_State == 90` вызывает `bloodhunt_on_relay`. Relay скрывает обычную дверь с ручкой и показывает `back_door_2` с её ручкой. Эта дверь ведёт через `HavenTeleport2` в `sm_hub_2`; при `Story_State > 90` `bloodhunt_off_relay` восстанавливает обычный выход. В Hub 2 переход обратно записан как `HavenTeleport2`, однако `haven_door.OnFullyOpen` адресует `HavenTeleport1`, отсутствующий в entity lump Hub 2. Достижимость обратного пути открыта.
- `HavenTeleport2.OnChangeLevel` адресует `werewolfBloodHavenExit()`, включая базовый BSP и SDK VMF. Определение отсутствует в проверенных установленных `.py`. Фактическую обработку вызова движком следует проверить.
- На позднем этапе `havenrm.OnOpen → havenTaxiCheck()`; при `Story_State >= 100` и `Credits_Running == 0` это вызывает `ChangeMap(2.5, "caine_landmark", "smhaven_caine")` в `sp_taxiride`. Ещё три brush-перехода записаны в `sp_genesisdevice_1`, `sp_tutorial_1` и `sp_observatory_1`. Прямых вызовов этих трёх из локальных entity-выходов не найдено. См. [[../../Space/Transitions|реестр переходов]].

## Квесты и интерактивные объекты

| Событие | Условия и эффекты |
|---|---|
| `logic_auto.OnMapLoad → beginningTheGame()` | Ставит журнал `Mercurio=1`, если предыдущее значение ниже 1. При отрицательном `Story_State` записывает -1. Тот же map-load набор вызывает `jackVisit`, `malcolmBribed`, `muriettaGone`, `heatherHavenP`, `stockTheFridge`, `posterCheck`, `lockHaven`, `malkTalkToTV`, `inviteGone`. |
| Улики Мурьетты | После `arthur.dlg:331` (`Arthur_Muddy=2`, журнал Bail Jumper=1) `muriettaGone()` показывает ключ, кнопку и подсветку. Три выхода `answering_machine_button.OnPressed` в сохранённом порядке: удаление подсветки (0), проигрывание `muddy_message_sound` (0), `updateBailJumperQuest()` (20 с, один раз). При `Muddy_Message=0` функция ставит Bail Jumper=2, `Muddy_Message=1`, `SK_Downtown=1`. Возврат Артуру и ветви провала в [[../../Quests/Bail_Jumper_Quest\|Bail Jumper]]. |
| Начальные припасы | Отдельный `logic_auto` однократно добавляет `starting_money` в `haven_desk_drawer`. Запись map-load для `stockTheFridge()` тоже однократная. Скрипт кладёт три `item_g_bluebloodpack` для Ventrue или три `item_g_bloodpack` для остальных. |
| Документы | Чтение газетной `prop_sign` вызывает `murderPaperRead()` один раз: Serial=1 при Story_State <5 и Serial=0. Чтение `regent_invite` вызывает `regentInvite()`: при Strauss=0 ставятся Strauss=1 и `Regent_Invitation=1`. `inviteGone()` убирает приглашение после `Regent_Introduced=1`, записку Меркурио после `Mercurio_Know=1`, плюс пиццу в Plus после `Heather_Haven=1`. Связь с финалом Serial в [[../junkyard1/SM-28_Junkyard_00_Index\|SM-28]]. |
| Ноутбук и ящик | `haven_pc` имеет difficulty 5. Письма Mitnick в `haven_pc.txt` через `putStuffInMailBox()` выдают предметы в ящик по `Shubs_Email` и `Shubs_Email_Read`, первый ключ ведёт в [[../shreknet1/SM-22_Shreknet_Passport\|Megahurtz Computing]]. `mailboxExitCheck()` при наличии `item_g_werewolf_bloodpack` заменяет его на `werewolf_reward`, пишет `Werewolf_Quest=4`, Werewolf Blood=3 и вызывает `ChangeMasqueradeLevel(-1)`. Здесь же записаны обмены предметов для серии Gary. |
| Смена убежища | При `Prince_Skyline`, `Gary_Haven` или `Regent_Family == 3` `lockHaven()` вызывает `haven_emptier` и скрывает выбранные постеры. Relay сначала показывает Heather/McFly (задержка 0), затем адресует обоим `Kill` (0.2 с). Только Basic скрывает ноутбук и переименовывает `Mailbox_haven`; Basic-взятка Malcolm добавляется в этот ящик при `Malcolm_Affair=4/5` и живом Malcolm. |

## NPC и постановка

- **Heather.** Скрыта на старте. `Heather.dlg:191/201` устанавливают `Heather_Haven=1`; `heatherHavenP()` раскрывает живую Heather и вызывает `heatherSkin()`. Поздний порог State≥75 при `Heather_Indoors=0` и `Player_Sabbat<3` или `Heather_Gone` приводит к скрытию. Plus-ответ 744 устанавливает `Heather_Indoors=1`. Прощальные узлы 301/311/331/621 устанавливают `Heather_Gone=1` и вызывают HumanityAdd(1); `Heather.OnDialogEnd → heatherLeaves()` при этом флаге запускает fade, `WillTalk(0)` и `Kill` через 3 с. Три скрытые постановочные фигуры `heather_dummy` и `heather_dummy_3` не имеют её DLG в BSP.
- **McFly.** Скрыт на старте. Условие показа в `heatherHavenP()`: State≥30 и <75, Heather в убежище и жива, `Heather_Gone=0`, `Heather_Lure=0`. Позднее в той же функции `Story_State>70`, смерть или любой флаг `Mcfly_Leave/Feed/Dominated/Dementated/Dump` удаляет его. Узлы `Mcfly.dlg:41,51` задают Dominate/Dementation outcomes, 62/112/122 — Leave, 121 — однократные $50 через `Mcfly_Money`, 131 — Feed. `OnDialogEnd → mcflyDialog()` запускает fade и отложенное удаление при Leave/Dominated/Dementated. В Plus ручки `plus_handle1/2` запираются при `Mcfly_Present=1` (иначе отпираются).
- **Jack.** Скрыт на старте. При State=90 `jackVisit()` показывает его, через 1 с начинает remote DLG и переключает дверь и `SetSafeArea(2)`. Plus-ветка при здоровье <100 выдаёт/пополняет elder vitae и планирует Bloodgain. При State>90 Jack скрывается и устанавливается `SetSafeArea(1)`.
- **Телеведущий.** Обычная `npc_VNewscaster` служит источником TV. Malkavian при State 65–85, `News_Spoke=0`, `Player_Insane=0` включает отдельную `newscaster_malkavian` и touch-триггер, временно переименовывая обычную. Touch запускает remote DLG через 0.1 с; DLG ID 461 выставляет `News_Spoke=1`. `OnDialogBegin` запускает камеру, `OnDialogEnd` закрывает кадр, убирает экран и восстанавливает обычного newscaster через `malkTvDone()`.

Открыты проходимость нижнего и верхнего лестничных маршей, сценарии загрузки Hub 2, граничные состояния Heather/McFly, порядок отложенных действий и ветки почты при смене убежища. Отдельные сценарии и критерии внесены в [[../../Space/Runtime_Verification|план runtime-проверок]].
