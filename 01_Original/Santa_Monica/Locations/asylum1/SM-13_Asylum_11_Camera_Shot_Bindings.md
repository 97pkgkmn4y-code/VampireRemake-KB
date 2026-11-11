---
id: SM-13-TOURETTE-CAMERA-BINDINGS
location: Santa_Monica/Locations/asylum1
original_map: sm_asylum_1
status: source-crosschecked; runtime-unverified
sources:
  - sm_asylum_1.vmf
  - vdata/CameraShots/LookAtTarget_Snap.txt
  - vdata/CameraShots/Tourette.txt
  - dlg/Santa Monica/Tourette.dlg
  - santamonica.py
tags: [vtmb, original, asylum, santa-monica, reverse-engineering, camera, direction]
sha256_LookAtTarget_Snap_txt: 61fade93192299349b294ee9e443ebc45c9365122105d11c99717489765ba169
sha256_Tourette_txt: dafe2e60311f896498ff811199895de0055a058b6414d81f8f6dced6bd30b72f
sha256_VMF: 6b637179bf6997e5441eaaf9d211e3ae3a52b3d9d3ebdd5d52f2a8b665c198e0
---
# SM-13.11 — Tourette: именованные привязки и переход от кино-камеры к диалогу

> [!abstract] Область исследования
> Дополнение к [[SM-13_Asylum_10_Camera_Direction]]. Исследуется **оригинальный Asylum Unofficial Patch Plus**, без проектирования ремейка. **[F:VMF]** — подтверждено `sm_asylum_1.vmf`; **[F:S]** — `LookAtTarget_Snap.txt`; **[F:T]** — `Tourette.txt`; **[F:D]** — `tourette.dlg`; **[I]** — интерпретация; **[?]** — не установлено.
>
> Важное ограничение: два `CameraShotTable` сравниваются как конфигурации, но кадр и движение камеры **не воспроизводились в игре**.

## 1. Что именно закрыто новым файлом

**[F:VMF, физические строки 43071–43088]** Сущность `camera_cinematic` с именем `tourette_cam` содержит `shotname = vdata/CameraShots/LookAtTarget_Snap.txt`. Теперь мы получили именно этот файл, который не был доступен при подготовке [[SM-13_Asylum_10_Camera_Direction]].

**[F:S, строки 1–38]** Файл содержит **один** профиль `LookAtTarget_Snap`, внутри которого определены `End`, `Target/Point1` и `CameraConstraints`.

**[F:VMF, строки 40080–40144]** Отдельно NPC `Tourette` использует `default_camera = vdata/CameraShots/Tourette.txt` и `dialogname = dlg/Santa Monica/Tourette.dlg`. **Не путать** параметр `shotname` у `camera_cinematic` с `default_camera` NPC.

## 2. Карта связывания имён и параметров

![[SM-13_Asylum_Assets/SM-13_Tourette_08_Named_Camera_Bindings.png]]

**[F:VMF]** У `tourette_cam` прямо указаны:

```text
classname = camera_cinematic
targetname = tourette_cam
shotname = vdata/CameraShots/LookAtTarget_Snap.txt
startent = tourette_cam
endent = tourette_cam
target1 = Tourette
target2 = Tourette
origin = -926.084 641.364 67.7361
```

**[F:S, строки 7–21]** Позиция камеры (`End`) и цель (`Target/Point1`) используют `Position = Named`, `AttachPos = Origin`, `AttachType = Follow`. В самом `.txt` *не названы* ни `tourette_cam`, ни `Tourette`: именованные ссылки берутся из конфигурации конкретной сущности в VMF.

**[I]** Связка указывает на камеру, пространственно привязанную к именованной опорной сущности и наводимую на именованную цель. При одинаковых `startent` и `endent`, а также `target1` и `target2`, статическая конфигурация не предписывает разных начала/конца пути или разных целей.

**[?]** Нельзя утверждать, что камера совершенно неподвижна: `Follow` может давать зависимость от перемещения целевой сущности; не исследованы интерпретация переходов между shot'ами, поведение анимаций, длительность кадра и скрытые настройки движка.

## 3. Объективная таблица сравнения

![[SM-13_Asylum_Assets/SM-13_Tourette_09_Camera_Profile_Comparison.png]]

| Характеристика | `LookAtTarget_Snap` | `Tourette` | Основание |
|---|---|---|---|
| Секция `End` — `Position` | `Named` | `DialogTarget` | [F:S L9] [F:T L8] |
| Секция `End` — `AttachPos` | `Origin` | `Origin` | [F:S L10] [F:T L9] |
| Секция `End` — `AttachType` | `Follow` | `Follow` | [F:S L11] [F:T L10] |
| Секция `End` — `OffsetOrigin` | не указан | `[48, 0, 53]` | [F:S] [F:T L11] |
| `Target/Point1` — `Position` | `Named` | `DialogTarget` | [F:S L18] [F:T L18] |
| `Target/Point1` — `AttachPos` | `Origin` | `Bone: Bip01 Head` | [F:S L19] [F:T L19] |
| `Target/Point1` — `AttachType` | `Follow` | `None` | [F:S L20] [F:T L20] |
| `MoveSpeed` | `250` | `500` | [F:S L28] [F:T L27] |
| `MoveAccel` | `100.0` | `250` | [F:S L26] [F:T L28] |
| `TurnAccel` | `60` | `30` | [F:S L27] [F:T L29] |
| `MaxTurnRate` | `[60,60,60]` | `[60,60,60]` | [F:S L29] [F:T L30] |
| `DistanceTolerance` | `5` | `5` | [F:S L30] [F:T L31] |
| `AngularTolerance` | `[5,5,5]` | `[7,7,7]` | [F:S L31] [F:T L32] |
| `FieldOfView` | **75** | **40** | [F:S L32] [F:T L33] |
| `DialogPOV` | `1` | `1` | [F:S L33] [F:T L34] |
| `SnapOnShotChange` | **1** | не указан | [F:S L34] |
| `SyncRotateOnMove` | не указан | **1** | [F:T L35] |

