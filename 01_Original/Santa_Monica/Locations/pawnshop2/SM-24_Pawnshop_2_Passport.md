---
id: SM-24
map: sm_pawnshop_2
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-24 — Trip's Pawnshop, технический паспорт

**Назначение и переходы.** В установленном BSP entity lump 56 entities; именованный NPC `Trip` с `dialogname=dlg/Santa Monica/Trip.dlg`. `talk_to_trip.OnPressed → Trip.StartPlayerDialogRemote`. `exitdoor.OnOpen` вызывает `pawnshopLeave()`; `santamonica.py:1474–1480` выбирает `PawnshopTeleport2` при `Story_State==90`, иначе `PawnshopTeleport1`. Два `trigger_changelevel` в BSP ведут соответственно в `sm_hub_2` и `sm_hub_1`, оба с `landmark=pawnshop1`. Входящие связи — в [[../../Space/Transitions|реестре]]. Тексты условий отделены от фактического выполнения в игре.

**Диалог и зависимости.** `trip.dlg` ID 22–24 содержит отдельные проверки `G.Trip_Know==1/2/3`, с репликами об Arthur, Knox и Mercurio. ID 31 ставит `G.Trip_Know=4`; ID 41 — `G.Trip_Guns=3` и вызывает `TripStoryState()`. Это социальные условия продажи оружия, а не доказательство того, что каждая ветка достижима в одном прохождении. Подробные цепочки Arthur/Knox и Mercurio уже находятся в [[../../Quests/Index|индексе квестов]] и [[../apartment1/SM-16_Apartment_02_Mercurio|SM-16]].

**Источники, SHA-256.** `SDKContent/MapSrc/up sources/sm_pawnshop_2_d.vmf`: `b8d8419d3a74aa90d6bb4190abbef7b8b0556578c53aa0febf84bf0908de2d28`; `Unofficial_Patch/maps/sm_pawnshop_2.bsp`: `0d9f4c62a87d2b3faad5a20889daf2de82c5a3573d067fb2a5c093f78e15ba3a`; `Unofficial_Patch/dlg/santa monica/trip.dlg`: `55a98b20305b51c0bff35337ef3d56d751073ff6702ad8a6fa49885b61aca8e6`; `Unofficial_Patch/python/santamonica/santamonica.py`: `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`. Выборочные entities проверены по BSP; коллизия, торговый ассортимент, условия появления NPC и runtime развилок открыты.

## Пространственные опоры

В UP BSP `exitdoor` стоит на Z=-112 (world face 809), внутри у `(-2054,-2380)` и `(-2054,-2440)` пол на той же высоте (face 852). Прилавок выше, его поверхность под кнопкой `talk_to_trip` на Z=-71 (face 601), кнопка имеет центр `(-2058,-2584,-50.5)`; Trip размещён за ней у `(-2060,-2624,-110.807)`. Это выборочные точки поверхности. От этой карты отличается [[../pawnshop1/SM-29_Pawnshop_1_Passport|sm_pawnshop_1]], где расположено убежище.

От входа до точки перед кнопкой проба `trip-counter` нашла 17 положений на Z=−111.95. При добавлении внутренней решётки в её закрытом положении (`--brush-model 7 -2031.5 -2416.5 -61.5`) сетка исчерпана после 39 положений. У решётки Use Opens и `wait=10` в UP BSP, `wait=4` в базовом BSP. В базовом BSP Trip стоит у `(-2056,-2712,-110.807)`, а удалённая кнопка диалога остаётся в той же точке. [[../../Space/Santa_Monica_BSP_Brush_Routes.csv]]

## Торговля и доступ к оружию

| DLG ID | Условие и эффект |
|---|---|
| 9/16 → 51 | Спросить об оружии при `Trip_Know=0` и `Trip_Guns=0`. Отказ 51 устанавливает `Trip_Guns=1`. |
| 52–59 и 62–69 | Варианты используют Inspection >2 или Malkavian, Persuasion 3, Seduction 3, Intimidation 3, Dominate/Dementation и дополнительные Plus-дисциплины. Plus проверяется явно для Thaumaturgy/Presence в 58/59, 67/68. |
| 72–77 | 72/73/76/77 ведут к 81 и повышают `Trip_Trust`, 74 ведёт к 81 с флагом `Dialog_Presence=1`. ID 75 ведёт в 321 и ставит `Trip_Guns=3`. ID 81 ставит Guns=3 и Know=4. Оба вызывают `TripStoryState()` (Story_State 0→1). |
| 82/83 | `npc.StartBarter(G.Story_State,0,G.Trip_Drugs)`, затем `preBarter("Trip")`. 83 требует `Trip_Name=1` и `Extra_Lines=1`, увеличивает доверие. `vamputil.py:2250` запускает таймер обработки дубликатов книг только в Plus. |
| 491 / 616 | Поздний переход к лицензии: начало 616 при Guns 1/2 и Story_State >1. ID 491 устанавливает Guns=3. |

**Ассортимент по vendor data.** В установленном UP `vdata/system/vendors.txt` содержит 29 записей Trip, включая боеприпасы. Базовый файл из `Vampire/pack101.vpk` содержит 24. Патч добавляет биту, кольцо, часы и болты арбалета с `MinStage=0`. Две книги для Computers и Firearms поднимаются с `MinStage=0` до 150. В UP запись для самого `item_w_glock_17c` имеет `AmmoOnly=0`, `MinVendorState=1` и без `MinStage`. Его боеприпасы отдельно имеют `AmmoOnly=1`, `MinStage=5`. Базовый Trip продаёт только боеприпасы Glock с `MinStage=10`. В установленном Trip DLG третий аргумент `StartBarter` равен `G.Trip_Drugs`, который становится 1 после сдачи коробки. Это сопоставление условия ассортимента с веткой задания. Фактическое применение `MinVendorState` и отображаемый список остаются для проверки в игре.

SHA-256 `vendors.txt`: UP `22a97bf2463702d9b5ac6398776ae7ddf3d5923d488cb6b4cd9f9f28a8765270`, база `8e3e9b5c8954235e5b519c61c6defad1c7654c34dec7deeb0c5504c558eab28d`.

## Drug Trip

Название журнала `Trip Drugs`, отображаемое имя Drug Trip. Стадии заданы в `Unofficial_Patch/vdata/system/quests_santamonica.txt` (SHA-256 `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38`).

1. ID 600/159/226/236 ведут к 121 при `Patch_Plus=1`, `Trip_Discount=0`, `Trip_Name=1`, `Trip_Guns>0`. В 122/123 записываются `Trip_Discount=1` и Trip Drugs=1.
2. В [[../medical1/SM-14_Medical_03_Quests|Clinic]] `updateDrugQuest()` при Plus, Discount=1 и наличии `item_g_drugs_drug_box` ставит Discount=2 и Trip Drugs=2. Коробка привязана к сейфу Clinic.
3. ID 152/599/124 при наличии коробки и Discount>0 ставят Discount=3 и ведут в 301. Ответы 303–306 удаляют коробку, записывают Trip Drugs=3 (XP-ключ `Trip01`), `Trip_Delivered=1`, `Trip_Drugs=1` и Finance +1. ID 305/306 дополнительно поднимают Guns до 3. Следующие узлы 281/291 разделены по полу. У 302 отдельная ветвь обычной торговли, если Discount<3 или Trip_Drugs=1.
