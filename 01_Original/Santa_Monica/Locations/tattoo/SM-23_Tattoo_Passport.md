---
id: SM-23
map: sm_tattoo
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-23 — Tattoo Parlor, технический паспорт

**Назначение и переход.** Отдельный интерьер, связанный с поиском Carson/Gimble (см. [[../../Quests/Knox_Quest|Knox]] и [[../basement1/SM-18_Basement_00_Index|SM-18]]). В установленном BSP entity lump 86 entities. `front_door.OnFullyOpen → transition.ChangeNow`; `transition` загружает `sm_hub_1` с `landmark=tattoo`. Обратная связь находится в [[../../Space/Transitions|реестре]]. Геометрический маршрут и доступность двери в игре не проверены.

**Геометрия и доступ.** В `sm_hub_1` электронная ручка `tattoodoor` имеет `key_name=item_k_tatoo_parlor_key` и `difficulty=1`. В интерьере грани world model 635, 634 и 606 лежат на Z=32 у входа, в средней зоне и перед телефоном. Brush entity `basic_phone_ring_trigger` (`*3`) охватывает X=108…520, Y=176…220, до Z≈65. Origin телефона Z=-96 относится к entity `npc_payphone`; находящаяся выше грань пола остаётся на Z=32.

**Телефон.** `Stan_Gimble` имеет класс `npc_payphone`, использует `dlg/Santa Monica/Stan_Gimble.dlg`. `OnDialogBegin` убирает `basic_phone_ring_trigger` и глушит звук `phone_ring`, `OnDialogEnd` задаёт `WillTalk(0)`. В DLG ID 1 записывает `G.Gimble_Phone=1`. BSP сохраняет две управляющие ветви.

- Basic: map-load включает `basic_phone_ring_trigger` и выключает разговор. Touch запускает звонок и `WillTalk(1)`. Дополнительный delayed `Disable` адресован `phone_ring_trigger`; точного имени цели среди entities установленной карты нет.
- Plus: `setPlus()` раскрывает `plus_note` и `plus_noteinspection`, скрывая `basic_*`. Чтение `Unofficial_Patch/vdata/Signs/tattoo_note.txt` (SHA-256 `b4062ce14fa157b0e14c7f71966965f9e3e2b81fe0e5e8541fb4988e7299eb7e`) через `plus_note.OnReadBegin` убирает подсветку, `OnReadEnd → phone_test.Test`. При `G.Gimble_Phone == 0` тест включает `WillTalk(1)` без явного выхода на звонок. Открыты фактический эффект скрытия Basic-триггера и переход к диалогу.

**Источники, SHA-256.** `SDKContent/MapSrc/up sources/sm_tattoo_d.vmf`: `b1f0683b5fc60a745c77af4f78d3a381972f8b006ff37e3b94191cb33659c498`; `Unofficial_Patch/maps/sm_tattoo.bsp`: `859b8abfeb0411efc0f063a86baf6139e8498a0775f3d724221fbf29f98eefe3`; `Unofficial_Patch/dlg/santa monica/stan_gimble.dlg`: `54794300b3ef97cb352a4151e3a01493919b89ac12bfde87a639c5e9234d298d`. Выборочные entities проверены в установленном BSP; источником деталей VMF здесь не объявляется полное совпадение BSP/геометрии. Runtime не проводился.