**[F]** Отсутствие параметра означает только, что он **не записан в этом профиле** — нельзя автоматически подставлять `0`.

**[I]** При одинаковой трактовке FOV `75` шире `40`: композиция потенциально переключается от обзорной сцены к более узкому диалоговому плану. Но физическая дистанция до лица NPC и итоговый кадр неизвестны. `SnapOnShotChange = 1` согласуется с идеей резкой смены кадра, однако значение этого ключа по названию **не доказывает**, что в игре нет интерполяции или дополнительной задержки.

## 4. Точные координатные опоры

![[SM-13_Asylum_Assets/SM-13_Tourette_10_Camera_Anchor_Map.png]]

| Сущность | Origin в VMF | Роль |
|---|---|---|
| `tourette_trigger` | `(-929.940, 693.370, 36.550)` | активирующая зона `[F:VMF L39923–39944]` |
| `tourette_cam` | `(-926.084, 641.364, 67.7361)` | позиционная опора `camera_cinematic` `[F:VMF L43071–43088]` |
| `player_to_tourette` | `(-932.865, 557.017, -14.8927)` | скриптовая последовательность игрока `[F:VMF]` |
| `Tourette` | `(-906.727, 452.287, -13.4556)` | именованная цель `target1/target2` `[F:VMF L40080–40144]` |

> [!warning] Что не показывает карта
> Подпись `target1/target2 = Tourette` — **логическая ссылка**, не проверка прямой видимости. Схема изображает горизонтальную проекцию XY; высоты Z могут различаться. Мы **не реконструировали точный угол обзора, occlusion или итоговый кадр**.

## 5. Условия запуска и порядок событий

**[F:VMF L39923–39944]** При `tourette_trigger.OnStartTouch` запланировано `tourette_cam.StartShot` с задержкой **0.4 с**; параллельно вызываются `tourette_control_player.CreateControllerNPC` (+0.4 с), `player_to_tourette.BeginSequence` (+0.6 с), `Tourette_point_gun.BeginSequence` (+2.0 с) и `Tourette_thirtyeight.ScriptUnhide` (+0.2 с).

**[F:VMF L40052–40079]** `Tourette_point_gun.OnEndSequence` вызывает `Tourette.StartPlayerDialog` с задержкой +0.3 с и освобождает `tourette_control_player`. **Только затем** DLG может обрабатывать свои `pc.SetCamera()` — это ожидаемая причинная последовательность по указанным событиям, но реальная диспетчеризация движка не проверена.

**[F:DLG]** Смена `SetCamera` на `tTherese` и `tJeanette` содержится в диалоговых узлах; их профилей **нет** ни в предоставленном `LookAtTarget_Snap.txt`, ни в `Tourette.txt`.

**[F:Python L321–330]** Функция `populateOffice()` включает `tourette_trigger` при одной из веток `G.Therese_Quest == 4` и других проверках (с учётом порядка предыдущих `if/elif`). Это не гарантирует, что любой игрок, достигший значения 4, обязательно запустит сцену.

## 6. Техническая интерпретация: зачем такой расклад

- **[I] Разделение сцены и диалога.** `camera_cinematic` и NPC `default_camera` — независимые части постановки. Первая реагирует на триггер, вторая относится к режиму разговора.
- **[I] Более широкий установочный кадр против узкого портретного.** FOV 75 vs 40 поддерживает такое прочтение, но не даёт точного размера плана без движка.
- **[I] Приоритет лица в диалоге.** `Bip01 Head` как точка наведения NPC-профиля повышает вероятность центрирования лица, в отличие от именованного `Origin` у первой камеры. Это не доказательство результата на экране.
- **[I] Обработка актёрской анимации.** Привязка разговора к `OnEndSequence`, а не фиксированному общему таймеру, позволяет сцене завершать анимацию прежде чем начинать диалог. Анимацию не проигрывали, поэтому реальные секунды не названы.

## 7. Открытые вопросы

1. **[?]** Как именно Source/Vampire-движок интерпретирует `SnapOnShotChange`, `DialogPOV`, `Follow`, `Named`, значения толерантности и FOV? В присланных текстовых файлах реализация не содержится.
2. **[?]** Как определяются именованные камеры `tTherese` и `tJeanette` из `tourette.dlg`? Они не описаны в этих двух `CameraShotTable` и не встречаются в именах VMF-сущностей, найденных текстовым поиском. Это не доказывает их отсутствия в игре.
3. **[?]** Что на самом деле видно на кадре во время вступления и каждого диалогового переключения? Нужна проверка в игре или точная документация движка.
4. **[?]** Нет ли глобальных/стандартных переопределений камеры и дополнительных режимов, которые применяются при загрузке сцены?

### Следующий источник

Полезнее всего **листинг каталога `vdata/CameraShots/`** (имена всех `.txt`) и, если там обнаружатся совпадения, профили для `tTherese` и `tJeanette`. Не следует придумывать имена файлов по одной строке DLG.

## 8. Вложения

- [[SM-13_Asylum_Assets/SM-13_Tourette_Shot_Profile_Diff.csv]] — буквально сопоставленные ключи обоих профилей.
- [[SM-13_Asylum_Assets/SM-13_Tourette_Shot_Bindings.csv]] — связи и события VMF с координатами и строками источника.
- Исходный `lookattarget_snap.txt` (SHA-256 выше) сохранён как основание сравнения, но не копируется в материалы проекта автоматически.
