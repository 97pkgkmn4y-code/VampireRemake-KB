---
id: SM-26-SYSTEMS
map: sm_gallery_1
---
# SM-26.01 — Slashterpiece и постановка

## Входы, состояние и предметы

**Опорная планировка по UP BSP.** Центры переходов `(-8,-344,-104)` и `(277,271,-104)`, landmarks `(-9,-351,-151)` и `(284,270,-151)`. Пол у обоих переходов и под Guardian имеет Z=-160 (грани 407, 222, 332). Полотна стоят по четырём сторонам от центра `(16,-24)`: `painting_0=(-193.457,-241.544,-120.194)`, `painting_1=(184.094,-214.785,-127.746)`, `painting_2=(-218.342,229.144,-127.331)`, `painting_3=(160.008,222.327,-125.603)`. Координаты задают точки взаимодействия. Обход зала и удары требуют проверки в игре.

Два `trigger_changelevel` возвращают в `sm_hub_1`: `GalleryTeleport1` через landmark `gallery1`, `GalleryTeleport2` через `gallery2` (установленный BSP). В Hub имеются соответствующие два входа ([[../../Space/Transitions|реестр]]). Статический набор не устанавливает доступность обеих дверей в каждом состоянии.

`jeanette.dlg` ID 361 пишет `G.Jeanette_Refuse=0`, `G.Jeanette_Quest=1`, журнал `Slashterpiece=1`, выдаёт `item_w_knife`. Достижимость реплики и порядок диалога не симулировались. `gallery.py:65–94`: `paintingsInGallery()` показывает четыре картины при `Jeanette_Quest==1` либо `Jeanette_Refuse>0`; в Plus показывает `cash_box` и его маркер, в Basic использует другие entities; при `Jeanette_Refuse>0` либо `Jeanette_Quest==2` вызывает `gallery_done_relay`. `logic_auto.OnMapLoad` вызывает эту функцию и `disableGallerySecurity()`. Последняя выключает `camera_switch` только при `Jeanette_Quest==1` и достаточно благоприятном состоянии Chunk (`Chunk_Befriend>=2`, `Chunk_Dominated>=1` либо `Chunk_Demented==1`), `gallery.py:42–46`.

## Граф событий четырёх картин

В установленном BSP четыре `prop_slashable`, но индекс имени картины и аргумент функции **не совпадают**:

| Entity `OnSlashed` | Вызов | Табличка SDK VMF |
| --- | --- | --- |
| `painting_0` | `paintingSlashed(0)` | `noir_label_cain_slays` (L9909) |
| `painting_3` | `paintingSlashed(1)` | `noir_label_cain_curse` (L9753) |
| `painting_1` | `paintingSlashed(2)` | `noir_label_cain_meet` (L9987) |
| `painting_2` | `paintingSlashed(3)` | `noir_label_cain_spurn` (L9831) |

`gallery.py:48–49` на загрузке сбрасывает `G.SlashedPaintings`. `paintingSlashed(p)` (`gallery.py:97–114`) требует ранее отмеченные индексы `0…p-1`; нарушение вызывает `healPaintings()`, сбрасывает массив, запускает `painting_healer` и отнимает единицу крови. При `p==3` вызывается `summonBloodCreature() → summon_relay.Trigger`. Это порядок **аргументов событий**, а не вывод из расположения картин. Фактические коллизии и срабатывание ударов `RUNTIME PENDING`.

Четыре `signs` в UP BSP (`*9…*12`) совпадают по координатам с VMF-табличками. По world brushes проверен последовательный подход к картинам от `(-18,-339,-150)` через `(-162,-241,-120)`, `(146,193,-120)`, `(151,-215,-120)`, `(-184,229,-120)` до `(16,-24,-123)` у Guardian. Сетка 12, шаг 18, отступ 170, лимит 12000. Пять участков дали 21, 63, 35, 65 и 39 положений на полу Z=−159.95. Это проверка доступности позиций около картин с моделью 32×32×72. Дальность удара и активность полотен определяет игра.

## Guardian, камера и исход

В BSP `summon_relay.OnTrigger` запирает передние и заднюю двери, показывает Guardian с задержкой 10 s, запускает `guardian_attack` через 10.5 s, использует `summon_camera.PlayAsCameraPosition`, `summon_target.PlayAsCameraTarget` и восстанавливает управление камерой через 11 s; также включает частицы, звук `plus_blood_summon` и controller NPC. Это статическая режиссёрская цепь, реальный кадр и контроль игрока не наблюдались.

`BloodGuardian.OnDeath` вызывает `bloodGuardianDeath()`, отпирает дверные замки и запускает death particles (BSP I/O). Python `gallery.py:26–30` пишет журнал `Slashterpiece=2` и `G.Jeanette_Quest=2`. Отдельная `paintingsSlashed()` (`gallery.py:116–119`) делает те же две записи, но её вызывающую entity в выбранной цепочке пока не установили; поэтому нельзя считать её обязательным шагом. В Plus `cash_box.OnPlayerPickup → playerGotBox()`; `vamputil.py:1203–1212` при `Got_Cash==0` записывает флаг, добавляет 250 денег и при Humanity>=6 и `Charity_Know==0` снижает Humanity. В Basic `charity_monies.OnPressed → charityMoneyStolen()`; `gallery.py:33–40` также добавляет 250 денег и условно снижает Humanity. Это разные статические пути; их игровая доступность не проверена.

В базовом `sm_gallery_1.bsp` призыв и смерть адресуют `Lock/Unlock` непосредственно трём дверям. В установленном UP те же выходы адресуют правой створке `front_door_r` и двум ручкам `front_door_l_lock`, `back_door_lock`. Обе ручки класса `prop_doorknob`, `difficulty=10`. В `gallery_done_relay`, вызываемом при отказе или завершённом задании, есть удаление `summon_relay` и Guardian, смена skin картин, но нет `Unlock`. После штатной победы команда отпирания записана на самом `BloodGuardian.OnDeath`. Состояние дверей на повторной загрузке остаётся для проверки.
