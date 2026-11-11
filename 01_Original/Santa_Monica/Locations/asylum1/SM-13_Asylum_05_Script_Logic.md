---
id: SM-13-SCRIPT
map: sm_asylum_1
reference: Unofficial Patch Plus (предоставленные файлы)
status: VMF/Python cross-verified; DLG and engine behavior pending
source_vmf: sm_asylum_1.vmf
source_vmf_sha256: 6b637179bf6997e5441eaaf9d211e3ae3a52b3d9d3ebdd5d52f2a8b665c198e0
source_script: santamonica.py (загружен как santamonica(1).py)
source_script_sha256: 5f62a97ba59c997fdc5df6befe9203f8d28e6261001b35d7b98f3aecc6c3daf4
---
# SM-13.05 — Asylum: Python, состояния квестов и синхронизация с VMF

> [!important] Доказательная база
> **[F:PY]** — точная реализация в предоставленном `santamonica.py` (строки `PY L…`). **[F:VMF]** — фактические свойства/выходы сущностей `sm_asylum_1.vmf` (строки `VMF L…`). **[F:2]** — связь подтверждена в обоих файлах. **[I]** — интерпретация, **[?]** — неизвестное поведение движка, DLG или другой карты. Исходники рассматриваются как единая предоставленная сборка, но версия патча по ним не датирована.
>
> Продолжение: [[SM-13_Asylum_00_Index]], [[SM-13_Asylum_01_Spatial]], [[SM-13_Asylum_02_Entities]], [[SM-13_Asylum_03_Logic]], [[SM-13_Asylum_04_Analysis]]. **Никакого проектирования ремейка.**

## 1. Область анализа

`worldspawn.levelscript="santamonica"` в VMF; в `santamonica.py` найдено **12 функций с явным комментарием `#ASYLUM`** (`PY L162–380`). Это общий скрипт нескольких локаций, поэтому остальные функции нельзя автоматически считать уникальными для Asylum.

| Функция / PY | Назначение, подтверждённое кодом | Вызывается в VMF |
|---|---|---|
| `calDialog` (163–166) | Разблокировать `downstairsbttn`, если `Cal_Permission==1` | `OnMapLoad`, `Cal.OnDialogEnd` |
| `checkElevatorPermission` (169–174) | Включить/снять блокировку `downstairsbttn` | `elev_counter_downstairs.OnHitMax` |
| `chunkDancing` (177–188) | Скрыть/показать Chunk; убрать умерших Danielle/Doll1 | `OnMapLoad` |
| `danielleDialog` (191–195) | При комбинации флагов Vandal/Patty/Gimble изменить общение Danielle | `Danielle.OnDialogEnd` |
| `elevatorConversation` (198–218) | Проверка X игрока; старт ссоры либо разблокировка комнат | `elevgrating2.OnFullyClosed` |
| `knoxPresence` (221–233) | Выбрать `Knox_plus`/`Knox_basic` и назвать `Knox` | `OnMapLoad` |
| `jeanetteDialog` (236–240) | Запустить `jeanette_boink_relay`, перевести флаг 1→2 | `Jeanette.OnDialogEnd` |
| `jeanetteDownstairs` (243–257) | Первое знакомство: перенос вниз, включение триггера разговора и реле | `OnMapLoad` |
| `jeanetteGoesUp` (260–265) | При условии перенести Jeanette вверх и скрыть | `Cal.OnDialogBegin` |
| `populateOffice` (268–362) | Восемь приоритетных веток состояния трёх NPC, ПК и триггеров | `OnMapLoad` |
| `touretteDialogueResults` (365–375) | Постсцена: затемнение и смена модели или переход на `asylum1` | `Tourette.OnDialogEnd` |
| `touretteMuzzleFlash` (378–380) | Включить `muzzle_flash` | **Прямого I/O-вызова в VMF не обнаружено** |

**[F:VMF]** Сопоставление строк показало, что имена локальных сущностей, к которым обращаются эти 12 функций через буквальный `Find("…")`, присутствуют в VMF. Это проверка ссылок, **не** проверка корректности выполнения каждого метода движком.

## 2. Доступ к лифту: флаг Cal не равен разрешению от дверей

