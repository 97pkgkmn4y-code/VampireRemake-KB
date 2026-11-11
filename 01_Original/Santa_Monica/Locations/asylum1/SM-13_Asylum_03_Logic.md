---
id: SM-13-LOGIC
map: sm_asylum_1
status: VMF I/O verified; external script behavior unknown
---
# SM-13.03 — Логика VMF: переходы, сцены, гейты

> [!important] Метод
> Каждое ребро ниже существует как конкретный KeyValue в секции `connections`. Это **доказательство проводки I/O**, но **не доказательство, что событие вообще наступит в данной сюжетной ветке**. Внешние Python-функции показаны как неопределённые вызовы; их реализация не видна.

## 1. Возвращение из клуба в город [F]

- `info_landmark targetname=asylum1` (`L36845`, origin `−1054 628 −272`).
- `trigger_changelevel targetname=AsylumTeleport1` (`L36858`) с `map=sm_hub_1` и `landmark=asylum1`.
- `func_door_rotating asylumdrl` (`L36158`) и `asylumdrr` (`L36268`) **каждая** имеют `OnFullyOpen → AsylumTeleport1.ChangeNow`.

**[F]** Это не «переход при пересечении порога»: в исходнике его вызывают события открытия дверей. **[?]** Нужен встречный `trigger_changelevel`/landmark в `sm_hub_1` и проверка фактической точки появления для полного графа переходов.

## 2. Лифт: двери, блокировки, разрешения [F]

### Параметры

| Сущность | Параметры / роль |
|---|---|
| `elevator` (`func_elevator`, L29674) | `speed=50`, `numfloors=2`, `floor1=-30`, `floor2=235` |
| `downstairsbttn` | `locked=1`, L41691 |
| `upstairsbttn` | `locked=0`, L41722 |
| `down_button_inside_elevator` | `parentname=elevator`, L41753 |
| `up_button_inside_elevator` | `parentname=elevator`, L41782 |
| `elev_counter_downstairs` | `min=0`, `max=6`, `startvalue=0`, L42167 |
| `elev_counter_upstairs` | `min=0`, `max=6`, `startvalue=0`, L42146 |

### Сигнальные цепочки

```mermaid
flowchart TD
 A[Кнопка лифта] --> B[SetState2]
 B --> C[GotoFloor 1/2 или elevator_relay]
 C --> D[elevator: OnMoveStart]
 D --> E[elevator_shake: StartShake]
 D --> F[elevator: OnReachFloorN]
 F --> G[Открытие группы дверей elev / elev2]
 F --> H[Блокировка внутренних кнопок]
 F --> I[skin_reverter: Trigger]
 G --> J[Шесть OnFullyClosed на группу]
 J --> K[math_counter: max=6]
 K --> L[Разблокировка кнопок]
 K --> M[Нижняя группа: checkElevatorPermission()]
```

Это **схематизация I/O**, а не механическая последовательность всех возможных событий (например, закрытие может происходить в циклах; сам переход в `OnFullyClosed` может наступать не сразу). Названия `floor1`, `floor2` не доказывают абсолютную высоту мира.

[?] Семантика `checkElevatorPermission()` в VMF отсутствует. Имеющиеся сигналы позволяют уверенно утверждать, что проектировщики учитывали закрытие групп дверей перед возвратом управления кнопкам, но **нельзя** по одному исходнику обещать отсутствие лифтовых багов.

## 3. Сцена Jeanette ↔ Cal ↔ лифт [F]

- `OnMapLoad` запускает `calDialog()`, `jeanetteDownstairs()`, `populateOffice()` и другие функции (L38813).
- `Cal.OnDialogBegin → jeanetteGoesUp()` (L38748).
- `Jeanette.OnDialogEnd → jeanetteDialog()` **и** `wait_for_elevator_relay.Trigger` (L38858).
- `wait_for_elevator_relay` имеет `StartDisabled=1` (L39343), а при Trigger вызывает: `tourette_control_player.CreateControllerNPC`, `Jeanette.WillTalk 0`, `jeanette_to_elevator_camera.StartShot`, `Jeanette_wait_for_elevator.BeginSequence` (с задержкой 1).
- `Jeanette_wait_for_elevator.OnBeginSequence → elevator_relay.Trigger` (задержка 1; L38834).
- `elevator_relay.OnTrigger → elevator.GotoFloor 1` (L38997).
- `Jeanette_in_elevator.OnEndSequence` управляет камерой, `WillTalk`, `ScriptHide`, `bring_Jeanette_up.Teleport` и кнопкой `downstairsbttn` (L41449).
- `Jeanette_dialog` (`trigger_once`, `StartDisabled=1`, L39660) при касании включает камеру и начинает `Jeanette.StartPlayerDialog`.

**[I]** Это комплексная режиссированная последовательность: разговоры, временный запрет на управление, приближение к лифту, видимая/невидимая часть перемещения, изменение доступа к лифту. Не установлено, в какие именно сюжетные моменты она запускается; `StartDisabled` и `ScriptHide` критически зависят от скриптов.

