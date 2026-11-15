---
id: SM-22
map: sm_shreknet_1
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-22 — ShreckNet hub, технический паспорт

**Назначение.** Небольшая отдельная карта с компьютером `shrek_hub`; он связан с заданием Mitnick. В установленном UP Plus 12.0 BSP entity lump 70 entities. `shreknetdoor.OnFullyOpen → shreknetexit.ChangeNow`; `shreknetexit` ведёт в `sm_hub_1` с `landmark=shreknetoutside`. Вход из Hub зафиксирован в [[../../Space/Transitions|реестре переходов]]. Runtime перехода не проверен.

**Взаимодействия.** `shrek_hub` — `prop_hacking` с `hack_file=vdata/HackTerminals/shrekhub1_terminal.txt`, `difficulty=3`, `skilltype=2`, `StartHidden=1`. Терминальный файл содержит `dependency=G.Shubs_Act==0`, `trigger=0`, `runscript=mitSetQuestThree()`. В BSP `shrek_hub.OnTrigger0` записывает `G.Shubs_Act=1`; `vamputil.py:4103–4105` ставит журнал `Mitnick=3`. Порядок терминального script и I/O и доступность скрытого компьютера требуют runtime проверки. `shreknetbreaker.OnActivate/OnDeactivate` переключает light/audio relays; это локальная система освещения, не доказанное условие квеста.

**Источники, SHA-256.** `SDKContent/MapSrc/up sources/sm_shreknet_1_d.vmf`: `dcf0dc8b66e801204d7e8da0b142d759ea5653a6580d7d4e3d439f5117125da4`; `Unofficial_Patch/maps/sm_shreknet_1.bsp`: `38f581af277567b0f7d2207294ec7921c847029abb43ef1da69ecc7b0d7d8656`; `Unofficial_Patch/vdata/HackTerminals/shrekhub1_terminal.txt`: `2b2b6b9131b3d67e34d856dc9335758da01213557386ae216764c4f29d4e30dc`; `Unofficial_Patch/python/vamputil.py`: `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491`. Именованные переход, терминал и breaker проверены в BSP; полного сравнения VMF/BSP и геометрии нет. Достижимость и сцена не проверены в игре.