**[F:2]** Кнопка у нижней остановки `downstairsbttn` имеет в VMF `locked=1` (`VMF L41691`), а верхняя `upstairsbttn` — `locked=0` (`L41722`). На загрузке и после окончания беседы с Cal вызывается `calDialog()`: **только** если `G.Cal_Permission == 1`, нижняя кнопка получает `Unlock()` (`PY L163–166`, `VMF L38748`, `L38813`).

**[F:2]** После закрытия шести створок нижней группы счётчик `elev_counter_downstairs` достигает max=6 (`VMF L42167`), вызывает `checkElevatorPermission()` (`PY L169–174`) и повторно ставит кнопку в `Lock` или `Unlock` в зависимости от **того же флага**. Следовательно, разрешение Cal проверяется как минимум в двух контекстах: загрузка/диалог и цикл лифтовых дверей.

**[?]** Какая реплика, условие навыка либо сюжетная переменная устанавливает `G.Cal_Permission=1`, Python **не показывает**: источник — диалог(и) или другое место установки флага. Нужен `dlg/Santa Monica/Cal.dlg`.

## 3. Первая ссора сестёр: цепочка полностью найдена

**[F:2]** В `VMF L28650` дверь `elevgrating2` (верхняя решётка лифта, `origin=-1113.5 606 38`) на `OnFullyClosed` через **0.7 с** вызывает `elevatorConversation()`.

```mermaid
flowchart TD
  A[Верхняя решётка elevgrating2 полностью закрылась] -->|через 0.7 с| B[elevatorConversation]
  B --> C{player.X >= -1114?}
  C -->|нет| D[Ничего не делать]
  C -->|да| E{G.Asylum_Visited == 0?}
  E -->|да| F[argument_relay.Trigger]
  F --> G[Ссора звучит; bathroom_door.Lock]
  F -->|52 с| H[argument_done_relay.Trigger]
  H --> I[G.Asylum_Visited = 1 через 0.1 с]
  H --> J[upstairsbttn.Unlock и bedroom_door.Unlock через 1 с]
  E -->|нет| K[bathroom_door.Unlock; bedroom_door.Unlock]
  K --> L[Заблокировать обе внутренние кнопки лифта]
```

Условие координат и ветки — `PY L198–218`. Запуск и звуковое событие — `VMF L41347`; завершение — `VMF L42665`.

**Важные тонкости:**

1. **52 и 55 секунд — разные механизмы.** `argument_relay` вызывает `argument_done_relay` через 52 с; Python параллельно планирует `G.Asylum_Visited=1` через **55 с** (`PY L205`). Завершающее реле само тоже устанавливает этот флаг через 0.1 с. Их нельзя ошибочно считать одной задержкой.
2. **Ванная ≠ спальня по механизму открытия.** Первый запуск сразу `bathroom_door.Lock`, а через 52+ секунд `argument_done_relay` разблокирует **`bedroom_door`**, но **не** `bathroom_door` (`VMF L41347`, `L42665`). В показанной Python-функции разблокировка ванной присутствует **в повторной ветке**, когда `Asylum_Visited != 0` и `X >= -1114`. Прямого VMF-события `bathroom_door.Unlock` в файле не найдено. Доступность ванной сразу после ссоры **не доказана**.
3. **Условие X, вероятно, отсеивает игрока внутри шахты/кабины** [I]: решётка расположена при `X=-1113.5`; если игрок ещё находится левее `X=-1114`, при закрытии разговор не стартует. Для подтверждения такой пространственной интерпретации нужен просмотр конкретного расположения игрока/коллизий [игра/BSP].
4. **Возможность повторного старта до установки флага** есть на уровне условий: сама функция не выставляет флаг синхронно перед запуском, а откладывает его. Будет ли повторно вызвано `OnFullyClosed` за этот интервал — **не доказано**, поэтому считать это багом нельзя.
5. `upstairsbttn` в свойствах VMF первоначально `locked=0`; позже самоблокируется при использовании и разблокируется несколькими путями (в том числе `argument_done_relay`, `elev_counter_upstairs`). Нельзя утверждать, что именно ссора впервые открывает верхнюю кнопку.

## 4. Первое знакомство с Jeanette и лифтовая постановка

