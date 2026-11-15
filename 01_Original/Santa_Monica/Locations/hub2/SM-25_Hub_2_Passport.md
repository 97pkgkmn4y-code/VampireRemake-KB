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
- `apartment_door_left/right.OnFullyOpen` в BSP вызывают `ApartmentTeleport1.ChangeNow` с `map=sm_apartment_1`. Для `ApartmentTeleport1_plus` прямого I/O вызова в этом entity lump не найдено. `sm_apartment_1b` отсутствует среди 22 loose BSP; проверка VPK индексов ранее также не обнаружила цель ([[../../../../KNOWLEDGE_BASE_AUDIT|аудит]]). Это `TARGET_NOT_FOUND_IN_CHECKED_SOURCES`, достижимость `UNVERIFIED`.
- `apartmentLeave()` (`santamonica.py:25–29`) отправляет из Apartment к `ApartmentTeleport2` в Hub 2 при `Story_State==90 && Credits_Running==0`, иначе к Hub 1. `pawnshopLeave()` (L1474–1479) выбирает `PawnshopTeleport2` при `Story_State==90`. Это внешние Python-переходы к позднему району; прямого `trigger_changelevel` Hub 1 ↔ Hub 2 в проверенных BSP нет.
- `trips_door.OnFullyOpen → PawnshopTeleport1.ChangeNow` в этой карте ведёт к `sm_pawnshop_2`. `haven_door.OnFullyOpen` сохранил цель `HavenTeleport1`, но entity lump Hub 2 содержит только `HavenTeleport2` (в `sm_pawnshop_1`, landmark `Haven2`). Явного `ChangeNow` для него нет. Из убежища поздний переход существует через другую версию двери, см. [[../pawnshop1/SM-29_Pawnshop_1_Passport|SM-29]].

## Геометрические опоры

Пробами `hub2-haven-to-trip` и `hub2-trip-to-mercurio` найдены уличные маршруты по world-brush между входными площадками. Обход добавляемого скриптом `AlleyWall*` в них не моделируется. [[../../Space/Santa_Monica_BSP_Brush_Routes.csv]]

В установленном BSP `info_player_start=(-1676,-3140,-102)` около заднего переулка убежища, поверхность Z=-112 (face 8972). У порога Trip's Pawnshop Z=-112 (8600), у подъезда Mercurio Z=-76 (8565), а у ориентиров `bloodhunt_1_h=(-2464,-2112,-104)` и `bloodhunt_2_h=(-2336,1808,-104)` Z=-120 (8950 и 6890). Два поздних перехода в `sp_tutorial_1` имеют отдельные объёмы в южной и северной части района (`*43` и `*42`). Источник их активации в прохождении требует проверки.

## Состояние при загрузке

`logic_auto.OnMapLoad` в BSP вызывает `openShops()`, `bloodHuntClanCheck()`, `unhidePlus()`; конкретное выполнение в игре не проверено. `openShops()` (`santamonica.py:688–713`) отпирает `trips_door`, если Trip не мёртв; отпирает две apartment doors, если Mercurio жив и `G.Mercurio_Attack==0`; может показать Knox при `Knox_Pissed>0` и Mercurio при `Mercurio_Attack==1 && Prince_Mercurio==0`. Наличие NPC в карте и условия скрипта не доказывают их фактическое появление в каждом состоянии.

- Knox `(-1172,464,-108)` и Mercurio `(-600,-2196,-80)` в BSP имеют `StartHidden=1` и `player_reaction=D_HT 5`. Разные DLG и условия показа сохраняют раздельные ветки.
- `openShops()` при отсутствии `AlleyWall*` создаёт три модели на X=-3060, Z=-50, с Y=305, 1805, -2100. Это размещение динамических препятствий. Размеры, коллизия и обход остаются открытыми.
- Map-load настраивает patrol type для `potence_2`, `auspex_1`, `fortitude_2` и через 0.1 с адресует пути `b1 b2`, `a1 a2`, `c2 c1`. Три NPC на `OnFoundPlayer` задают соответственно Potence 3, Auspex 3 и Fortitude 3. `bloodHuntClanCheck()` подменяет модели по клану игрока. Для Nosferatu и Toreador также ставит `Bloodhunt_Obfuscate=1`. Отдельная `obfuscatorsCheck()` переключает двух obfuscators на Potence 3 при этом флаге 0.

## Источники и ограничения

В охотничьей ветке `setPlus()` при наличии `bloodhunt_2_h_trigger` и `Hunter_Bloodhunt==1` этот объём показывается, `CaineTeleport1`, Caine, taxi и windows скрываются, двери Trip и обе двери Apartment получают `Lock`, а флаг принимает 2. `bloodhunt_2_h_trigger.OnStartTouch` вызывает собственный `ChangeNow`. У `bloodhunt_1_h_trigger` есть только управление видимостью из `hunterQuests()`, а в BSP отключён touch. Штатный Caine запускает `toCaineTaxi()` через `OnDialogEnd`, эта функция нацелена на `CaineTeleport1` в `sp_taxiride`. Порядок `openShops()` и охотничьих операций остаётся открытым. Сценарные источники перечислены в [[../../Space/Transitions]].

- `SDKContent/MapSrc/up sources/sm_hub_2.vmf`, SHA-256 `e0c00b92879b6a0acac1106b56d4c6f7cf7242aa26ec2dc4e0cd44b176d9bbae`.
- `Unofficial_Patch/maps/sm_hub_2.bsp`, SHA-256 `88df4bf1d10db9a31f0c01c7491580760a175b6c8ea7f330779262ded479c724`.
- `Unofficial_Patch/python/santamonica/santamonica.py`, SHA-256 `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`.

Выборочно сопоставлены названия целей VMF/BSP; полная геометрия, коллизия, NPC и quest graph Hub 2 не исследованы. Runtime `RUNTIME PENDING`.
