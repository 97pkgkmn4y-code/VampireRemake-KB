---
id: SM-15
map: sm_diner_1
reference: Unofficial Patch Plus
status: SOURCE COMPLETE / RUNTIME PENDING
---
# SM-15 — Santa Monica Diner

- [[SM-15_Diner_01_Spatial|01 — Пространство и карта]]
- [[SM-15_Diner_02_Systems|02 — Засада, NPC и диалоги]]
- [[SM-15_Diner_03_Analysis|03 — Квестовые связи, интерпретация и вопросы]]

![[SM-15_Diner_Assets/SM-15_Diner_Plan.png]]

## Паспорт источников

- [VMF] `Reference/Vampire - The Masquerade Bloodlines/SDKContent/MapSrc/up sources/sm_diner_1.vmf`: 27224 строки, `worldspawn.levelscript=santamonica`, 345 `entity`, 41 класс.
- [BSP] `Reference/Vampire - The Masquerade Bloodlines/Unofficial_Patch/maps/sm_diner_1.bsp`: VBSP v17, 161 сущность в entity lump. Девять ключевых `targetname`/классов/origin выборочно совпали с VMF (см. `SM-14_Medical_Assets/compare-bsp.js`). Это не доказывает побайтовое совпадение геометрии.
- [PY] `Unofficial_Patch/python/santamonica/santamonica.py` L1084–1232; `Unofficial_Patch/python/vamputil.py` L1037–1054.
- [DLG] `Unofficial_Patch/dlg/santa monica/{doris,thug,killer}.dlg`. Исходные поля 447 нумерованных строк сохранены в `SM-15_Diner_Assets/SM-15_Dialogue_Rows.csv`; числовые ссылки не дополнены предположениями о соседних ответах.
- [VMF] `sm_hub_1_d.vmf` содержит обратный переход `DinerTeleport1` в `sm_diner_1` (около L137767).

**SOURCE COMPLETE:** основные доступные локальные источники для геометрии, засады, социальных веток, Doris, Killer, Lily's purse и перехода к городу исследованы. **RUNTIME PENDING:** точная динамическая достижимость DLG, коллизия и игровые последовательности не наблюдались. Статические цепочки не равны гарантированному прохождению.