**[F:2]** На загрузке `jeanetteDownstairs()` проверяет `Jeanette.times_talked == 0` и `G.Therese_Quest < 2` (`PY L243–257`). Если оба условия верны:

- переключает disposition Jeanette на `Flirtatious`;
- вызывает `bring_Jeanette_down.Teleport()`; точка переноса — `(-904.223, 420.837, -280.691)`;
- включает `Jeanette_dialog` и `wait_for_elevator_relay` (в VMF оба стартуют с `StartDisabled=1`).

Далее `Jeanette_dialog.OnStartTouch` запускает разговор с задержкой 1 с (`VMF L39660`); `Jeanette.OnDialogEnd` вызывает `wait_for_elevator_relay.Trigger` и `jeanetteDialog()` (`VMF L38858`). Реле переключает камеру, контроллер игрока и запускает сцену ожидания лифта (`VMF L39343`). По дальнейшим I/O Jeanette оказывается у лифта и переносится наверх через `bring_Jeanette_up`, при этом применяется `ScriptHide` (`VMF L41449`).

**[F:PY]** Если первое-знакомство-условие **не** выполнено, `jeanetteDownstairs()` лишь включает `UseInteresting(1)` на `jeanette_flirt_partner`; положение Jeanette из этой ветки само по себе не определяется.

**[F:2]** `Cal.OnDialogBegin → jeanetteGoesUp()`: если `G.Cal_Permission != 1` **или** `G.Therese_Quest == 0`, Jeanette переносится наверх и скрывается (`PY L260–265`). Это независимая от сцены ожидания лифта ветка. В каком порядке реальные диалоги допускают её выполнение — проверять по DLG.

**[F:2]** После диалога Jeanette, когда `G.Jeanette_Boink == 1`, `jeanetteDialog()` активирует отдельное `jeanette_boink_relay` и переводит флаг в `2` (`PY L236–240`); relay инициирует fade/аудио/контроллер и возвращает Jeanette через 35 с (`VMF L42122`). Условие получения `Jeanette_Boink == 1` находится **не в данном Python**.

## 5. populateOffice(): действительный порядок условий

**[F:PY]** Функция (`PY L268–362`) — приоритетная цепочка `if / elif`, а **не** независимая таблица одновременно действующих правил. Вывод ниже показывает действия выбранной ветки **до** иных I/O или диалогов. `Show`/`Hide` означает вызовы `ScriptUnhide`/`ScriptHide` на сущностях, а не гарантированную итоговую видимость в кадре.

| № / строки | Условие (проверяется только после отказа предыдущих) | Показаны / скрыты | Дополнительный эффект |
|---|---|---|---|
| 1, L278–286 | `Therese_Quest < 2` | `Jeanette_Know==1`: только Therese; иначе **Jeanette и Therese одновременно**; Tourette скрыта | Не меняет ПК-блокеры явно |
| 2, L287–293 | `2 ≤ Therese_Quest < 3`, `Jeanette_Quest < 2`, `Jeanette_Refuse < 1` | Jeanette видна, Therese/Tourette скрыты | Jeanette PC blocker виден, Therese blocker скрыт |
| 3, L294–300 | `Jeanette_Quest == 2` и `Therese_Quest < 4` | Therese видна; остальные скрыты | Therese PC blocker виден; `Therese_mad_trigger.Enable` |
| 4, L301–307 | `3 < Hotel state < 6` и `Slashterpiece state == 0` | Therese видна; остальные скрыты | Аналогично ветке 3 |
| 5, L308–313 | `Jeanette_Refuse ≥ 1`, `Jeanette_Fire < 3`, `Therese_Quest < 3` | Все три скрыты | Оба ПК-блокера скрыты |
| 6, L314–320 | `Jeanette_Fire == 3`, `Therese_Quest < 4` | Therese видна; остальные скрыты | `Therese_mad_trigger.Enable` |
| 7, L321–330 | `Therese_Quest == 4`, нет `Tourette_Wins`, `Therese_Dead`, `Jeanette_Dead` | Tourette видна; Jeanette/Therese скрыты | Включить `tourette_trigger`, запустить `tourette_sequence_relay` |
| 8, L331–355 | `Tourette_Wins==1` **или** Therese/Jeanette dead | Если `Story_State < 10` — все скрыты; иначе победитель/выжившая по последовательным проверкам | ПК-блокеры меняются согласно подветке |
| 9, L356–359 | Ни один вариант | Сообщение `Unaccounted for case` | Нет явного переключения NPC |

