---
id: SM-13-TOURETTE-CAMERAS
map: sm_asylum_1
location: 01_Original/Santa_Monica/Locations/asylum1
status: CameraShotTable + DLG + VMF + Python cross-checked; runtime/camera-resolution unverified
sources:
  - vdata/CameraShots/Tourette.txt
  - dlg/Santa Monica/Tourette.dlg
  - sm_asylum_1.vmf
  - santamonica.py
tags: [vtmb, original, santa-monica, asylum, cinematography, camera, reverse-engineering]
sha256_tourette_txt: dafe2e60311f896498ff811199895de0055a058b6414d81f8f6dced6bd30b72f
sha256_tourette_dlg: 9c49561f8cf51c160260c56d9a5cec06669912bf487c6055183db1037708b5fb
sha256_vmf: 6b637179bf6997e5441eaaf9d211e3ae3a52b3d9d3ebdd5d52f2a8b665c198e0
---
# SM-13.10 — Tourette: камеры, привязки и монтажные события

> [!abstract] Задача и границы
> Исследование **только оригинального** Asylum в эталоне Unofficial Patch Plus. Это продолжение [[SM-13_Asylum_09_Tourette_Dialogue]].
> **[F:C]** — `Tourette.txt`, фактические строки 1–39; **[F:D]** — `Tourette.dlg`, ID записи совпадает с номером строки; **[F:M]** — `sm_asylum_1.vmf`, физические строки; **[F:P]** — `santamonica.py`; **[I]** — обоснованная интерпретация; **[?]** — пробел доказательности. Положение камеры в движке не воспроизводилось.

## 1. Ключевой вывод

**[F:C]** Предоставленный `Tourette.txt` — **один** `CameraShotTable` с **одной** секцией камеры по ключу `Tourette`. В нём нет `tTherese`, `tJeanette` и `DialogDefault`. **[F:M L40080–40144]** VMF у NPC `Tourette` записаны `default_camera = vdata/CameraShots/Tourette.txt` и `dialogname = dlg/Santa Monica/Tourette.dlg`.

**[F:D]** В DLG **96 отдельных записей** содержат `pc.SetCamera()`: **45** переключений на `tTherese`, **44** на `tJeanette`, **3** на `Tourette` и **4** на `DialogDefault`. Это **96 статически присутствующих вызовов**, не 96 кадров одного прохождения: сюжетные ветви взаимоисключающие.

## 2. Параметры `CameraShotTable` из Tourette.txt

| Секция | Ключ | Буквальное значение | Что можем сказать |
|---|---|---|---|
| `End` | `Position` | `DialogTarget` | Позиция задаётся относительно диалоговой цели [F:C L8] |
| `End` | `AttachPos` | `Origin` | Опорная точка origin [L9] |
| `End` | `AttachType` | `Follow` | Задано слежение за опорой [L10] |
| `End` | `OffsetOrigin` | `[48, 0, 53]` | Смещение, **не мировой XYZ** [L11] |
| `Target/Point1` | `Position` | `DialogTarget` | Точка наведения — диалоговая цель [L18] |
| `Target/Point1` | `AttachPos` | `Bone: Bip01 Head` | Ориентир — кость головы цели [L19] |
| `Target/Point1` | `AttachType` | `None` | Отдельное значение привязки точки цели [L20] |
| `CameraConstraints` | `MoveSpeed` | `500` | Параметр скорости; единицы движка не проверены [L27] |
| `CameraConstraints` | `MoveAccel` | `250` | Параметр ускорения [L28] |
| `CameraConstraints` | `TurnAccel` | `30` | Параметр ускорения поворота [L29] |
| `CameraConstraints` | `MaxTurnRate` | `[60, 60, 60]` | Три компонента ограничения вращения [L30] |
| `CameraConstraints` | `DistanceTolerance` | `5` | Допуск по расстоянию [L31] |
| `CameraConstraints` | `AngularTolerance` | `[7, 7, 7]` | Три компонента допуска угла [L32] |
| `CameraConstraints` | `FieldOfView` | `40` | Установлен FOV 40; ось измерения движком не проверена [L33] |
| `CameraConstraints` | `DialogPOV` | `1` | Флаг включён, точный режим требует движка [L34] |
| `CameraConstraints` | `SyncRotateOnMove` | `1` | Флаг синхронизации вращения с движением [L35] |

