---
id: SM-13
title: Asylum — указатель исследования
game: Vampire The Masquerade Bloodlines (2004)
reference: Unofficial Patch Plus
map: sm_asylum_1
status: static source analysis; RUNTIME PENDING; UPP v12.0 provenance partly unverified
source: sm_asylum_1.vmf
source_sha256: 6b637179bf6997e5441eaaf9d211e3ae3a52b3d9d3ebdd5d52f2a8b665c198e0
---
# SM-13 — The Asylum

> [!important] Статус доказательности
> Это статический анализ по **VMF** (`sm_asylum_1.vmf`, sha256 в frontmatter), **BSP** (base `Vampire\maps` и `Unofficial_Patch\maps`), **Python** (`santamonica.py`) и **DLG** (CSV Cal/Jeanette/Therese/Tourette в `SM-13_Asylum_Assets`), дополненный отдельно обозначенными внешними свидетельствами.
> История: индекс создан 2026-11-05 при доступе к VMF-only; заметки 05–12 дополнены к 2026-11-06; устаревшая выноска «Python/DLG/BSP отсутствуют» исправлена 2026-11-10 (VAULT_AUDIT §4.1).
> Игровая проверка (RUNTIME) не выполнялась. **Состояния квестов, активная популяция и фактическая проходимость не установлены полностью.**

## Связанные заметки

- [[SM-13_Asylum_01_Spatial|01 — Пространство и вертикальная структура]]
- [[SM-13_Asylum_02_Entities|02 — Сущности, триггеры и интерактивность]]
- [[SM-13_Asylum_03_Logic|03 — Логика, сценарии, цепочки I/O]]
- [[SM-13_Asylum_04_Analysis|04 — Геймдизайн, квестовые связи и вопросы]]
- [[SM-13_Asylum_05_Script_Logic|05 - Python и логика сценариев]]
- [[../Characters/SM-13_Asylum_06_Cal_Dialogue|06 - Cal: диалог и условия]]
- [[../Characters/SM-13_Asylum_07_Therese_Dialogue|07 - Therese: DLG и состояния]]
- [[../Characters/SM-13_Asylum_08_Jeanette_Dialogue|08 - Jeanette: DLG и последствия]]
- [[../Characters/SM-13_Asylum_09_Tourette_Dialogue|09 - Tourette: DLG и камеры]]
- [[SM-13_Asylum_10_Camera_Direction|10 - направление камеры]]
- [[SM-13_Asylum_11_Camera_Shot_Bindings|11 - привязки камер]]
- [[SM-13_Asylum_12_Symmetric_Cameras|12 - симметрия камер]]
- [[../Santa_Monica_Research_Index|Общий индекс Santa Monica]]
- ![[SM-13_Asylum_Assets/asylum_vmf_schematic.png]]

## Легенда свидетельств

- **[F]** — прямое утверждение, проверенное в `sm_asylum_1.vmf` (при необходимости указаны строки `L` и `targetname`).
- **[E]** — внешнее свидетельство (всегда со ссылкой; не равнозначно проверке в данном патче).
- **[I]** — интерпретация геометрии / возможное назначение / геймдизайнерский вывод, основанный на [F].
- **[?]** — вопрос, требующий другой файл, движок или игровой эксперимент.

## Паспорт исходника [F]

| Параметр | Значение |
|---|---|
| Файл | `sm_asylum_1.vmf` |
| Объём | 1 806 427 байт, 81 261 строка |
| Форма | Source/VMF, plain text |
| `worldspawn.levelscript` | `santamonica` |
| `worldspawn.safearea` | `2` |
| `worldspawn.copwaitarea` | `1` |
| `worldspawn.nosferatu_tolerrant` | `1` — именно такое написание ключа |
| `worldspawn.skyname` | `holly` |
| `worldspawn.comment` | `Edited by Psycho-A and Wesp5 for Unofficial Patch` |
| Мировые браши | 368 |
| Браши с учётом entity solids | 982 |
| Entity blocks | 542 |
| Различных `classname` | 48 |

Параметры `safearea`, `copwaitarea` и `nosferatu_tolerrant` пока рассматриваются **только как записи карты**, не как полностью расшифрованное поведение. В файле нет определения их реализации.

## Главные факты [F]

1. Один BSP-уровень включает основной танцпол, сцену, бар, промежуточную площадку/балкон и частные помещения, локализуемые по брашам, статическим моделям и интерактивным объектам.
2. Две симметричные системы ступеней связывают низ и промежуточный уровень; есть отдельный двухостановочный `func_elevator`.
3. Выходной `trigger_changelevel` указывает на `sm_hub_1`, landmark `asylum1`; `OnFullyOpen` обеих створок главной двери посылает `ChangeNow`.
4. Карта содержит шаблоны персонажей `Jeanette`, `Therese`, `Tourette`, `Cal`, `Danielle`, `Chunk`, `Knox_basic`, `Knox_plus`, танцующих и `Doll1`. Наличие в VMF **не означает одновременного появления** в игре.
5. Сцены используют `logic_relay`, `scripted_sequence`, `camera_cinematic`, `env_fade` и контроллер игрока. Сценарии сильно зависят от внешнего `santamonica` и `.dlg`.
6. В `ambient_generic music` указан `Music/Licenced/05. Chiasm - Isolated.mp3`.

## Границы исследования

- **Не доказано:** все доступные игроку маршруты, точные коллизии, момент открытия лифта и комнат, живые стадии квестов, реальное число посетителей на конкретном прохождении, входные условия крупных катсцен.
- **Не выполнялось:** преобразование Asylum под ремейк, переделка планировки, сравнение с Unity-картой, автоматическое исправление или экспорт игровых ресурсов.

## Внешний контекст (не подменяет VMF)

- [The Asylum — VTMB Wiki](https://vtmb.fandom.com/wiki/The_Asylum): список квестов, персонажей, характер клуба и музыка. **[E]**
- [The Asylum — White Wolf Wiki](https://whitewolf.fandom.com/wiki/The_Asylum): описание клубных функций и балкона. **[E]**
- [Sibling Rivalry — VTMB Wiki](https://vtmb.fandom.com/wiki/Sibling_Rivalry): нарративный контекст. **[E]**

## Степень готовности

**Геометрия:** ориентировочная карта зон и источники лестниц найдены; топология с проверенной проходимостью не доказана.  
**Сущности:** полная сводка классов и ключевые `targetname` извлечены.  
**I/O:** основные цепочки восстановлены.  
**Скрипты и диалоги:** `santamonica.py` и DLG-CSV доступны (см. выноску выше); выводы ограничены сверенным в заметках 05–12.


> **Полнота и runtime:** пространственная схема, сущности/I/O, Python, DLG и камеры рассматриваются в отдельных заметках выше. Проходимость и фактическое поведение в установленной игре не проверялись. Для части исходников в текущих заметках версия Unofficial Patch Plus v12.0 не зафиксирована явно. Сводные пробелы: [[../Santa_Monica_Research_Index]].