**Критический пример приоритета [F:PY]:** `Therese_Quest == 4` **не гарантирует** появление Tourette. Если на том же входе `Hotel state==4` и `Slashterpiece state==0`, сработает **ветка №4**, потому что она стоит раньше ветки №7. Это нельзя терять при построении квестового графа.

**Особенность ветки 8:** при `Story_State >=10` проверяется сначала `Tourette_Wins`, затем `Jeanette_Dead`, затем `Therese_Dead`. Если одновременно истинны несколько флагов, первый подходящий вариант имеет приоритет. Статусы «выжил/умер» берутся из глобальных флагов; их условия установки — не в этой функции.

После выбора ветки при `Vandal_Quest==3`, `Patty_SM!=1`, `Gimble_Vandal!=1` код **дополнительно убивает/удаляет Danielle entity** (`L360–362`). Это не часть выбора трёх вампиров.

## 6. Tourette: развязка и смена модели

**[F:2]** Ветка №7 `populateOffice()` показывает Tourette и включает `tourette_trigger`. VMF-триггер управляет камерой, анимациями оружия, видимостью револьвера и временным контроллером игрока (`VMF L39923–40080`). После диалога вызывается `touretteDialogueResults()` (`PY L365–375`).

- Если `G.Jeanette_Dead == 1`: запускается `asylum_fade`, через 3 с **модель сущности `Tourette`** меняется на `Therese.mdl`. Это **не** явное изменение `targetname`, `dialogname` или факт рождения нового NPC.
- Иначе, если `G.Tourette_Wins == 1`: удаляется `Tourette_thirtyeight` (при наличии) и вызывается `__main__.ChangeMap(2.5, "asylum1", "AsylumTeleport1")`.
- Если ни одно условие не истинно, функция не делает явных действий. Условия появления этой развязки определяются и диалогами.

**[F:PY]** `touretteMuzzleFlash()` включает `muzzle_flash` (`PY L378–380`). В VMF объект `muzzle_flash` есть (`L41878`), но обращения к функции в `connections` **нет**. Не следует считать эффекты выстрела нерабочими: вызов может находиться в DLG/другом сценарии.

## 7. Второстепенные NPC и версии Plus

**[F:PY]** `knoxPresence()` (`PY L221–233`) показывает Knox, если `G.Mercurio_Quest >= 2` и `IsDead("Knox")` ложно. При `G.Patch_Plus == 1` выбирается **`Knox_plus`**, иначе — **`Knox_basic`**, затем сущности присваивается имя `Knox` (`SetName`). VMF показывает различное расположение этих двух entities (см. [[SM-13_Asylum_02_Entities]]). Это уже **прямое свидетельство**, что переключение вариантов Knox определяется Python, а не только именами `basic/plus`.

**[F:PY]** `chunkDancing()` (`PY L177–188`) показывает Chunk только при всех условиях: `Chunk_Dominated==2`, `Story_State<10`, `Chunk_Dead==0`, `not IsDead("Chunk")`. Если `Danielle_Dead==1` или `Doll1_Dead==1`, соответствующие сущности удаляются.

**[F:PY]** `danielleDialog()` (`L191–195`) при `Vandal_Quest==3`, `Patty_SM!=1`, `Gimble_Vandal!=1` вызывает `UseInteresting(1)` и `WillTalk(0)` для Danielle. `populateOffice()` при тех же условиях может вызвать `Danielle.Kill`; их фактическое сочетание во времени нужно проверять, а не автоматически объявлять ошибкой.

**[?]** `unhidePlus()` вызывается из `logic_auto` VMF (`L46555`), **но не объявлена** как `def` в переданном `santamonica.py`. В верхней части скрипта есть импорт `vamputil`; реализацию `unhidePlus()` нужно искать в доступных глобальных/импортируемых функциях. Поэтому переключение **остального** Plus-декора ещё не закрыто.

## 8. Доказуемые перекрёстные связи других карт

