---
id: SM-14
title: Santa Monica Medical Clinic — index
game: Vampire The Masquerade Bloodlines (2004)
reference: Unofficial Patch Plus
map: sm_medical_1
status: SOURCE COMPLETE / RUNTIME PENDING
---
# SM-14 — Santa Monica Medical Clinic

## Исследование

- [[SM-14_Medical_01_Spatial|01 — Пространство и координатные планы]]
- [[SM-14_Medical_02_Systems|02 — Сущности и системы доступа]]
- [[SM-14_Medical_03_Quests|03 — Скрипты, диалоги и квестовые зависимости]]
- [[SM-14_Medical_04_Analysis|04 — Дизайн и открытые вопросы]]

## Источники и границы

Основной источник [VMF] — `Reference/Vampire - The Masquerade Bloodlines/SDKContent/MapSrc/up sources/sm_medical_1.vmf` (117900 строк, `worldspawn.levelscript=santamonica`, комментарий UP); [BSP] — установленная `Unofficial_Patch/maps/sm_medical_1.bsp`; [PY] — `Unofficial_Patch/python/santamonica/santamonica.py` и `Unofficial_Patch/python/vamputil.py`; [DLG] — `Unofficial_Patch/dlg/santa monica/{clinic_guard,nurse,malcolm,phil,lily,vandal}.dlg`; [DATA] — терминалы `Unofficial_Patch/vdata/hackterminals/clinic_*.txt`. Сверены 16 ключевых `targetname`, классов и origin между VMF и entity lump установленной BSP; все выбранные пары совпали. Это поддерживает применимость исследованных сущностей к установленной версии, но не подтверждает равенство всей геометрии и runtime-состояний. Проверка в запущенной игре не проводилась.

Структурный парсер `SM-14_Medical_Assets/extract-vmf.js` сохранил `vmf-extract.json`: 1236 блоков `entity`, 75 классов, 732 горизонтальные верхние грани и 320 сечений брашей на трёх выбранных отметках. Многоугольники получены пересечением **всех** плоскостей соответствующего выпуклого браша. Это не утверждение о 732 доступных полах. `SM-14_Medical_Assets/compare-bsp.js` воспроизводит выборочную сверку BSP; `extract-dialogue.js` сохраняет 1401 строку шести DLG в `SM-14_Dialogue_Rows.csv` без выдуманных переходов по соседству.

![[SM-14_Medical_Assets/SM-14_Medical_Ground.png]]

Планы: [[SM-14_Medical_Assets/SM-14_Medical_Basement.svg|подвал]], [[SM-14_Medical_Assets/SM-14_Medical_Ground.svg|первый этаж]], [[SM-14_Medical_Assets/SM-14_Medical_Upper.svg|верхний этаж]]. Для каждого есть PNG. **SOURCE COMPLETE:** основные локально доступные VMF, установленная BSP entity lump, Python, шесть DLG и шесть связанных терминалов исследованы для основных пространственных и игровых систем. **RUNTIME PENDING:** проходимость, приоритет диалоговых условий и выполнение отдельных I/O не наблюдались в игре; перечень в [[SM-14_Medical_04_Analysis]].

Связанный контекст: [[SM-13_Asylum_00_Index|The Asylum]] и [[Surface|Santa Monica surface]].
