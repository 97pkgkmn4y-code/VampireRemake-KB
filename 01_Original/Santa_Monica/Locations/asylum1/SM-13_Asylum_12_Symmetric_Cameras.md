---
id: SM-13-TOURETTE-SYMMETRIC-CAMERAS
map: sm_asylum_1
location: 01_Original/Santa_Monica/Locations/asylum1
status: camera-profiles + SDK-how-to + DLG + VMF + Python cross-checked; runtime-unverified
sources:
  - vdata/CameraShots/ttherese.txt
  - vdata/CameraShots/tjeanette.txt
  - vdata/CameraShots/camera shots how-to.txt
  - vdata/CameraShots/tourette.txt
  - vdata/CameraShots/lookattarget_snap.txt
  - dlg/Santa Monica/Tourette.dlg
  - sm_asylum_1.vmf
  - santamonica.py
tags: [vtmb, original, santa-monica, asylum, cameras, cinematography, evidence, reverse-engineering]
---
# SM-13.12 — Tourette: зеркальные камеры сестёр и техническая инструкция SDK

> [!abstract] Предмет и уровень доказательности
> **Только оригинальный Asylum (Unofficial Patch Plus)**. Это дополнение к [[SM-13_Asylum_09_Tourette_Dialogue]], [[SM-13_Asylum_10_Camera_Direction]] и [[SM-13_Asylum_11_Camera_Shot_Bindings]]. Не проектируем ремейк.
>
> **[F:T]** — `ttherese.txt`; **[F:J]** — `tjeanette.txt`; **[F:H]** — `camera shots how-to.txt` (SDK); **[F:D]** — `tourette.dlg`, номера *узлов/физических строк*; **[F:M]** — `sm_asylum_1.vmf`, номера физических строк; **[F:P]** — `santamonica.py`; **[F:O]** — ранее изученные `tourette.txt` и `lookattarget_snap.txt`. **[I]** — интерпретация конфигурации и геймдизайна; **[?]** — неизвестно без наблюдения/движка. **Ни одна картосхема ниже не является снятым в игре кадром.**

## 1. Источники и проверка целостности

| Файл | SHA-256 |
|---|---|
| `ttherese.txt` | `7cf7ffeccb7db44c995f21421bda40c502ee714f9dd53feaa1542c560f445a0e` |
| `tjeanette.txt` | `3856d533d5f42cfb6980f348df0ba2289697ad61de777d141e176490e5e668eb` |
| `camera shots how-to.txt` | `a73f72b744a3a5993678e944b74d7bec1ca25fbbdc85bd2b7dcc90c5e707ff8b` |
| `tourette.txt` | `dafe2e60311f896498ff811199895de0055a058b6414d81f8f6dced6bd30b72f` |
| `lookattarget_snap.txt` | `61fade93192299349b294ee9e443ebc45c9365122105d11c99717489765ba169` |
| `tourette.dlg` | `9c49561f8cf51c160260c56d9a5cec06669912bf487c6055183db1037708b5fb` |
| `sm_asylum_1.vmf` | `6b637179bf6997e5441eaaf9d211e3ae3a52b3d9d3ebdd5d52f2a8b665c198e0` |
| `santamonica(1).py` | `5f62a97ba59c997fdc5df6befe9203f8d28e6261001b35d7b98f3aecc6c3daf4` |

**[F:T,J]** Оба CameraShotTable содержат по одному профилю (`tTherese` и `tJeanette`). Их поля, кроме `End.OffsetOrigin`, **совпадают полностью**. Сравнение произведено по вложенным ключам, а не по приблизительному пересказу.

**[F:D]** Статический разбор `Tourette.dlg`: 949 слотов, **96** записей с `pc.SetCamera()` — `tTherese=45`, `tJeanette=44`, `Tourette=3`, `DialogDefault=4`. Все 96 в полученном файле расположены в **поле условия**, не в поле прямого действия. Это не означает, что за одно прохождение игрок увидит 96 смен камер.

## 2. Профили tTherese и tJeanette: точные совпадения

![[SM-13_Asylum_Assets/SM-13_Tourette_14_Profile_Comparison.png]]

