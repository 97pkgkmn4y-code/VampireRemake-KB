---
id: SM-17
map: sm_coffee_1
reference: Unofficial Patch Plus SDK source
status: PARTIAL; RUNTIME PENDING; BSP/VMF comparison pending
---
# SM-17 — Coffee Shop: исходник и UP+ BSP (сверка pending)

**PARTIAL; RUNTIME PENDING; BSP/VMF comparison pending.** `Unofficial_Patch\maps\sm_coffee_1.bsp` найден (1752312 B, 22.01.2026); базовый `Vampire\maps` его не содержит (карта UP+). Статическая сверка BSP entity lump с VMF — следующий шаг. До её завершения наличие перехода в VMF само по себе не доказывает, что карта загружается в установленной игре (RUNTIME PENDING).

## Что подтверждено локально

- [VMF] `SDKContent/MapSrc/up sources/sm_coffee_1.vmf`: 35515 строк, 264 `entity`, 25 классов, `worldspawn.levelscript=santamonica`, `safearea=0`, комментарий `Created by Wesp5 and improved by Psycho-A`. Структурная выгрузка в `SM-17_Coffee_Assets/vmf-extract.json`.
- [VMF] `coffee_transition` ID 197 ведёт в `sm_hub_1` с landmark `coffee` ID 196; `coffee_frontdoor.OnOpen` ID 6416 вызывает `coffee_transition.ChangeNow`. В `sm_hub_1_d.vmf` обратный `coffee_transition` указывает на `sm_coffee_1` (L179174–179177). Это связь в **исходниках**, не доказанный runtime-переход.
- [VMF] На карте нет NPC-entity; `scott_laptop` ID 7063 `(457.161,101.714,36.006)` имеет `difficulty=4`, `skilltype=2`, `hack_file=Scott_laptop.txt`. Другие I/O карты — общий `unhidePlus()` и события мира/игрока, без собственного NPC-диалога.
- [DATA] `Unofficial_Patch/vdata/hackterminals/scott_laptop.txt`: Journal с паролем `Ankara`; функция Fifth вызывает `G.Library_Coffee=2; librarySetQuest()`. [PY] `vamputil.py:1177–1194` при `Library_Coffee==2 && Library_Open==0` записывает `Library` quest stage 4, `Library_Open=1`, `Library_Coffee=3`. Текст журнала связывает библиотеку, smoke shop, junkyard и Beckett, но содержание записи не доказывает посещения этих мест игроком.
- [VMF] Большие горизонтальные грани Z=0: solid 42 / side 241 X66–420, Y−584…148 и solid 121223 / side 3863 X420–544, Y−321…148. Это опорные геометрические ориентиры, не доказательство проходимости. Отсутствие NPC и единственный значимый терминал делают локацию прежде всего информационным узлом в доступном VMF — [INF], без утверждения о её реализации в установленной игре.

## Что мешает закрыть SOURCE COMPLETE

1. **RESOLVED (2026-11-10):** UP+ `sm_coffee_1.bsp` найден (1752312 B); следующий шаг — статическая сверка BSP entity lump с VMF (base `Vampire\maps` карту не содержит — она UP+-специфична).
2. **CROSS-LOCATION:** проверить условия входной двери `sm_hub_1` и дальнейшее использование `Library_Open` при исследовании smoke shop / library.
3. **RUNTIME:** если BSP найден, проверить загрузку карты и работу `Scott_laptop` в игре; DLG для этой VMF отсутствуют, NPC-entity не обнаружены.

BSP найден — продолжать отсюда (сверка entity lump), не повторяя VMF/DATA/Python-разбор.
