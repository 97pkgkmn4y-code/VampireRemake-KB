# Santa Monica — реестр загрузочных переходов UP Plus 12.0

В установленном каталоге `Unofficial_Patch/maps/` найдены ровно 22 файла `sm_*.bsp`, совпадающие по именам с матрицей [[../../../KNOWLEDGE_BASE_AUDIT|аудита]]. Из их **установленных BSP entity lump** извлечены 65 entities класса `trigger_changelevel`. Их реестр: [[Santa_Monica_BSP_Changelevels.csv]]. Каждая строка содержит исходную/целевую карту, имя entity, landmark, I/O ссылки на эту entity из той же BSP, SHA-256 BSP и статус `RUNTIME PENDING`. Ссылки включают `ChangeNow`, а также действия вроде `ScriptUnhide`; последние лишь меняют видимость и сами по себе не загружают карту.

Метод: VBSP v17, entity lump с offset/length в заголовке; из каждой entity взяты `classname`, `targetname`, `map`, `landmark` и выходы `On*`, направленные на имя перехода. `referencing_events` сохраняет конкретный input, поэтому `ChangeNow` и `ScriptUnhide` различимы. Совпадение имени и input `ChangeNow` доказывает сохранённую I/O связь, **не** фактическое выполнение. Поле `[not identified in entity I/O]` означает лишь, что прямой выход из entity lump не найден: возможны touch, Python `ChangeMap` и другие механизмы. `availability_condition=UNVERIFIED` не является утверждением, что карта всегда доступна.

## Каркас района по статическим целям

```mermaid
flowchart LR
  H[sm_hub_1] <--> A[Asylum / Medical / Diner / Bail Bonds / Gallery]
  H <--> AP[sm_apartment_1]
  H <--> B[Pawnshops / Coffee / Smoke / Tattoo / Shreknet / Arena / Junkyard]
  H <--> P[sm_pier_1]
  P <--> BH[sm_beachhouse_1]
  H <--> O1[sm_oceanhouse_1]
  O1 <--> O2[sm_oceanhouse_2]
  H <--> W[sm_warehouse_1]
  AP <--> H2[sm_hub_2: late-state route]
```

Диаграмма объединяет имена целей; она не описывает условия, этажи, коллизию и достижимость каждого ребра. `sm_hub_2` также содержит назначение `sm_apartment_1b`, отсутствующее среди 22 loose BSP; ранее проверенные VPK индексы не выявили его ([[../../../KNOWLEDGE_BASE_AUDIT|аудит]]). Это `TARGET_NOT_FOUND_IN_CHECKED_SOURCES`, а не доказательство невозможности загрузки.

## Связи, уже разобранные детально

- Ocean House: [[../Locations/oceanhouse/SM-20_Ocean_House_01_Spatial|SM-20 spatial]] и [[Sewers|канализация B7]].
- Warehouse: [[../Locations/warehouse/SM-21_Warehouse_01_Systems|SM-21 systems]]; вход через Bertram зависит от DLG, Python и I/O, поэтому в CSV для `warehouseteleport` прямой entity activator не показан.
- Apartment и поздний Hub: [[../Locations/apartment1/SM-16_Apartment_00_Index|SM-16]].

## Способы активации и выбор маршрута

После повторного извлечения entity lump подтвердились все 65 кортежей `source_map / target_map / transition_entity / landmark / bsp_sha256`. У каждого перехода с целью среди 22 Santa Monica BSP на целевой карте есть `info_landmark` с указанным именем при сравнении без учёта регистра. Для четырёх записей нет loose BSP назначения: две цели `taxi` (Hub 1/2), одна `sewer_map` (Hub 1), одна `sm_apartment_1b` (Hub 2). Только для последней проведена и ранее документирована проверка индексов VPK.

| Узел и направление | Связь в установленных данных |
|---|---|
| Hub 1 ↔ Hub 2 через интерьеры | `apartmentLeave()` выбирает Hub 2 при `Story_State==90 && Credits_Running==0`, `pawnshopLeave()` при `Story_State==90`. [[../Locations/pawnshop1/SM-29_Pawnshop_1_Passport\|Haven]] при State=90 переключает выход в Hub 2. У обратной двери в [[../Locations/hub2/SM-25_Hub_2_Passport\|Hub 2]] обнаружено несовпадение `HavenTeleport1/2`. |
| Hub 1 ↔ специализированные двери | Ключи на ручках: Foxy Boxes `item_k_gimble_key`, ShreckNet `item_k_shrekhub_one_key`, Tattoo `item_k_tatoo_parlor_key`. Для Coffee и Smoke дверь с I/O показывает `setPlus()`; Coffee дополнительно проверяет `Library_Coffee>0`. Состояния замков см. в [[../Locations/Index\|паспортах карт]]. |
| Pier ↔ Beach House | На Pier скрытый переход показывается touch-триггером. Ворота имеют отдельное условие Mercurio, см. [[Surface]]. |
| Канализация | A1–B3 используют парные внутрикартовые `point_teleport`; B7 вызывает загрузку Ocean House. Замок, вертикальная связь и карта мира описаны в [[Sewers]]. |
| Специальные переходы | [[../Locations/pawnshop1/SM-29_Pawnshop_1_Passport\|Haven → sp_taxiride]] через `havenTaxiCheck()`. В [[../Locations/oceanhouse/SM-20_Ocean_House_01_Spatial\|Ocean House 2]] комнаты связываются `trigger_teleport` в обе стороны. Эти действия требуют иной активации, чем обычный touch `trigger_changelevel`. |

## Открытая часть реестра

CSV охватывает `trigger_changelevel` только в 22 установленных BSP. Для полноценного графа ещё нужны входы из Python `ChangeMap`, внутрикартовые телепорты, двери/блокировки, условия DLG и runtime-проверка направлений. Поэтому этот реестр имеет статус `PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING` и не делает район готовым к реализации всей RPG.
