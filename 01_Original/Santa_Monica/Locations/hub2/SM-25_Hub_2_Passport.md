---
id: SM-25
map: sm_hub_2
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
depth_required: A
---
# SM-25 — Santa Monica Hub 2, предварительный паспорт

`sm_hub_2` — отдельная установленная BSP для позднего состояния района, а не дополнительная область `sm_hub_1`. Из-за смены доступных магазинов, NPC и выходов ей требуется исследование уровня A; текущий паспорт закрывает только ключевые переходы и скриптовые условия.

## Переходы

- В установленном UP BSP есть восемь `trigger_changelevel`: Haven, Pawnshop, Apartment, `ApartmentTeleport1_plus` (`sm_apartment_1b`), taxi/специальные внешние цели; полный список и SHA в [[../../Space/Santa_Monica_BSP_Changelevels.csv|реестре]].
- `apartment_door_left/right.OnFullyOpen` в BSP вызывают `ApartmentTeleport1.ChangeNow` с `map=sm_apartment_1`. Для `ApartmentTeleport1_plus` прямого I/O вызова в этом entity lump не найдено. `sm_apartment_1b` отсутствует среди 22 loose BSP; проверка VPK индексов ранее также не обнаружила цель ([[../../../../KNOWLEDGE_BASE_AUDIT|аудит]]). Это `TARGET_NOT_FOUND_IN_CHECKED_SOURCES`, достижимость `UNVERIFIED`.
- `apartmentLeave()` (`santamonica.py:25–29`) отправляет из Apartment к `ApartmentTeleport2` в Hub 2 при `Story_State==90 && Credits_Running==0`, иначе к Hub 1. `pawnshopLeave()` (L1474–1479) выбирает `PawnshopTeleport2` при `Story_State==90`. Это внешние Python-переходы к позднему району; прямого `trigger_changelevel` Hub 1 ↔ Hub 2 в проверенных BSP нет.

## Состояние при загрузке

`logic_auto.OnMapLoad` в BSP вызывает `openShops()`, `bloodHuntClanCheck()`, `unhidePlus()`; конкретное выполнение в игре не проверено. `openShops()` (`santamonica.py:688–713`) отпирает `trips_door`, если Trip не мёртв; отпирает две apartment doors, если Mercurio жив и `G.Mercurio_Attack==0`; может показать Knox при `Knox_Pissed>0` и Mercurio при `Mercurio_Attack==1 && Prince_Mercurio==0`. Наличие NPC в карте и условия скрипта не доказывают их фактическое появление в каждом состоянии.

## Источники и ограничения

- `SDKContent/MapSrc/up sources/sm_hub_2.vmf`, SHA-256 `e0c00b92879b6a0acac1106b56d4c6f7cf7242aa26ec2dc4e0cd44b176d9bbae`.
- `Unofficial_Patch/maps/sm_hub_2.bsp`, SHA-256 `88df4bf1d10db9a31f0c01c7491580760a175b6c8ea7f330779262ded479c724`.
- `Unofficial_Patch/python/santamonica/santamonica.py`, SHA-256 `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`.

Выборочно сопоставлены названия целей VMF/BSP; полная геометрия, коллизия, NPC и quest graph Hub 2 не исследованы. Runtime `RUNTIME PENDING`.