**[?]** Нельзя вывести из `Tourette.txt` мировую позицию камеры, точный формат координат относительно цели, геометрию ракурса двух сестёр, реальный путь перемещения, длительность каждого кадра или то, является ли `FieldOfView=40` горизонтальным или вертикальным углом. Названия полей позволяют выдвинуть гипотезы, но не заменить проверку.

## 3. Отдельная кинематографическая камера до разговора

![[SM-13_Asylum_Assets/SM-13_Tourette_05_Camera_World_Anchors.png]]

**[F:M L43071–43088]** `tourette_cam` — сущность `camera_cinematic` в **мировой точке `(-926.084, 641.364, 67.7361)`**; её `shotname = vdata/CameraShots/LookAtTarget_Snap.txt`, `startent = endent = tourette_cam`, `target1 = target2 = Tourette`. Это **другая конфигурация**, не `Tourette.txt`.

**[F:M L40080–40144]** NPC `Tourette` находится около `(-906.727, 452.287, -13.4556)` и имеет `default_camera = vdata/CameraShots/Tourette.txt`. Координаты NPC — **не** конечная мировая точка диалоговой камеры.

| Сущность VMF | Мировой origin | Значение в постановке |
|---|---|---|
| `tourette_trigger` | `(-929.940, 693.370, 36.550)` | `trigger_once`; запускает события при касании [L39923] |
| `tourette_cam` | `(-926.084, 641.364, 67.7361)` | кинематографическая камера [L43071] |
| `player_to_tourette` | `(-932.865, 557.017, -14.8927)` | последовательность игрока [L41661] |
| `Tourette_point_gun` | `(-938.607, 516.532, -18)` | анимация перед диалогом [L40052] |
| `Tourette_gun` | `(-935.897, 449.187, -18)` | другая последовательность NPC [L40026] |
| `Tourette` | `(-906.727, 452.287, -13.4556)` | NPC, цель кино-камеры и участник разговора [L40080] |

> [!warning] Ограничение топ-плана
> Это **точки сущностей**, а не точная планировка комнаты или навигация. Линия `target1/target2 → Tourette` означает заданную **ссылку на цель**, а не проверенную прямую видимость. Сопоставлять с [[SM-13_Asylum_01_Spatial]], но не подменять геометрию этой схемой.

## 4. Последовательность сценических вызовов

![[SM-13_Asylum_Assets/SM-13_Tourette_06_Camera_Stage_Pipeline.png]]

- **[F:P L321–330]** `populateOffice()` в своей поздней ветке делает `Tourette.ScriptUnhide()`, включает `tourette_trigger` и вызывает `tourette_sequence_relay.Trigger()`. Ветка выполняется **только после неуспеха более ранних if/elif**, так что сам `Therese_Quest == 4` недостаточен.
- **[F:M L41857–41873]** `tourette_sequence_relay` вызывает `Tourette_gun.BeginSequence` сразу.
- **[F:M L39923–39944]** `tourette_trigger.OnStartTouch` включает `Tourette_thirtyeight.ScriptUnhide` через **0,2 с**, `tourette_cam.StartShot` и управление игроком через **0,4 с**, `player_to_tourette.BeginSequence` через **0,6 с**, `Tourette_point_gun.BeginSequence` через **2,0 с**.
- **[F:M L40052–40079]** по `Tourette_point_gun.OnEndSequence` вызывается `Tourette.StartPlayerDialog` через **0,3 с**, `tourette_control_player.RemoveControllerNPC` без дополнительной задержки.
- **[F:M L40080–40144]** NPC ссылается на `Tourette.txt`; **[F:D]** диалог меняет имя камеры вызовами `pc.SetCamera` на отдельных узлах.
- **[F:M L40135–40138]** `OnDialogEnd` вызывает `touretteDialogueResults()`; **[F:P L364–375]** эта функция обрабатывает флаги исхода сцены. Это НЕ доказывает, что кинематографическая камера всё время продолжает работать после начала DLG.

**[?]** Перечисленные времена — относительные задержки *разных I/O*, а не абсолютная временная шкала сцены. Длительность анимаций, переходы между кадрами и задержка загрузки диалога без наблюдения движка неизвестны.