| Параметр | `tTherese` | `tJeanette` | Источник |
|---|---|---|---|
| `End.Position` | `DialogTarget` | `DialogTarget` | [F:T,J L8] |
| `End.AttachPos` | `Origin` | `Origin` | [F:T,J L9] |
| `End.AttachType` | `Follow` | `Follow` | [F:T,J L10] |
| **`End.OffsetOrigin`** | **`[21, -13, 59]`** | **`[21, 13, 59]`** | [F:T,J L11] |
| `Target.Point1.Position` | `DialogTarget` | `DialogTarget` | [F:T,J L18] |
| `Target.Point1.AttachPos` | `Bone: Bip01 Neck` | `Bone: Bip01 Neck` | [F:T,J L19] |
| `Target.Point1.AttachType` | `None` | `None` | [F:T,J L20] |
| `MoveSpeed` | 500 | 500 | [F:T,J L27] |
| `MoveAccel` | 250 | 250 | [F:T,J L28] |
| `TurnAccel` | 30 | 30 | [F:T,J L29] |
| `MaxTurnRate` | `[60, 60, 60]` | `[60, 60, 60]` | [F:T,J L30] |
| `DistanceTolerance` | 7 | 7 | [F:T,J L31] |
| `AngularTolerance` | `[5, 5, 5]` | `[5, 5, 5]` | [F:T,J L32] |
| `FieldOfView` | 75 | 75 | [F:T,J L33] |
| `DialogPOV` | 0 | 0 | [F:T,J L34] |
| `SnapOnShotChange` | 1 | 1 | [F:T,J L35] |

**[F]** Единственное различие — **знак второй компоненты** `OffsetOrigin`. `[21,-13,59]` и `[21,+13,59]` — **смещения от опоры в её локальной системе**, а не абсолютные XYZ в здании.

## 3. Локальная пространственная схема: почему камера зеркалится

![[SM-13_Asylum_Assets/SM-13_Tourette_11_Local_Mirror_Offsets.png]]

**[F:H L50–54]** SDK объясняет `OffsetOrigin` как вектор `[X,Y,Z]` и предлагает читать его как `[вперёд/назад, вправо/влево, вверх/вниз]`. В примере `[40,-10,25]` число `-10` описано как **10 единиц влево**. Значит, у tTherese `[21,-13,59]` задаёт локальный левый сдвиг, а у tJeanette `[21,+13,59]` — зеркальный правый (при той же ориентации опоры).

**[F:H L44–48]** `Follow` означает слежение за позицией опоры с преобразованием смещения относительно направления, в которое опора обращена. В связи с этим зеркальность **строго локальная**. Нельзя поставить эти камеры на карту Asylum по одним лишь трём числам — нужна ориентация NPC в соответствующем кадре и точное исполнение движком.

**[F:T,J L18–20]** Обе камеры наводятся на `Bone: Bip01 Neck` той же `DialogTarget`. На схеме цель взгляда показана схематически в центре, но не утверждается, что шею можно математически приравнять к origin объекта.

## 4. Точная семантика, которую даёт SDK

| Фрагмент `camera shots how-to.txt` | Подтверждённое правило | Следствие/ограничение |
|---|---|---|
| L6–8 | Без `Start` камера берёт текущую позицию; для новой без позиции — стандартную камеру игрока | В обоих профилях **нет** секции `Start`; старт не задан фиксированной точкой |
| L10 | Без `End` камера не перемещается между точками | В обеих есть `End` с `DialogTarget` |
| L15–16 | При заданных `Start` и `End` камера движется к `End` каждый кадр | Инструкция **не расписывает** конкретно сочетание «только `End` + `SnapOnShotChange`» |
| L18–19 | Один Target задаёт наведение на него каждый кадр; два — на среднюю точку | В обеих ровно `Point1` |
| L28–32 | `DialogTarget` — NPC разговора | Мировая точка определяется текущим NPC, а не именем файла |
| L34–48 | `AttachType=Follow` поворачивает смещение относительно направления опоры | Камера может следовать за движением NPC |
| L50–54 | Смещение задаётся трёхкомпонентным вектором в единицах SDK | `−13`/`+13` определяют разные локальные стороны |
| L94–105 | `MoveSpeed`, `MoveAccel`, `FieldOfView`, допуски и `DialogPOV` документированы | Можно трактовать значения, но не рассчитывать точные кадры без движка |
| L104 | `DialogPOV=1`: NPC смотрит в камеру вместо глаз игрока | У двух сестринских профилей `0`; **принудительный взгляд в камеру не включён** |

**[важная граница]** `SnapOnShotChange` **в показанной SDK-инструкции не определён**. Поэтому мы не приравниваем `1` к доказанному мгновенному перемещению без анимации. Точное взаимодействие с `MoveSpeed`, `Start` и `End` остаётся **[?]**.

