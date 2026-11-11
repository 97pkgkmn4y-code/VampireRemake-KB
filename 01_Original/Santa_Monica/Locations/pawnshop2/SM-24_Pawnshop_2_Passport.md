---
id: SM-24
map: sm_pawnshop_2
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-24 — Trip's Pawnshop, технический паспорт

**Назначение и переходы.** В установленном BSP entity lump 56 entities; именованный NPC `Trip` с `dialogname=dlg/Santa Monica/Trip.dlg`. `talk_to_trip.OnPressed → Trip.StartPlayerDialogRemote`. `exitdoor.OnOpen` вызывает `pawnshopLeave()`; `santamonica.py:1474–1480` выбирает `PawnshopTeleport2` при `Story_State==90`, иначе `PawnshopTeleport1`. Два `trigger_changelevel` в BSP ведут соответственно в `sm_hub_2` и `sm_hub_1`, оба с `landmark=pawnshop1`. Входящие связи — в [[../../Space/Transitions|реестре]]. Тексты условий отделены от фактического выполнения в игре.

**Диалог и зависимости.** `trip.dlg` ID 22–24 содержит отдельные проверки `G.Trip_Know==1/2/3`, с репликами об Arthur, Knox и Mercurio. ID 31 ставит `G.Trip_Know=4`; ID 41 — `G.Trip_Guns=3` и вызывает `TripStoryState()`. Это социальные условия продажи оружия, а не доказательство того, что каждая ветка достижима в одном прохождении. Подробные цепочки Arthur/Knox и Mercurio уже находятся в [[../../Quests/Index|индексе квестов]] и [[../apartment1/SM-16_Apartment_02_Mercurio|SM-16]].

**Источники, SHA-256.** `SDKContent/MapSrc/up sources/sm_pawnshop_2_d.vmf`: `b8d8419d3a74aa90d6bb4190abbef7b8b0556578c53aa0febf84bf0908de2d28`; `Unofficial_Patch/maps/sm_pawnshop_2.bsp`: `0d9f4c62a87d2b3faad5a20889daf2de82c5a3573d067fb2a5c093f78e15ba3a`; `Unofficial_Patch/dlg/santa monica/trip.dlg`: `55a98b20305b51c0bff35337ef3d56d751073ff6702ad8a6fa49885b61aca8e6`; `Unofficial_Patch/python/santamonica/santamonica.py`: `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`. Выборочные entities проверены по BSP; коллизия, торговый ассортимент, условия появления NPC и runtime развилок открыты.
