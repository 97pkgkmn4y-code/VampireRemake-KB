---
id: SM-18
map: sm_basement_1
reference: Unofficial Patch Plus
status: SOURCE COMPLETE / RUNTIME PENDING
---
# SM-18 — Gimble basement / Carson

**SOURCE COMPLETE / RUNTIME PENDING.** Статическая цепь VMF → Python → DLG и два основных уровня восстановлены. Проходимость конкретной лестницы, исполнение scripted sequences и семантика движкового `Kill → OnDeath` остаются вопросами runtime; основной квестовый результат имеет отдельные подтверждённые источники в обеих ветках.

## Разделы

- [[SM-18_Basement_01_Spatial]] — опорные грани, двери, уровни и координатная схема.
- [[SM-18_Basement_02_Systems]] — I/O, Python, диалоги и состояния.
- [[SM-18_Basement_03_Analysis]] — причинная цепь, ветки Plus, границы доказательства.
- [Схема SVG](SM-18_Basement_Assets/SM-18_Basement_Levels.svg) · [PNG](SM-18_Basement_Assets/SM-18_Basement_Levels.png).

## Источники и сверка

- [VMF] `Reference/Vampire - The Masquerade Bloodlines/SDKContent/MapSrc/up sources/sm_basement_1.vmf`, 100952 строк, 552 entity-блока; `worldspawn.levelscript=santamonica`, `safearea=0`. Структурно восстановленные полигоны и I/O: `SM-18_Basement_Assets/vmf-extract.json`.
- [DATA] Установленный `Unofficial_Patch/maps/sm_basement_1.bsp`: VBSP v17; entity lump содержит 273 сущности. Сопоставлены семь якорей VMF/BSP: Stan, Carson, `BasementTeleport1`, landmark, `carson_switch`, `Carson prot brush`, `gimble_dead_relay`. Это выборочная сверка, не полное тождество геометрии.
- [PY] `Unofficial_Patch/python/santamonica/santamonica.py:411–424`.
- [DLG] `Unofficial_Patch/dlg/Santa Monica/{Stan_Gimble,Carson}.dlg`: 285 и 114 нумерованных строк; индекс `SM-18_Basement_Assets/SM-18_Dialogue_Rows.csv`.

## Открытые проверки

- [HYP] Фактические коллизии лестницы и дверей, начало/конец scripted sequences, доступность взаимодействия с Carson и то, вызывает ли `Kill` событие смерти, требуют наблюдения в игре. [DLG] В Plus ветке Carson IDs 13/14 отдельно ставят `G.Gimble_Dead=1` и `Arthur Knox=3`; [VMF] `gimble_attack_check` OnFalse явно вызывает `gimble_dead_relay.Trigger`, поэтому отсутствие доказанного `Kill → OnDeath` не оставляет условный квестовый исход без статической цепи.
- [INF] Связь выхода с `sm_hub_1` подтверждается `trigger_changelevel` ID 951 и `leveldoor` ID 948; обратный вход и загрузка landmark требуют проверки со стороны hub.