Эти факты — из **того же** `santamonica.py`, но относятся к вызовам на **других локациях**, которые пока не сопоставлены с их VMF:

| Другая локация / функция | Проверенный эффект | Что это значит для Asylum |
|---|---|---|
| Ocean House, `oceanhouseQuestComplete` (`PY L1457–1460`) | `SetQuest("Hotel",2)`; `G.Therese_Quest=2` | Объясняет один внешний источник перехода в поздние ветки `populateOffice` |
| Diner, `thugsAllDead` (`PY L1212–1232`) | Если `Therese_Quest !=4`, выставляет `G.Therese_Quest=4`, `SetQuest("Diner",2)`, включает звонок | Переход к потенциальной ветке Tourette зависит от события в **другой карте**, а не только Asylum |
| Santa Monica hub, `bertramOutOfHiding` (`PY L1750–1777`) | Реагирует на `Tourette_Wins`, `Therese_Dead`, `Jeanette_Dead` и открывает связанную реакцию Bertram | Исход развязки имеет следствие вне Asylum (точная точка вызова ещё не проверена) |
| Santa Monica hub, `jeanetteRefused` (`PY L1964–2010`) | Использует `Jeanette_Quest`, `Jeanette_Refuse`, `Gallery_Slashed` и другие флаги | Решения/состояния Jeanette связаны с событиями Gallery/улицы; точная сценарная последовательность требует исходники hub/DLG |
| Santa Monica hub, `knoxState` (`PY L2033–2045`) | При `Mercurio_Quest==2` или смерти Knox удаляет его entity из hub | Дополняет `knoxPresence`: NPC может быть убран из одной карты и показан в Asylum в зависимости от флагов; это пока **не** доказательство его маршрута в игровом мире |

**[I]** Таким образом, Asylum выступает *визуализатором глобального состояния прохождения*: его локальная популяция не хранит всю квестовую причинность внутри одной карты. Python содержит проверяемые последствия, но причины многих флагов лежат в DLG.

## 9. Неожиданная находка: записка Voerman связана с Serial

**[F:2]** VMF: `voerman_note` (`VMF L41398`) вызывает на `OnReadBegin` **`murderPaperRead()`**. В `santamonica.py` функция расположена в разделе `#HAVEN` (`PY L1375–1380`) и при `GetQuestState("Serial")==0` и `Story_State<5` выставляет `SetQuest("Serial",1)`.

Это **прямое сцепление** записки в Asylum с функцией для газеты в Haven. **[?]** Нам неизвестно, приводит ли чтение записки к реальному обновлению квеста именно в игровой сборке: надо проверить движок/первоначальное состояние квеста. **Не называть багом без проверки.**

## 10. Открытые вопросы после изучения Python

| Приоритет | Что неизвестно | Минимальный источник |
|---|---|---|
| **P0** | Кто/какая реплика устанавливает `G.Cal_Permission=1`, есть ли альтернативные методы допуска наверх | `dlg/Santa Monica/Cal.dlg` |
| **P0** | Условия изменения `G.Therese_Quest`, `G.Jeanette_Quest`, `G.Jeanette_Know`, `G.Jeanette_Fire`, `G.Jeanette_Refuse`; итог Jeanette/Therese/Tourette | `Jeanette.dlg`, `Therese.dlg`, `Tourette.dlg` |
| P1 | Доступ в ванную непосредственно после окончания 52-секундной ссоры без нового цикла верхней решётки | Точечная игровая проверка или полная трассировка DLG/движка |
| P1 | Кто вызывает `touretteMuzzleFlash()` и какие действия сопровождают выстрел | `Tourette.dlg` / дополнительные сценарии |
| P1 | Внешняя реализация `unhidePlus` и других функций из `vamputil` | `vamputil.py` при необходимости |
| P2 | Читается ли `voerman_note`, когда `Serial` state равен 0, и меняет ли квест | Прицельная игровая проверка |
| P2 | Какие физические позиции/коллизии реально обеспечивают условие X при закрытии лифтовой решётки | BSP или игровая проверка |

**Достаточный следующий файл для углубления по порядку: `dlg/Santa Monica/Cal.dlg`.** Пока не требуется повторное прохождение клуба или загрузка других VMF.
