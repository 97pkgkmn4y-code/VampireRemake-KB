---
id: SM-16-MERCURIO
map: sm_apartment_1
---
# SM-16.02 — Mercurio: диалог, квесты, изменения пространства

Источник [DLG] — `Unofficial_Patch/dlg/santa monica/mercurio.dlg` относительно корня эталона в [[SM-16_Apartment_00_Index]]. Все 1026 нумерованных строк и их исходные поля 4–6 находятся в `SM-16_Apartment_Assets/SM-16_Dialogue_Rows.csv`. Указанные далее переходы — явные числовые цели DLG. Порядок выбора среди пересекающихся стартовых условий и соседние ответные строки не реконструированы движковым тестом.

## Входные условия

| DLG-слоты | Условие → целевой узел | Смысл условия, не гарантированный результат |
| --- | --- | --- |
| 1007–1008 | `Credits_Running==1 → 521`; `Astrolite` stage 5 `→911` | Финальное состояние и конфликт Astrolite. |
| 1009–1016 | Точные `Story_State` 125/120/115/110/105/100 и пороги ≥75/≥65; флаги `Mercurio_Anarch/Traitor/Dragon/Flame`; 1015 требует `Patch_Plus==1` | Поздние варианты после смены сюжетной роли. |
| 1017–1023 | `Mercurio_Friend==1 →521`; пороги Story 55/45/35/25 и флаги `Mgun/Swat/Spas/Fix`; `Mercurio_Deal==1 →481`; `Story_State>=10 →961` | Условия пересекаются, приоритет движка здесь не доказан. |
| 1024–1026 | `Mercurio_Quest==2 →151`; `Mercurio_Quest==1 →311`; `npc.times_talked==1 →1` | Ранние этапы задания. |

## Причинные узлы [DLG + PY + VMF]

- [DLG] ID 1 ставит квест `Mercurio=2`; ID 121 `G.Mercurio_Quest=1` и `Astrolite=1`. ID 171 ставит `Mercurio_Quest=2`, `Mercurio_Astro=2`, `Astrolite=3`. ID 851/891 — `Astrolite=4`, `Mercurio_Quest=1`. Эти записи нельзя объединять в единую обязательную линейную последовательность: разные входы и условия находятся в одном DLG.
- [PY] `journalPickup()` L69–74 при `Mercurio_Quest<2` записывает `Warehouse=6`, `Astrolite=7`, `Mercurio_Quest=2`; [VMF] `mercurio_journal.OnPlayerPickup` ID 609 вызывает её и отдельно пишет `G.Journal_Taken=1` (L33602 и далее). Предмет активируется в `mercurioFight()` только при Astrolite stage 5.
- [DLG] ID 161 при выборе даёт Humanity +1, `Mercurio_Aid=1` и опыт `Astro03`; ID 939 ставит `Mercurio_Attack=1` при `Story_State<100`. [VMF] `Mercurio.OnDialogEnd → mercurioDialog()` (ID 514); [PY] L112–118 при `Mercurio_Attack==1` переводит безопасную зону в 0 и делает NPC враждебным. `Mercurio.OnDeath → mercurioDeath()` устанавливает `Mercurio_Dead=1` и при Astrolite stage 5 записывает stage 6 (PY L101–110).
- [DLG] ID 961 записывает `Mercurio_Deal=1`, `Mercurio_Combat=0`; ID 661 ставит `Mgun=1`, `Friend=1`; ID 671/691 ставят `Traitor/Anarch=1` и `Friend=0`. Эти поздние записи меняют доступность стартовых веток, но их игровой порядок не следует из одного списка строк.
- [PY] `updateMercurioModel()` L76–91 скрывает Mercurio при `5<=Story_State<15`, возвращает и переносит при `Story_State>=15 && Prince_Mercurio==0`, либо убивает при `Prince_Mercurio`. `finishElysiumTip()` L39–66 при `Patch_Plus==1 && Carson_Rescued==1` удаляет найденные объекты Carson; отдельная ветка при `Story_State>=15 && Patch_Plus==1 && Level_Clean==0` меняет кровавую обстановку на прибранную и ставит `Level_Clean=1`. Перед этими проверками функция при `Elysium_Tip==1` восстанавливает `Story_State` из `Story_State_Save`. [VMF] `logic_auto` IDs 515/619 запускают эти проверки при загрузке.

## Виды изменений состояния

| Вид | Подтверждённые примеры | Основание |
| --- | --- | --- |
| Записи журнала | `pc.SetQuest("Mercurio",2)`, `pc.SetQuest("Astrolite",1/3/4/7)`, `pc.SetQuest("Warehouse",6)` и условный `Arthur Knox=2` | DLG 1/121/171/851/891; `journalPickup()` L69–74; `carsonComputerHacked()` L31–36 |
| Глобальные переменные | `G.Mercurio_Quest`, `G.Mercurio_Astro`, `G.Mercurio_Aid`, `G.Mercurio_Attack`, `G.Journal_Taken`, `G.Key_Taken`, `G.Trunk_Opened`, `G.Level_Clean` | DLG 121/161/171/939; VMF события предметов и замка; PY L53–74 |
| Локальные действия NPC и объектов | Скрытие/показ и смена модели Mercurio, телепорт, расписание и враждебность | `updateMercurioModel()`, `mercurioFight()`, `mercurioDialog()` L76–91, L112–137 |
| Предметы и окружение | Показ journal и его маркера при Astrolite stage 5; отдельные ветки удаления объектов Carson и замены кровавой обстановки | `mercurioFight()` L123–137; `finishElysiumTip()` L44–66; VMF ID 609 |

Число этапа в `pc.SetQuest` и значение `G.*` — разные записи состояния. Например, DLG 171 независимо задаёт `G.Mercurio_Quest=2`, `G.Mercurio_Astro=2` и журнальный `Astrolite=3`.

## Carson и физические предметы

[DATA] `Carson_Computer.txt` содержит McGee / `Imalia`; функция Location вызывает `carsonComputerHacked()`. [PY] L31–36 повышает `Arthur Knox` до stage 2 только при текущей стадии 1. [VMF] `Carson_Computer` ID 596 имеет `difficulty=2`, `skilltype=2`; ключ tattoo parlor ID 597 пишет `G.Key_Taken=1`, journal ID 609 пишет `G.Journal_Taken=1`, `trunk_lock` ID 616 пишет `G.Trunk_Opened=1` на успешной проверке. Наличие этих средств не доказывает возможность получить каждый предмет в любом сюжетном состоянии.

**Отличие Plus:** DLG 1015 явно требует `G.Patch_Plus==1`; `finishElysiumTip()` проверяет Plus при удалении объектов Carson и очистке помещения. Это свидетельства в исходниках UP, не утверждение о полном наборе изменений относительно релиза 2004 года.
