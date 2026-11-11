---
id: SM-16
map: sm_apartment_1
reference: Unofficial Patch Plus
status: SOURCE COMPLETE / RUNTIME PENDING
---
# SM-16 — Santa Monica Apartment (Mercurio)

**Статус: SOURCE COMPLETE / RUNTIME PENDING.** Статическое исследование основных локально доступных источников завершено. Движковые вопросы отделены в [[SM-16_Apartment_03_Analysis]].

- [[SM-16_Apartment_01_Spatial|01 — Пространство и карта]]
- [[SM-16_Apartment_02_Mercurio|02 — Mercurio, DLG, квесты и предметы]]
- [[SM-16_Apartment_03_Analysis|03 — Причинная схема, анализ и вопросы]]

![[SM-16_Apartment_Assets/SM-16_Apartment_Plan.png]]

## Проверенные источники

Корень эталонной установки для путей ниже: `C:/Users/Slava/Documents/Bloodlines-GLM/Reference/Vampire - The Masquerade Bloodlines/`. Указанные пути отсчитываются от этого корня, а вложения `SM-16_Apartment_Assets/` — от папки данной заметки.

- [VMF] `SDKContent/MapSrc/up sources/sm_apartment_1.vmf`: 229 блоков `entity`, 43 класса, `worldspawn.levelscript=santamonica`, `safearea=2`. Структурная выгрузка верхних граней и сущностей в `SM-16_Apartment_Assets/vmf-extract.json`.
- [BSP] Установленная `Unofficial_Patch/maps/sm_apartment_1.bsp`: VBSP v17, 189 сущностей в entity lump. Восемь выбранных имён/классов/origin (Mercurio, оба выхода, landmark, Carson_Computer, journal, angry trigger и trunk lock) совпали с VMF. Это выборочная сверка, не доказательство полной идентичности геометрии.
- [PY] `Unofficial_Patch/python/santamonica/santamonica.py` L24–137 содержит `apartmentLeave`, `carsonComputerHacked`, `finishElysiumTip`, `journalPickup`, `updateMercurioModel`, `mercurioCamera`, `mercurioDeath`, `mercurioDialog`, `mercurioFight`.
- [DLG] `Unofficial_Patch/dlg/santa monica/mercurio.dlg`: 1026 нумерованных строк сохранены как исходные поля в `SM-16_Apartment_Assets/SM-16_Dialogue_Rows.csv`. Начальные условия, важные записи и явные переходы разобраны в [[SM-16_Apartment_02_Mercurio]]; динамическая достижимость не симулировалась.
- [DATA] `Unofficial_Patch/vdata/hackterminals/Carson_Computer.txt`: меню McGee, пароль `Imalia`, функция Location вызывает `carsonComputerHacked()` и сообщает о tattoo parlor; `santamonica.py` L31–36 повышает `Arthur Knox` до стадии 2 только при исходной стадии 1.

## Уже установленная логика [VMF/PY]

| Узел | Условие → действие | Источник |
| --- | --- | --- |
| Выход | `exitdoor1/2.OnOpen → apartmentLeave()`. При `Story_State==90 && Credits_Running==0` вызывается `ChangeMap` к `ApartmentTeleport2` / `sm_hub_2`, иначе к `ApartmentTeleport1` / `sm_hub_1`. | VMF doors IDs 483/481, changelevels 617/511; PY L25–29. |
| Mercurio | На загрузке `mercurioFight()`, `finishElysiumTip()`, `updateMercurioModel()`; при Astrolite stage 5 показываются journal и angry talk trigger, NPC переносится и меняет поведение. | VMF logic_auto IDs 515/619; PY L38–137. |
| Journal | `mercurio_journal.OnPlayerPickup → journalPickup()`; только при `Mercurio_Quest<2` ставятся `Warehouse=6`, `Astrolite=7`, `Mercurio_Quest=2`. | VMF ID 609; PY L68–74. |
| Состояние помещения | `finishElysiumTip()` при Plus и `Carson_Rescued==1` удаляет компьютер/плакат/устройства; при `Story_State>=15 && Patch_Plus==1 && Level_Clean==0` меняет кровавую сценографию на прибранную. | PY L38–66; соответствующие `targetname` в VMF. |

## Остаточные вопросы

Планы, диалоги, предметы, дверные узлы и оба выхода документированы. Открыты коллизии, электронные замки, динамический приоритет DLG и постановка `mercurioCamera()`. Для `sm_apartment_1b` результат проверки — `TARGET_NOT_FOUND_IN_CHECKED_SOURCES`; детали в [[SM-16_Apartment_03_Analysis]].
