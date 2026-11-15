# Santa Monica — квесты и состояния

Самостоятельные заметки о квестах и переменных состояния. Тексты диалогов и Python не копируются сюда: см. исходные исследования персонажей и карт по ссылкам.

- [[Arthur's_Introduction]] — начальный разговор с Артуром и состояния, не являющиеся отдельными квестами.
- [[Bail_Hustler_Quest]] — состояния делового задания Артура.
- [[Bail_Jumper_Quest]] — ветки bounty hunter Артура.
- [[Knox_Quest]] — Кнокс и связанные переходы между картами; см. также [[../Locations/basement1/SM-18_Basement_00_Index|Gimble basement]].
- [[Santa_Monica_Discovery]] — записи диалога Артура о местах и делах района; в документе отмечено, что это не отдельный квест.
- [[../Locations/medical1/SM-14_Medical_03_Quests|Medical Clinic — квестовые состояния внутри анализа карты]].

## Night at the Library

Цепь связывает убежище, Smoke Shop, Pier, Coffee Shop и Downtown. Журнал `Library` задан в `Unofficial_Patch/vdata/system/quests_downtown.txt` (SHA-256 `5b533c73c5f61209b14aab5b76d936d6f9a699e075c71fe1d81fef2420c7ee17`). SHA `vamputil.py`, `santamonica.py` и почты приведены в [[../Locations/pawnshop1/SM-29_Pawnshop_1_Passport|SM-29]].

| Шаг | Условие и запись |
|---|---|
| Письмо в убежище | `setPlus()` ставит `Library_Ready=1`, если `Jumbles_Removed=1`, `LaSombra_Seen=1`, `Isaac_Movie>0`. В `haven_pc.txt:247` письмо требует `Library_Ready>=1` и Plus. Вызов `librarySetQuest()` при Smoke=0 ставит Library=1 и `Library_Smoke=1`. |
| [[../Locations/smoke1/SM-19_Smoke_00_Index|Smoke Shop]] | `setPlus()` показывает записку при Smoke=1. Разговор с продавцом даёт контекст. Записка при чтении ставит `Library_Smoke=2` и через 0.1 с вызывает `librarySetQuest()`: Library=2, Note=1, Smoke=3. |
| [[../Space/Surface|Pier]] | `logic_auto.OnMapLoad → murderCleanedUp()` показывает `piernote` и подсветку при Note=1. Чтение ставит Note=2 и через 0.1 с вызывает `librarySetQuest()`: Library=3, Coffee=1, Note=3. При выходе из чтения записаны отдельные выходы на частицы и показ `trapobfuscator`. |
| [[../Locations/coffee1/SM-17_Coffee_00_Index|Coffee Shop]] | `setPlus()` отпирает вход при Coffee>0. Пятая запись Scott laptop ставит Coffee=2; при Open=0 вызов `librarySetQuest()` задаёт Library=4, Open=1 и Coffee=3. |
| Downtown → Library | `setPlus()` при Open>0 показывает `library_open` у `(650,-5017,-980)` в `la_hub_1` и скрывает `library_closed`. Активный люк через `OnActivate → library_trigger.ChangeNow` (1.5 с) ведёт в `la_library_1`, landmark `library_entrance`. `library_leave` ведёт обратно. SHA BSP: `la_hub_1` — `f2cbdce345bc3d709880d42274fd4a75ceadcf7aa350612d77c159ea397037be`, `la_library_1` — `2008a86c9f6727f9b25d9885f4dc2a1706a81ea1c16fb02a9185aaa872b6fd4b`. |
| Исход в скриптах | `useBox()` при наличии коробки ставит Library=5, первое `unhideKey()` — 6, `foundRitualChamber()` — 7, `defeatedAndrei()` — 8 и Jumbles_Removed=2. Следующее письмо при Plus/Jumbles_Removed=2 пишет Open=2; при обоих `Guard*_Killed=0` `librarySetQuest()` выдаёт `Library02` и ставит Open=3. Постановочные входы внутри Downtown Library требуют собственной проверки. |

