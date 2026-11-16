---
id: SM-25
map: sm_hub_2
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
depth_required: A
---
# SM-25 — Santa Monica Hub 2, предварительный паспорт

`sm_hub_2` — отдельная установленная BSP позднего состояния района. Ниже описаны геометрические ориентиры, условия доступа и выбранные системы Bloodhunt.

## Переходы

- В установленном UP BSP есть восемь `trigger_changelevel`: Haven, Pawnshop, Apartment, `ApartmentTeleport1_plus` (`sm_apartment_1b`), taxi/специальные внешние цели; полный список и SHA в [[../../Space/Santa_Monica_BSP_Changelevels.csv|реестре]].
- `apartment_door_left/right.OnFullyOpen` в BSP вызывают `ApartmentTeleport1.ChangeNow` с `map=sm_apartment_1`. `ApartmentTeleport1_plus *37` имеет `StartHidden=1` и Disable Touch. Для него не найдено I/O активатора в карте. Его нет в базовом Hub 2 BSP. Повторная проверка loose-файлов и VPK индексов `Unofficial_Patch` и `Vampire` не обнаружила `maps/sm_apartment_1b.bsp`. Одноимённый Python hook в `vamputil.py:3553–3555` только планирует `hunterStats()`. Достижимость отдельной цели остаётся `UNVERIFIED`.
- `apartmentLeave()` (`santamonica.py:25–29`) отправляет из Apartment к `ApartmentTeleport2` в Hub 2 при `Story_State==90 && Credits_Running==0`, иначе к Hub 1. `pawnshopLeave()` (L1474–1479) выбирает `PawnshopTeleport2` при `Story_State==90`. Это внешние Python-переходы к позднему району; прямого `trigger_changelevel` Hub 1 ↔ Hub 2 в проверенных BSP нет.
- `trips_door.OnFullyOpen → PawnshopTeleport1.ChangeNow` в этой карте ведёт к `sm_pawnshop_2`. `haven_door.OnFullyOpen` сохранил цель `HavenTeleport1`, но entity lump Hub 2 содержит только `HavenTeleport2` (в `sm_pawnshop_1`, landmark `Haven2`). Явного `ChangeNow` для него нет. Из убежища поздний переход существует через другую версию двери, см. [[../pawnshop1/SM-29_Pawnshop_1_Passport|SM-29]].

## Геометрические опоры

Пробами `hub2-haven-to-trip` и `hub2-trip-to-mercurio` найдены уличные маршруты по world brushes между входными площадками. Повтор с `--terrain` дал те же 104 и 131 положений; оба пути остаются на X≥−2056, далеко от западных размещений `AlleyWall*`. [[../../Space/Santa_Monica_BSP_Brush_Routes.csv]]

В установленном BSP `info_player_start=(-1676,-3140,-102)` около заднего переулка убежища, поверхность Z=-112 (face 8972). У порога Trip's Pawnshop Z=-112 (8600), у подъезда Mercurio Z=-76 (8565), а у ориентиров `bloodhunt_1_h=(-2464,-2112,-104)` и `bloodhunt_2_h=(-2336,1808,-104)` Z=-120 (8950 и 6890). Поздние переходы в `sp_tutorial_1` используют отдельные объёмы `*43` и `*42` к югу и северу соответственно.

## Состояние при загрузке

`logic_auto.OnMapLoad` в BSP вызывает `openShops()`, `bloodHuntClanCheck()`, `unhidePlus()`; конкретное выполнение в игре не проверено. `openShops()` (`santamonica.py:688–713`) отпирает `trips_door`, если Trip не мёртв; отпирает две apartment doors, если Mercurio жив и `G.Mercurio_Attack==0`; может показать Knox при `Knox_Pissed>0` и Mercurio при `Mercurio_Attack==1 && Prince_Mercurio==0`. Наличие NPC в карте и условия скрипта не доказывают их фактическое появление в каждом состоянии.

