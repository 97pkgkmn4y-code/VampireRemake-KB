---
id: SM-23
map: sm_tattoo
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-23 — Tattoo Parlor, технический паспорт

**Назначение и переход.** Отдельный интерьер, связанный с поиском Carson/Gimble (см. [[../../Quests/Knox_Quest|Knox]] и [[../basement1/SM-18_Basement_00_Index|SM-18]]). В установленном BSP entity lump 86 entities. `front_door.OnFullyOpen → transition.ChangeNow`; `transition` загружает `sm_hub_1` с `landmark=tattoo`. Обратная связь находится в [[../../Space/Transitions|реестре]]. Геометрический маршрут и доступность двери в игре не проверены.

**Телефон.** Entity `Stan_Gimble` имеет класс `npc_payphone`, `dialogname=dlg/Santa Monica/Stan_Gimble.dlg`; `OnDialogBegin` глушит `phone_ring`, `OnDialogEnd` задаёт `WillTalk(0)`. `phone_test` — `logic_pythoncheck` с `python_script=G.Gimble_Phone==0`, `OnTrue → Stan_Gimble.WillTalk(1)`. В DLG ID 1 записывает `G.Gimble_Phone=1`. Связь условия и dialog статически подтверждена; вызов `phone_test.Test`, порядок звонка и доступность разговора требуют отдельной проверки. Это не доказательство присутствия живого Stan в этом помещении.

**Источники, SHA-256.** `SDKContent/MapSrc/up sources/sm_tattoo_d.vmf`: `b1f0683b5fc60a745c77af4f78d3a381972f8b006ff37e3b94191cb33659c498`; `Unofficial_Patch/maps/sm_tattoo.bsp`: `859b8abfeb0411efc0f063a86baf6139e8498a0775f3d724221fbf29f98eefe3`; `Unofficial_Patch/dlg/santa monica/stan_gimble.dlg`: `54794300b3ef97cb352a4151e3a01493919b89ac12bfde87a639c5e9234d298d`. Выборочные entities проверены в установленном BSP; источником деталей VMF здесь не объявляется полное совпадение BSP/геометрии. Runtime не проводился.
