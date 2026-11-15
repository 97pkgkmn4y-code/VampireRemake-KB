---
id: SM-22
map: sm_shreknet_1
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-22 — ShreckNet hub, технический паспорт

**Назначение.** Небольшая отдельная карта с компьютером `shrek_hub`; он связан с заданием Mitnick. В установленном UP Plus 12.0 BSP entity lump 70 entities. `shreknetdoor.OnFullyOpen → shreknetexit.ChangeNow`; `shreknetexit` ведёт в `sm_hub_1` с `landmark=shreknetoutside`. Вход из Hub зафиксирован в [[../../Space/Transitions|реестре переходов]]. Runtime перехода не проверен.

**Доступ.** В `sm_hub_1` электронная ручка `shreknetdoor` требует `item_k_shrekhub_one_key` и имеет `difficulty=1`. Письмо Mitnick в [[../pawnshop1/SM-29_Pawnshop_1_Passport|убежище]] устанавливает `Shubs_Email=1`, вызывает `mitSetQuestTwo()` и `putStuffInMailBox()`. Последняя при `Shubs_Email_Read<1` кладёт ключ в ящик и записывает `Shubs_Email_Read=1`.

**Взаимодействия.** `shrek_hub` — `prop_hacking` с `hack_file=vdata/HackTerminals/shrekhub1_terminal.txt`, `difficulty=3`, `skilltype=2`, `StartHidden=1`. `shreknetbreaker.OnActivate → lights_on.Trigger` включает свет, показывает `shrek_hub` и скрывает декоративный `shrek_hub_dark`. `OnDeactivate → lights_off.Trigger` меняет состояния обратно. У переключателя есть отдельные выходы на skin лампы и audio relays. Терминальный файл содержит `dependency=G.Shubs_Act==0`, `trigger=0`, `runscript=mitSetQuestThree()`. В BSP `shrek_hub.OnTrigger0` записывает `G.Shubs_Act=1`; `vamputil.py:4103–4105` ставит журнал `Mitnick=3`. Декоративная копия сохраняет такой же `OnTrigger0`, но относится к классу `prop_dynamic`. Порядок terminal script и I/O требует runtime-проверки.

**Планировочные опоры UP BSP.** Входная дверь `(-472.5,-894.5,-58)`, `locked_door` у `(-723.5,-636.5,-57)`, распределительный узел с breaker `(-717,-547,-40.8)`, дальние двери `door1` и `door2` на Y=-275.5 и терминал `(-690,-145,-73)`. У входа, обеих дальних дверей, `locked_door` и под терминалом горизонтальные world faces на Z=-112 (121, 127, 124, 125 и 114 соответственно). Проверить связность маршрута и замок каждой двери в игре.

**Источники, SHA-256.** `SDKContent/MapSrc/up sources/sm_shreknet_1_d.vmf`: `dcf0dc8b66e801204d7e8da0b142d759ea5653a6580d7d4e3d439f5117125da4`; `Unofficial_Patch/maps/sm_shreknet_1.bsp`: `38f581af277567b0f7d2207294ec7921c847029abb43ef1da69ecc7b0d7d8656`; `Unofficial_Patch/vdata/HackTerminals/shrekhub1_terminal.txt`: `2b2b6b9131b3d67e34d856dc9335758da01213557386ae216764c4f29d4e30dc`; `Unofficial_Patch/python/vamputil.py`: `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491`. Именованные переход, терминал и breaker проверены в BSP; полного сравнения VMF/BSP и геометрии нет. Достижимость и сцена не проверены в игре.