## 5. Где стоят `SetCamera` в DLG

![[SM-13_Asylum_Assets/SM-13_Tourette_07_DLG_Camera_Cue_Map.png]]

| Имя камеры | Число появлений | Доказательность |
|---|---:|---|
| `tTherese` | **45** | Вызовы есть в DLG; определения ракурса нет в предоставленном CameraShotTable |
| `tJeanette` | **44** | Аналогично |
| `Tourette` | **3** | Вызовы DLG: узлы `1`, `11`, `921`; профиль `Tourette` присутствует в `Tourette.txt` |
| `DialogDefault` | **4** | Вызовы DLG: `711`, `741`, `751`, `781`; общий профиль не входит в файл `Tourette.txt` |

**[F:D]** Группы узлов дают широкую разметку ракурсов и для ранней ссоры, и для поздних разговоров. Примеры: `1 → Tourette`, `5 → tJeanette`, `7 → tTherese`, `11 → Tourette`; `711/741/751/781 → DialogDefault`. Это **не утверждение, что эти узлы проигрываются в таком порядке в одном прохождении**.

**[I]** Практически симметричное число обращений к `tTherese/tJeanette` согласуется с диалогом, построенным как чередование выступлений двух персонажей. Данные подтверждают намерение смены именованных ракурсов, но не реальные размеры планов (крупный/общий), углы, положение и монтажную скорость.

**[F:D]** В поле скрипта некоторых NPC-узлов стоит конструкция `pc.SetCamera("tTherese") or npc.SetDisposition(...)`. Без сведений о возвращаемых значениях этих методов нельзя доказать, что обе операции всегда исполняются: в Python `or` выполняет правый операнд условно. **Не считать автоматическим гарантированным выполнением `SetDisposition`.**

## 6. Уточнение к SM-13.09

Фраза «две камеры» в предыдущем исследовании была слишком упрощённой. **[F:M + F:C + F:D]** Мы различаем: (1) объект `camera_cinematic` перед диалогом, (2) профиль `Tourette` из `Tourette.txt` как камера NPC, (3) именованные вызовы `tTherese`/`tJeanette`, для которых здесь нет определений, (4) общий `DialogDefault`. Это разные сущности и типы ссылок; нельзя приравнивать их друг к другу.

## 7. Нерешённые вопросы и нужные исходники

1. **[?]** Как определены `tTherese` и `tJeanette`? Они есть в DLG, но не в текущем `Tourette.txt` или именах сущностей предоставленного VMF. Не утверждать, что это обязательно одноимённые `.txt`-файлы: возможны другие механизмы регистрации.
2. **[?]** `LookAtTarget_Snap.txt` — **точно указан** в VMF как `shotname` для `tourette_cam`, но не загружен. Он важнее следующей произвольной карты для понимания вступительного кадра.
3. **[?]** Как движок интерпретирует `DialogPOV`, `Follow`, `MaxTurnRate`, `SyncRotateOnMove` и координатные оси смещения? Требуется техническая документация или наблюдение камеры в игре.
4. **[?]** Как реально выглядит пространство кадра при двух именах `tTherese` и `tJeanette` (дистанция, направление взгляда, освещение, монтаж)? Проверить после исследования настроек.

### Следующий точный источник

`vdata/CameraShots/LookAtTarget_Snap.txt` — ссылка на файл обнаружена непосредственно в `sm_asylum_1.vmf` [F:M L43078]. Кроме того, полезен **список файлов/имён** в папке `vdata/CameraShots` для поиска определения `tTherese` / `tJeanette`, без угадывания имён.

## 8. Приложения и воспроизводимость

- [[SM-13_Asylum_Assets/SM-13_Tourette_Camera_Cues.csv]] — все **96** вызовов `SetCamera` с DLG ID и ссылкой на физическую строку DLG.
- [[SM-13_Asylum_Assets/SM-13_Tourette_Camera_Parameters.csv]] — все поля CameraShotTable.
- Для точной идентификации исходников SHA-256 записаны в YAML. Исходники читаются как предоставленная пользователем редакция; отсутствие некоторых полей нельзя трактовать как отсутствие их реализаций в игровом движке.

**Никакого проектирования или реализации ремейка в этом исследовании нет.**