- Knox `(-1172,464,-108)` и Mercurio `(-600,-2196,-80)` в BSP имеют `StartHidden=1` и `player_reaction=D_HT 5`. Разные DLG и условия показа сохраняют раздельные ветки.
- `openShops()` при отсутствии `AlleyWall*` создаёт три `prop_dynamic` на X=−3060, Z=−50 с Y=305, 1805, −2100 и yaw 90 (`santamonica.py:705–711`). Через SDK Crowbar декодированы MDL и DX80 VTX. Все три размещения имеют видимые границы X −3067.96…−3051.96, Z −227.39…126.30 и по Y около ±198.56 от origin. Hull bounds заголовка MDL имеют другие размеры, около 35×35×50 units. PHY отсутствует в проверенных loose-файлах, обоих VPK индексах и pak lump `sm_hub_1/2`. `createEntity()` перед `CallEntitySpawn` задаёт имя и модель без поля `solid` (`vamputil.py:3836–3844`). Тип коллизии при спавне и обход модели движком остаются открытыми. SHA-256 `Unofficial_Patch/models/scenery/misc/blackbox/AlleyWall.mdl` — `38121515e7cefb05e0d44bdb7dcd46cedbdaee0ced149b3711a155d26c2d557c`.
- Map-load настраивает patrol type для `potence_2`, `auspex_1`, `fortitude_2` и через 0.1 с адресует пути `b1 b2`, `a1 a2`, `c2 c1`. Три NPC на `OnFoundPlayer` задают соответственно Potence 3, Auspex 3 и Fortitude 3. `bloodHuntClanCheck()` подменяет модели по клану игрока. Для Nosferatu и Toreador также ставит `Bloodhunt_Obfuscate=1`. Отдельная `obfuscatorsCheck()` переключает двух obfuscators на Potence 3 при этом флаге 0.

## Источники и ограничения

### Hunter Bloodhunt

1. В `sp_tutorial_1` ответы 25/45 `hunter1.dlg` выставляют `Hunter_Bloodhunt=1`. `Hunter1.OnDialogEnd` через 1 с вызывает `hunterQuests()`, который показывает `bloodhunt_1_h_trigger *179` при этом флаге и отпирает `frontdoor1/2`, пока `Hunter_Finished=0`. Обе двери по `OnFullyOpen` адресуют `ChangeNow` к этому триггеру в той же карте. Переход ведёт в Hub 2 через южный landmark `bloodhunt_1_h`.
2. В Hub 2 охотничья ветка `setPlus()` при `Hunter_Bloodhunt=1` показывает северный `bloodhunt_2_h_trigger *42`, скрывает `CaineTeleport1`, Caine, taxi и windows, запирает Trip и обе двери Apartment и переводит флаг в 2. Северный объём по `OnStartTouch` вызывает собственный `ChangeNow` в `sp_tutorial_1`. Южный `*43` в Hub 2 имеет `StartHidden=1`, Disable Touch и не имеет найденного локального активатора. Он отличается от одноимённого `*179` в Tutorial. Порядок `openShops()` и `setPlus()` в игре остаётся открытым. Штатная ветка Caine использует `toCaineTaxi()`, `CaineTeleport1` и `sp_taxiride`. [[../../Space/Transitions]]
3. Статическая проба `--terrain --goal-directed --start -2464 -2112 -80 --finish -2336 1808 -95 --grid 12 --step 18 --margin 3300 --limit 45000` нашла 1109 положений по брашам и 288 треугольникам рельефа (20 652 посещённых). Маршрут уходит на восток до X=524. Корпус в конце пересекает браш 2891 северного объёма `*42`. Проба не учитывает NPC и изменения состояния в игре.
4. После возврата через северный landmark реплика `hunter1.dlg:195` проверяет `Hunter_Bloodhunt=2` и ведёт в 91. Ответ 92 завершает задание, ставит флаг 3 и даёт $100. У ответа нет проверки числа убитых NPC. В проверенных ветках входа, выхода и отчёта отдельного счётчика убийств не обнаружено.

- `SDKContent/MapSrc/up sources/sm_hub_2.vmf`, SHA-256 `e0c00b92879b6a0acac1106b56d4c6f7cf7242aa26ec2dc4e0cd44b176d9bbae`.
- `Unofficial_Patch/maps/sm_hub_2.bsp`, SHA-256 `88df4bf1d10db9a31f0c01c7491580760a175b6c8ea7f330779262ded479c724`.
- `Unofficial_Patch/python/santamonica/santamonica.py`, SHA-256 `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`.

Выборочно сопоставлены названия целей VMF/BSP; полная геометрия, коллизия, NPC и quest graph Hub 2 не исследованы. Runtime `RUNTIME PENDING`.