**[важная граница]** `AttachType=None` у `Target.Point1` по SDK означает «поставить в точку и не следовать» [F:H L47]; это отдельная настройка точки наведения, в то время как у позиции камеры стоит `Follow`. Нельзя подменять одно другим и утверждать, что взгляд непрерывно следует за анимированной шеей без проверки.

## 5. Сопоставление с Tourette.dlg: два голоса, одна NPC-сущность

![[SM-13_Asylum_Assets/SM-13_Tourette_15_Voice_Shot_Examples.png]]

**[F:P L321–330]** В соответствующей ветке `populateOffice()` вызываются `jeanette.ScriptHide()`, `tourette.ScriptUnhide()`, `therese.ScriptHide()`, активируется `tourette_trigger`. Выбор этой ветки зависит от `G.Therese_Quest == 4`, других флагов и приоритета предыдущих `if/elif`; **не является гарантированным** при любом состоянии с `Therese_Quest=4`.

**[F:M L40080–40144]** В VMF есть NPC с именем `Tourette`, `default_camera = vdata/CameraShots/Tourette.txt` и `dialogname = dlg/Santa Monica/Tourette.dlg`.

**[F:D]** В предоставленном DLG реплики разных голосов содержат назначение камер:

| ID узла | Чей текст | Вызов камеры |
|---:|---|---|
| 1 | `[Therese]` | `Tourette` |
| 5 | `[Jeanette]` | `tJeanette` |
| 7 | `[Therese]` | `tTherese` |
| 15 | `[Therese]` | `tTherese` |
| 17 | `[Jeanette]` | `tJeanette` |
| 21 | `[Jeanette]` | `tJeanette` |
| 25 | `[Therese]` | `tTherese` |
| 921 | нейтральная реакция Tourette | `Tourette` |

**[I]** При условии, что целевой NPC — `Tourette`, две камеры создают два противоположно смещённых ракурса **одной актёрской сущности**. Такая геометрическая организация поддерживает постановочное разделение Therese и Jeanette, не требуя двух одновременно стоящих NPC-моделей. Это **причинно обоснованная интерпретация замысла**, а не зарегистрированные кадры из игры.

**[F:D]** Все **96** вызовов расположены в поле *условия*, например `pc.SetCamera("tTherese") or npc.SetDisposition("neutral",1)`. В Python `or` условно вычисляет правую часть; без точного возвращаемого значения `SetCamera` нельзя гарантировать, что `SetDisposition` всегда вызывается. Предыдущие заметки правильно оставляли этот вопрос открытым.

## 6. Картосхемы режиссуры и распределения вызовов

![[SM-13_Asylum_Assets/SM-13_Tourette_12_Stage_Camera_Chain.png]]

**[F:M L39923–39944, L40052–40079]** Начальная постановка использует `tourette_trigger` → `tourette_cam.StartShot` и анимации; после окончания `Tourette_point_gun` запускается `Tourette.StartPlayerDialog` (задержка 0,3 с от `OnEndSequence`). `tourette_cam` использует `LookAtTarget_Snap`; NPC использует `Tourette.txt` как `default_camera`, а в DLG встречаются `tTherese`/`tJeanette`. **Не смешивать `camera_cinematic` и `default_camera` NPC.**

![[SM-13_Asylum_Assets/SM-13_Tourette_13_DLG_Camera_Cues.png]]

Распределение статических вызовов по номерам узлов (источник DLG): `tTherese` 45, `tJeanette` 44, `Tourette` 3, `DialogDefault` 4. **Горизонтальная ось — ID, не реальное время.** Пример распределения не означает, что все узлы достижимы в одном диалоге.

## 7. Сопоставление четырёх профилей (важные контрасты)

- **[F:O] `Tourette`** — `OffsetOrigin=[48,0,53]`, цель `Bip01 Head`, `FieldOfView=40`, `DialogPOV=1`, `SyncRotateOnMove=1`.
- **[F:T,J] `tTherese/tJeanette`** — зеркальные `[21,±13,59]`, цель `Bip01 Neck`, `FieldOfView=75`, `DialogPOV=0`, `SnapOnShotChange=1`.
- **[F:O] `LookAtTarget_Snap`** — `End.Position=Named`, `Target.Position=Named`, `FieldOfView=75`, `DialogPOV=1`, `SnapOnShotChange=1`. Именованные опоры задаёт `tourette_cam` из VMF.

