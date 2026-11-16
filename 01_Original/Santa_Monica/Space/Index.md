# Santa Monica — пространство района

- [[Surface]] — существующий свод по поверхности, улицам, пирсу, Beach House и связям карт. Материал имеет неоднородную версионную основу; см. ограничения в [[../Santa_Monica_Research_Index|главном индексе]].
- [[Sewers]] — существующая заметка о канализационных переходах и связи с Ocean House.
- [[Transitions]] — реестр 65 загрузочных переходов из entity lump 22 установленных BSP и его ограничения.
- [[Runtime_Verification]] — контрольные состояния, действия и критерии для игровых проверок.
- [[Santa_Monica_BSP_Brush_Routes.csv]] — 54 базовые пробы на 22 установленных BSP и 47 дополнительных проб с рельефом, PHY, переключаемыми брашами и разными размерами корпуса.

## Проверка геометрии по коллизионным брашам

[Скрипт проверки](../../../Research/trace_bsp_brush_route.py) читает `planes → nodes/leaves → leafbrushes → brushes/brushsides` модели `*0` установленного VBSP v17. В расчёте есть world brushes с битами solid, window, grate и playerclip. Команда `--brush-model` добавляет выбранную модель с перемещением в указанную точку. Для сравнения ниже использованы неподвижные двери без ненулевой исходной ориентации. Значения contents сопоставлены с [публичным заголовком Valve](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/public/bspflags.h).

В каждой пробе вертикальный луч с объёмом ставит ноги на опору. Дальше поиск шагает по сетке, проверяя непрерывным sweep AABB `32×32×72` каждый горизонтальный сегмент и подъём/спуск до 18 units. Эти размеры — параметры измерения. CSV хранит начальную и конечную пробы, найденные положения на опоре, SHA, координаты добавленной модели и параметры сетки. Значения `route_found` доказывают существование проверенной последовательности шагов для этой выборки брашей. `no_route_in_sample` означает исчерпание заданной сетки, `ungrounded` означает недоступную опору у входной координаты, `limit` означает исчерпанный лимит поиска.

Пример запуска из корня Vault:

```powershell
python Research/trace_bsp_brush_route.py "../Vampire - The Masquerade Bloodlines/Unofficial_Patch/maps/sm_vamparena.bsp" --start -112 -633 32 --finish -129 151 32 --margin 140 --limit 12000
```

Для пробы с закрытой дверью добавить `--brush-model 1 -137 -400.5 54`. Для границ лестничных брашей использовать `--ladder-bounds` без координат маршрута.

### Рельеф и выбранные модели

`--terrain` восстанавливает треугольники рельефа из BSP v17. Скрипт читает грани, их рёбра и вершины, параметры displacement, смещения и флаги треугольников. Для sweep корпуса каждый треугольник используется как конечная двусторонняя поверхность. Для опоры по умолчанию требуется Z-компонента нормали не ниже 0,7. По умолчанию `--goal-directed` выбирает положения ближе к концу по манхэттенскому расстоянию. [Структуры BSP в Source SDK](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/public/bspfile.h)

`--decoded-physics <json>` и повторяемый `--physics-prop <MDL_PATH> <X> <Y> <Z> <YAW>` добавляют выпуклые секции PHY моделей с проверенной единичной корневой костью. Координаты IVP переводятся в Source как `(x, z, −y) / 0.0254`, затем применяется yaw и перенос. Трансформации pitch, roll и подвижных костей здесь не моделируются. Для набора `pier-walkways` взять [[Surface#Коллизия подъёма к Beach House|пять размещений и три ресурса]].

Воспроизведение декодирования в соседнем VampireRemake-Starter. Для каждого из трёх ресурсов проверить loose-версию в `Unofficial_Patch` и извлечь PHY из `Vampire/pack002.vpk` через SDK либо `Sources` из `UnityProject/VampireRemake/tools/export-map-geometry.py`. В файл заданий записать по одному объекту `{"path":"models/scenery/structural/pier/walkwaya.mdl","phy":"<абсолютный путь к PHY>"}` на ресурс. Запустить `UnityProject/VampireRemake/tools/read-bloodlines-physics.ps1` в 32-битном PowerShell из `SysWOW64` с параметрами `-SdkAssembly <игра>/SDKBinaries/tools/Crowbar/CroVtmb.exe -JobsFile <задания.json> -OutputFile <decoded.json>`. Перед применением новой модели сверить checksum с MDL и проверить корневую кость.

Дополнительные столбцы CSV задают число добавленных треугольников `displacement_triangles`, набор моделей `physics_model_set`, порядок поиска `goal_directed` и порог опоры `minimum_ground_normal`. Пустые поля базовых строк означают ноль треугольников, отсутствие PHY, обход в ширину и порог 0,7. Результаты относятся к заданным корпусу, сетке и включённой геометрии. Для движения по лестнице, подъёмников, прыжков, анимации дверей и игровых квестовых состояний нужны отдельные проверки.

Для новых проб `--hull-height` задаёт высоту корпуса, `--rise-increment` перебирает подъёмы от нуля до `--step`, `--max-drop` задаёт отдельный предел спуска. `--diagonal` добавляет диагональные сегменты и при `--goal-directed` сортирует позиции по евклидову расстоянию. `--bounds X_MIN X_MAX Y_MIN Y_MAX` задаёт область поиска вместо `--margin`. Пустые новые поля CSV означают исходную схему проб. Высота 36 и спуски 64 и 450 являются параметрами измерения.

```powershell
python Research/trace_bsp_brush_route.py "../Vampire - The Masquerade Bloodlines/Unofficial_Patch/maps/sm_beachhouse_1.bsp" --terrain --goal-directed --diagonal --grid 8 --step 18 --rise-increment 2 --max-drop 64 --limit 30000 --bounds 2670 3680 -2410 -1250 --start 3155.23 -1620.73 -102.144 --finish 3300 -2110 -90
```
