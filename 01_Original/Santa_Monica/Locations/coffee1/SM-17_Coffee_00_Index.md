---
id: SM-17
map: sm_coffee_1
reference: Unofficial Patch Plus 12.0
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-17 — Coffee Shop

**Сверка UP BSP.** В установленной карте 159 entities, включая `coffee_frontdoor`, `coffee_transition`, `coffee` и `scott_laptop`; класса `npc_*` нет. Сопоставлены имена, типы, назначение перехода, `OnOpen`, координата и файл терминала. Базовый каталог `Vampire/maps` не содержит loose BSP этой карты.

## Что подтверждено локально

- [VMF] `SDKContent/MapSrc/up sources/sm_coffee_1.vmf`: 35515 строк, 264 `entity`, 25 классов, `worldspawn.levelscript=santamonica`, `safearea=0`, комментарий `Created by Wesp5 and improved by Psycho-A`. Структурная выгрузка в `SM-17_Coffee_Assets/vmf-extract.json`.
- [VMF] `coffee_transition` ID 197 ведёт в `sm_hub_1` с landmark `coffee` ID 196; `coffee_frontdoor.OnOpen` ID 6416 вызывает `coffee_transition.ChangeNow`. В `sm_hub_1_d.vmf` обратный `coffee_transition` указывает на `sm_coffee_1` (L179174–179177). Это связь в **исходниках**, не доказанный runtime-переход.
- [VMF] На карте нет NPC-entity; `scott_laptop` ID 7063 `(457.161,101.714,36.006)` имеет `difficulty=4`, `skilltype=2`, `hack_file=Scott_laptop.txt`. Другие I/O карты — общий `unhidePlus()` и события мира/игрока, без собственного NPC-диалога.
- [DATA] `Unofficial_Patch/vdata/hackterminals/scott_laptop.txt`: Journal с паролем `Ankara`; функция Fifth вызывает `G.Library_Coffee=2; librarySetQuest()`. [PY] `vamputil.py:1302–1318` при `Library_Coffee==2 && Library_Open==0` записывает `Library` quest stage 4, `Library_Open=1`, `Library_Coffee=3`. Текст журнала связывает библиотеку, smoke shop, junkyard и Beckett, но содержание записи не доказывает посещения этих мест игроком.
- [VMF] Большие горизонтальные грани Z=0: solid 42 / side 241 X66–420, Y−584…148 и solid 121223 / side 3863 X420–544, Y−321…148. Это опорные геометрические ориентиры, не доказательство проходимости. Отсутствие NPC и единственный значимый терминал делают локацию прежде всего информационным узлом в доступном VMF — [INF], без утверждения о её реализации в установленной игре.

## Доступ и геометрия установленной карты

- `sm_hub_1`: `plus_coffee_door.OnOpen → coffee_transition.ChangeNow`, `map=sm_coffee_1`, `landmark=coffee`. `setPlus()` показывает `plus_*`, скрывает `basic_*` и отдельно запирает `plus_coffee_door` при `Library_Coffee=0`, отпирая при `Library_Coffee>0`. Совмещённая `basic_coffee_door` не имеет выхода на этот переход. См. [[../../Quests/Index#Night at the Library|связь улик]].
- Грани UP BSP у обоих порогов санузлов (1303, 1305), задней двери (1307) и под терминалом (1235) расположены на Z=0. Входная `coffee_frontdoor` и коробка перехода `*3` лежат на стороне Y≈-570. Пороги санузлов находятся к +X от общей входной оси. Состояния замков, связность с задней дверью и геометрия свободного прохода требуют проверки.

**SHA-256.** `Unofficial_Patch/maps/sm_coffee_1.bsp` — `24f6262047cfd00dfc6efe7bf5ba46a0be30d8571f96c398d726820a9d728a84`; `SDKContent/MapSrc/up sources/sm_coffee_1.vmf` — `d92b15508c63d93a565b85150545129f16751b03a97fa0603113f3295def5961`; `Unofficial_Patch/vdata/hackterminals/scott_laptop.txt` — `7f600c3ac9a2f4617e5e757212e4ba219627fb2284d01abc903a80ca56a8e793`. SHA Hub 1 и `vamputil.py` приведены в [[../../Space/Sewers]] и [[../../Quests/Index#Night at the Library|цепи квеста]].