**[I]** Оригинал различает более тесную фронтальную композицию Tourette (FOV 40) и более широкие противоположные боковые композиции сестёр (FOV 75). Реальный план, фокусное ощущение и ось FOV по текстам не восстановлены — это не снятые изображения.

## 8. Геймдизайнерская и режиссёрская интерпретация — только оригинал

1. **[I] Конфликт кодируется направлением взгляда.** Одним небольшим изменением Y от `−13` до `+13` режиссура меняет сторону, с которой мы наблюдаем одну диалоговую цель. Это поддерживает восприятие двух конфликтующих говорящих, не доказывая автоматического монтажа.
2. **[I] Подстановка голоса на единую актёрскую сущность.** DLG помечает реплики двумя именами, а локационная ветка показывает `Tourette` вместо отдельных Jeanette/Therese. Анимация и камера работают как разные слои представления того, кто «говорит».
3. **[I] Отделение вступительной сцены от управляемого диалога.** Отдельные `camera_cinematic`, NPC `default_camera` и именные `SetCamera` позволяют сочетать постановочный вход и ветвящийся диалог. Нельзя восстановить монтаж по одним только числовым ID DLG.
4. **[F:H + I] Стабилизация кадра и точки наведения.** SDK описывает допуски `DistanceTolerance/AngularTolerance`; у сестринских профилей они равны 7 и `[5,5,5]`. Их назначение — избежать мелких движений при следовании. Но реальную амплитуду дрожания/поворотов в сцене без запуска не оценить.

## 9. Что скорректировать в старых исследованиях

- В [[SM-13_Asylum_10_Camera_Direction]] имена `tTherese/tJeanette` теперь **разрешены**: отдельные файлы действительно содержат совпадающие внутренние `ShotName`.
- В [[SM-13_Asylum_11_Camera_Shot_Bindings]] вопрос о механизме именованных камер сестёр закрыт в части CameraShotTable. Точный визуальный результат по-прежнему **не верифицирован движком**.
- Мы больше не называем зеркальные числовые смещения **абсолютными координатами в комнате**.
- По SDK можно подтверждённо толковать `DialogPOV=1`, `Follow`, оси смещения и смысл допусков; `SnapOnShotChange` остаётся открытым.

## 10. Незакрытые вопросы и минимальная проверка

1. **[?]** Точная реализация `SnapOnShotChange` и его сочетания с отсутствующей секцией `Start`.
2. **[?]** Меняется ли мгновенно фактическое положение камеры при каждой реплике; как движок учитывает ориентацию `Tourette` и анимацию модели.
3. **[?]** В какие моменты и по каким веткам игрок действительно видит профиль `Tourette` с FOV 40 вместо двух боковых shot'ов.
4. **[?]** Меняется ли направление взгляда NPC при `DialogPOV=0` из-за другого игрового поведения, не описанного CameraShotTable.
5. **[?]** Визуально подтвердить композицию и переходы можно короткой записью/скриншотами **только если это станет необходимо**. Для технической схемы текущих файлов уже достаточно.

## 11. Вложения и ссылки

- [[SM-13_Asylum_Assets/SM-13_Tourette_11_Local_Mirror_Offsets.png]] / `.svg` — **локальная**, а не мировая координатная схема двух ракурсов.
- [[SM-13_Asylum_Assets/SM-13_Tourette_12_Stage_Camera_Chain.png]] / `.svg` / `.dot` — цепочка Python → VMF → DLG → CameraShotTable.
- [[SM-13_Asylum_Assets/SM-13_Tourette_13_DLG_Camera_Cues.png]] / `.svg` — 96 статических вызовов.
- [[SM-13_Asylum_Assets/SM-13_Tourette_14_Profile_Comparison.png]] / `.svg` — буквальные различия профилей.
- [[SM-13_Asylum_Assets/SM-13_Tourette_15_Voice_Shot_Examples.png]] / `.svg` / `.dot` — примеры назначения камеры по говорящему.
- [[SM-13_Asylum_Assets/SM-13_Tourette_Profiles_Verbatim.csv]] — все извлечённые параметры четырёх профилей.
- [[SM-13_Asylum_Assets/SM-13_Tourette_12_Camera_Cues.csv]] — 96 привязок ID → имя shot → выражение.

Следующим объектом в Asylum разумно исследовать **звуковую режиссуру** (музыка, ambience, разделение публичных/частных зон) или **второстепенных NPC**, а не снова запрашивать материалы, уже достаточные для закрытия камер.
