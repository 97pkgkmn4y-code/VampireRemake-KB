# Santa Monica — квесты и состояния

Самостоятельные заметки о квестах и переменных состояния. Тексты диалогов и Python не копируются сюда: см. исходные исследования персонажей и карт по ссылкам.

- [[Arthur's_Introduction]] — начальный разговор с Артуром и состояния, не являющиеся отдельными квестами.
- [[Bail_Hustler_Quest]] — состояния делового задания Артура.
- [[Bail_Jumper_Quest]] — ветки bounty hunter Артура.
- [[Knox_Quest]] — Кнокс и связанные переходы между картами; см. также [[../Locations/basement1/SM-18_Basement_00_Index|Gimble basement]].
- [[Santa_Monica_Discovery]] — записи диалога Артура о местах и делах района; в документе отмечено, что это не отдельный квест.
- [[../Locations/medical1/SM-14_Medical_03_Quests|Medical Clinic — квестовые состояния внутри анализа карты]].

## Межкартовые зависимости журнала

Имена, ID и награды сверены с `Unofficial_Patch/vdata/system/quests_santamonica.txt` (SHA-256 `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38`). Ниже указаны подтверждённые записи в журнал и связи с картами. Достижимость альтернатив остаётся открытой там, где покрытие частичное.

| Журнал | Проверенные связи |
|---|---|
| Mercurio, Astrolite, Morphine | [[../Locations/pawnshop1/SM-29_Pawnshop_1_Passport\|Haven]] задаёт Mercurio=1, `mercurio.dlg:1` — 2. `mercurio.dlg:121` назначает Astrolite=1. В Beach House `astrolitePickup()` пишет 2 или 5 при прежнем 4 и повышает criminal level при `Dennis_Alone=0`. `dennis.dlg` также пишет 2/5; `mercurio.dlg:171` завершает Astrolite=3. Смерть Mercurio и подбираемый журнал меняют стадии 6/7. Morphine назначается в DLG Mercurio, `morphinePickup()` даёт 2, DLG 152/153 — 3, поздний 918 — провал 4. [[../Locations/apartment1/SM-16_Apartment_02_Mercurio\|Mercurio]] |
| Arthur Knox, Bail Jumper, Muddy | [[Knox_Quest\|Carson]] связывает Bail Bonds, Tattoo и Gimble. [[Bail_Jumper_Quest\|Bail Jumper]] связывает Артура, автоответчик Мурьетты и возвращение к Артуру. `arthur.dlg:381` отдельно открывает Muddy=1 после отчёта. Журнал Muddy=2–4 продолжает цепь за пределами района. |
| Knox Asian | [[Knox_Quest\|Knox]] → Krimeputer (`virgilViewed()`) → морг (`gimbleDead()`, получение ключа) → [[../Locations/vamparena/SM-30_Foxy_Boxes_Passport\|Foxy Boxes]] → отчёт. Бой даёт 3, отчёт или разоблачение дают успешные 4/6, смерть Knox при активных состояниях — провал 8. |
| Lily | [[Pier_Thin_Bloods\|Thin Bloods: Lily and Copper]] details the Pier dialogue, outcomes, deaths and late-story cutoff. `e.dlg:119/139/149/159` starts state 1; the [[../Locations/diner1/SM-15_Diner_02_Systems\|Diner]] clue chain and `diaryPickup()` advance it to 2; the [[../Locations/medical1/SM-14_Medical_03_Quests\|Clinic]] frees Lily at state 3; `e.dlg:221` records reunion at 8 (`Thinned04`). |
| Danielle | `vandal.dlg:382` ставит 1, Danielle ID 71 — 2, Stan Gimble 256/257 — 7. Журнал 4/5 соответствует варианту Patty и её смерти. Vandal 365/366/399/411 пишут успех 6 (`Danielle01`), `vandalDeath()` может дать 3. [[../Characters/SM-13_Danielle_Introduction\|Danielle]] |
| Hotel, Release the Spirit, Slashterpiece | [[../Characters/SM-13_Asylum_07_Therese_Dialogue\|Therese]] отправляет в [[../Locations/oceanhouse/SM-20_Ocean_House_00_Index\|Ocean House]]. Pendant и возврат меняют Hotel, DLG меняет варианты сдачи. [[../Characters/SM-13_Asylum_08_Jeanette_Dialogue\|Jeanette]] связывает pendant и [[../Locations/gallery1/SM-26_Gallery_00_Index\|Gallery]]. В Gallery смерть Guardian пишет Slashterpiece=2, другие исходы задаются DLG. |
| Diner, Tourette, Warehouse | Therese ID 381 ставит Diner=1, `thugsAllDead()` — 2 и включает `SMphone`. ID 41/51 телефона ставят Tourette=1/2. `tourette.dlg:671/721/761` пишет успешные Tourette=5/4/3 и Warehouse=3. `toWarehouse()` ведёт на [[../Locations/warehouse/SM-21_Warehouse_00_Index\|Warehouse]] при `Bertram_Ready=2` и Story_State<5. |
| Werewolf Blood | Письмо Haven через `werewolfBloodQuestAssigned()` даёт 1, кровь в Clinic — 2. Обычный выход из Haven с образцом в ящике даёт 3. Ответное письмо через `werewolfBloodQuestDone()` даёт 4 (`Wblood02`). |
| Serial | Газета в Haven/Smoke → `murderPaperRead()` при Story_State<5 и Serial=0. [[../Locations/diner1/SM-15_Diner_02_Systems\|Diner]] и [[../Locations/junkyard1/SM-28_Junkyard_00_Index\|Junkyard]] содержат встречу Killer и разные успешные записи 8/9. |
| Heather, Strauss, BertramCD | Plus-функции `heatherQuest1/2/3` ведут журнал Heather в Clinic и дальше, а её появление в Haven зависит от `Heather_Haven` и `Heather_Gone`. `regentInvite()` ставит Strauss=1, Regent DLG 2/3/11 — 2. Письмо Haven вызывает `bertramSetQuest()` (BertramCD=4), `checkCD()` и `bertram.dlg:561–574` управляют поиском и сдачей. |
| Copper | [[Pier_Thin_Bloods\|Thin Bloods: Lily and Copper]] covers Plus quest `Daydream Believer`, persuasion and scam branches, payments, XP, death and `Story_State>=35` cutoff. |
| Bloodhunt, Ming | `jack.dlg:1311` ставит Bloodhunt=1 в позднем Haven, `caine.dlg:1` — 2. Ming меняется за пределами района в DLG Nines, Caine, Ming Xiao и Regent. Локальные переходы описаны в [[../Locations/hub2/SM-25_Hub_2_Passport\|Hub 2]] и [[../Locations/pawnshop1/SM-29_Pawnshop_1_Passport\|Haven]]. |
| Trip Drugs | [[../Locations/pawnshop2/SM-24_Pawnshop_2_Passport#Drug Trip\|Trip → Clinic → Trip]]: запрос Plus, коробка из сейфа, журнал 1→2→3, `Trip01` и Finance +1. |
| Hunter Temple, Hunter Hallowbrook, Hunter Giovanni, Hunter Bloodhunt, Hunter Society | Пять самостоятельных определений кампании охотника. Стадии 1→2 (Society 1→2→3) и XP `Hunter01`…`Hunter05` сверены. Сценарные ветки охотника остаются `PARTIAL`. |

Для Mitnick см. [[../Locations/shreknet1/SM-22_Shreknet_Passport|первый хаб и путь почтового ключа]].

## Night at the Library

Цепь связывает убежище, Smoke Shop, Pier, Coffee Shop и Downtown. Журнал `Library` задан в `Unofficial_Patch/vdata/system/quests_downtown.txt` (SHA-256 `5b533c73c5f61209b14aab5b76d936d6f9a699e075c71fe1d81fef2420c7ee17`). SHA `vamputil.py`, `santamonica.py` и почты приведены в [[../Locations/pawnshop1/SM-29_Pawnshop_1_Passport|SM-29]].

| Шаг | Условие и запись |
|---|---|
| Письмо в убежище | `setPlus()` ставит `Library_Ready=1`, если `Jumbles_Removed=1`, `LaSombra_Seen=1`, `Isaac_Movie>0`. В `haven_pc.txt:247` письмо требует `Library_Ready>=1` и Plus. Вызов `librarySetQuest()` при Smoke=0 ставит Library=1 и `Library_Smoke=1`. |
| [[../Locations/smoke1/SM-19_Smoke_00_Index\|Smoke Shop]] | `setPlus()` показывает записку при Smoke=1. Разговор с продавцом даёт контекст. Записка при чтении ставит `Library_Smoke=2` и через 0.1 с вызывает `librarySetQuest()`: Library=2, Note=1, Smoke=3. |
| [[../Space/Surface\|Pier]] | `logic_auto.OnMapLoad → murderCleanedUp()` показывает `piernote` и подсветку при Note=1. Чтение ставит Note=2 и через 0.1 с вызывает `librarySetQuest()`: Library=3, Coffee=1, Note=3. При выходе из чтения записаны отдельные выходы на частицы и показ `trapobfuscator`. |
| [[../Locations/coffee1/SM-17_Coffee_00_Index\|Coffee Shop]] | `setPlus()` отпирает вход при Coffee>0. Пятая запись Scott laptop ставит Coffee=2; при Open=0 вызов `librarySetQuest()` задаёт Library=4, Open=1 и Coffee=3. |
| Downtown → Library | `setPlus()` при Open>0 показывает `library_open` у `(650,-5017,-980)` в `la_hub_1` и скрывает `library_closed`. Активный люк через `OnActivate → library_trigger.ChangeNow` (1.5 с) ведёт в `la_library_1`, landmark `library_entrance`. `library_leave` ведёт обратно. SHA BSP: `la_hub_1` — `f2cbdce345bc3d709880d42274fd4a75ceadcf7aa350612d77c159ea397037be`, `la_library_1` — `2008a86c9f6727f9b25d9885f4dc2a1706a81ea1c16fb02a9185aaa872b6fd4b`. |
| Исход в скриптах | `useBox()` при наличии коробки ставит Library=5, первое `unhideKey()` — 6, `foundRitualChamber()` — 7, `defeatedAndrei()` — 8 и Jumbles_Removed=2. Следующее письмо при Plus/Jumbles_Removed=2 пишет Open=2; при обоих `Guard*_Killed=0` `librarySetQuest()` выдаёт `Library02` и ставит Open=3. Постановочные входы внутри Downtown Library требуют собственной проверки. |