## 4. Сцена Therese / Tourette [F]

- `Tourette` — отдельная VMF-сущность (`npc_VVampire`, L40080), `additionalequipment=item_w_thirtyeight`, `dialogname=dlg/Santa Monica/Tourette.dlg`.
- `tourette_trigger` (`trigger_once`, `StartDisabled=1`, L39923) при касании запускает через задержки: `tourette_cam.StartShot`, `Tourette_point_gun.BeginSequence`, `tourette_control_player.CreateControllerNPC`, `player_to_tourette.BeginSequence` и `Tourette_thirtyeight.ScriptUnhide`.
- `Tourette_point_gun.OnEndSequence → Tourette.StartPlayerDialog` (0.3 сек; L40052), одновременно удаляет controller.
- `Tourette.OnDialogEnd` вызывается со скриптовым выражением `touretteDialogueResults()` и завершает `Tourette_point_gun` (L40080).
- `Therese_mad_trigger` (`StartDisabled=1`, L41894) содержит `Therese.StartPlayerDialogRemote` и `player_to_therese.BeginSequence` наряду с контроллером игрока.
- `asylum_fade` (L40145): `OnBeginFade` по задержкам удаляет модель оружия, запускает разговор и создаёт controller.

**[I]** Карта поддерживает как минимум две постановочные конфигурации встреч наверху: управляемую автоматикой сцену с Tourette и дистанционный/режиссированный запуск Therese. **[?]** Как они переключаются по веткам и кто видим в конкретный момент — неизвестно без Python/DLG.

## 5. Ссора / изменение доступа [F]

`argument_relay` (L41347) при `Trigger`:

1. `argument_done_relay.ScriptUnhide` сразу.
2. `argument_done_relay.Trigger` через **52 секунды**.
3. `sisters_argument.PlaySound` сразу; источник — `Character/CONVERSATIONS/Sisters_Argument.wav`.
4. `bathroom_door.Lock` сразу.

`argument_done_relay` (L42665) при Trigger:

1. `G.Asylum_Visited = 1` (0.1 с).
2. `upstairsbttn.Unlock` (1 с, одноразовое действие).
3. `bedroom_door.Unlock` (1 с, одноразовое действие).
4. `unlock_door_sound.PlaySound` (1 с, одноразовое действие).

**Критическая оговорка:** `argument_relay` не имеет прямого входящего ребра от другого объекта в просмотренных VMF connections — оно может запускаться из Python/Dialog/движка. Поэтому **не доказано**, что сцена автоматически начинается при входе или что 52 секунды отсчитываются от загрузки карты. `G.Asylum_Visited` здесь ставится по окончании реле, а не просто при загрузке.

## 6. Танец, NPC и скриптовые состояния [F]

`player_dance_trigger`:
- `OnUseBegin`: отключает общие `dance_spot`, включает `dance_spot_player`, ставит `G.No_Idle=1`.
- `OnUseEnd`: возвращает состояние обратно и ставит `G.No_Idle=0`.

`Danielle`:
- `Danielle.OnDeath → G.Danielle_Dead=1`.
- `Danielle.OnDialogEnd → danielleDialog()`.
- `intersting_place` (L41996) содержит `OnNPCArrived → Danielle_kill_trigger.Enable`; сам `trigger_once targetname=danielle_kill_trigger` (L42023) на касание вызывает `Danielle.Kill`.
- Отличие регистров `Danielle_kill_trigger` и `danielle_kill_trigger` — **факт текста**, но по одному VMF оно не доказывает неисправность: в данном анализе имена совпадают при сравнении без регистра.

`Doll1.OnDeath → G.Doll1_Dead=1`.

## 7. Состав OnMapLoad [F]

В первом `logic_auto` (L38813) указаны следующие вызовы:

```text
calDialog()
chunkDancing()
jeanetteDownstairs()
populateOffice()
Jeanette.WillTalk 1
finishElysiumTip()
knoxPresence()
```

Отдельно в нижней части файла (L46555) `logic_auto.OnMapLoad → unhidePlus()`; у `logic_timer idle_timer` (L46570) каждые 5 секунд: `IsIdling()`.

В `events_player_plus` и `events_world` (L46614+) находятся десятки общих обработчиков дисциплин, frenzy, полиции, Masquerade и боевой музыки. Они важны как точки интеграции глобальной системы, **но не следует без подтверждения приписывать каждую из них уникальному геймдизайну Asylum**.

## 8. Скриптовые вызовы, нуждающиеся в реализации-источнике [?]

Локальные/связанные с картой:

```text
calDialog()
chunkDancing()
jeanetteDownstairs()
populateOffice()
finishElysiumTip()
knoxPresence()
jeanetteGoesUp()
jeanetteDialog()
elevatorConversation()
checkElevatorPermission()
danielleDialog()
touretteDialogueResults()
murderPaperRead()
unhidePlus()
IsIdling()
```

Кроме того, есть непосредственные присваивания `G.*` и общие мировые callbacks. **Нельзя считать содержимое функций известным по их названиям.**
