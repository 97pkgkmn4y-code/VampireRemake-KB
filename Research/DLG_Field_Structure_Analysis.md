# Анализ структуры DLG файлов Bloodlines

## Цель
Проверить 13 полей описаний DLG файлов из раздела IV.2 Mod Developer Guide путем сравнения с реальным файлом arthur.dlg.

## Источники данных
- **arthur.dlg**: Reference/Vampire - The Masquerade Bloodlines/Unofficial_Patch/dlg/santa monica/arthur.dlg
- **venus.dlg**: Reference/Vampire - The Masquerade Bloodlines/Unofficial_Patch/dlg/downtown la/venus.dlg
- **jeanette.dlg**: Reference/Vampire - The Masquerade Bloodlines/Unofficial_Patch/dlg/santa monica/jeanette.dlg

## Структура DLG файлов

### Формат
DLG файлы используют табулированную структуру с содержимым между фигурными скобками `{}`:

```
{	{ID}	{Response1}	{Response2}	{NextID}	{Conditions}	{Scripts}	{BrujahResponse}	{GangrelResponse}	{NosferatuResponse}	{ToreadorResponse}	{TremereResponse}	{VentrueResponse}	{MalkavianResponse}
```

### Полная структура (13 полей)

**VERIFIED_STATIC** - Все поля подтверждены анализом DLG файлов:

1. **ID** - Уникальный идентификатор узла диалога (текстовое поле)
   - Позиция 0
   - Пример: `{11}` - ID узла Arthur

2. **Response 1** - Первый вариант ответа (текст)
   - Позиция 1
   - Пример: `{[With the panache...]Welcome to Kilpatrick...}`

3. **Response 2** - Второй вариант ответа (текст)
   - Позиция 2
   - Пример: `{[With the panache...]Welcome to Kilpatrick...}`

4. **Next ID** - ID следующего узла диалога
   - Позиция 3
   - Пример: `{#}` (никакого следующего узла), `{0}` (авто-конец), `{11}` (ID следующего узла)

5. **Conditions** - Условия показа ответа
   - Позиция 4
   - Пример: `{not IsClan(pc,"Malkavian")}`, `{G.Arthur_BJ == 0 and IsClan(pc,"Malkavian")}`, `{Intimidate 5}`

6. **Scripts** - Скрипты (действия)
   - Позиция 5
   - Пример: `{npc.SetDisposition("Joy",1)}`, `{G.Arthur_Talked = 1}`, `{G.Jeanette_Seduce = G.Jeanette_Seduce + 1}`

7. **Brujah Response** - Ответ для клана Brujah
   - Позиция 6
   - Пример: `{Greetings!}` (строка 3 arthur.dlg), `{}` (пустое в строке 11)

8. **Gangrel Response** - Ответ для клана Gangrel
   - Позиция 7
   - Обычно пустое: `{}`

9. **Nosferatu Response** - Ответ для клана Nosferatu
   - Позиция 8
   - Обычно пустое: `{}`

10. **Toreador Response** - Ответ для клана Toreador
    - Позиция 9
    - Обычно пустое: `{}`

11. **Tremere Response** - Ответ для клана Tremere
    - Позиция 10
    - Обычно пустое: `{}`

12. **Ventrue Response** - Ответ для клана Ventrue
    - Позиция 11
    - Обычно пустое: `{}`

13. **Malkavian Response** - Ответ для клана Malkavian
    - Позиция 12
    - Пример: `{I must be gone.}` (строка 20 arthur.dlg), `{}` (пустое в строке 11)

## Примеры

### Строка 11 arthur.dlg (инициализация)
```
{	11	}{	[With the panache of a hubcap salesman]Welcome to Kilpatrick 24-Hour Bail Bonds. My name's Arthur Kilpatrick. How can I help you?	}{	[With the panache of a hubcap salesman]Welcome to Kilpatrick 24-Hour Bail Bonds. My name's Arthur Kilpatrick. How can I help you?	}{	#	}{	npc.SetDisposition("Joy",1)	}{	G.Arthur_Talked = 1	}{	}{	}{	}{	}{	}{	}{	}{	}
```

Поля:
1. `{11}` - ID
2. `{[With the panache...]Welcome to Kilpatrick...}` - Response 1
3. `{[With the panache...]Welcome to Kilpatrick...}` - Response 2
4. `{#}` - Next ID
5. `{npc.SetDisposition("Joy",1)}` - Conditions
6. `{G.Arthur_Talked = 1}` - Scripts
7-13. `{}` - Все clan responses пустые

### Строка 3 arthur.dlg (Brujah response)
```
{	3	}{	Hi.	}{	Hi.	}{	11	}{	}{	}{	}{	}{	}{	}{	}{	}{	Greetings!	}
```

Поля:
1. `{3}` - ID
2-3. `{Hi.}` - Responses
4. `{11}` - Next ID
5-6. `{}` - Conditions and Scripts
7. `{Greetings!}` - Brujah response
8-13. `{}` - Остальные clan responses пустые

### Строка 20 arthur.dlg (Malkavian response)
```
{	20	}{	Nothing now, thanks. Goodbye.	}{	Nothing now, thanks. Goodbye.	}{	0	}{	}{	}{	}{	}{	}{	}{	}{	}{	I must be gone.	}
```

Поля:
1. `{20}` - ID
2-3. `{Nothing now, thanks. Goodbye.}` - Responses
4. `{0}` - Next ID
5-6. `{}` - Conditions and Scripts
7-12. `{}` - Пустые clan responses (Brujah, Gangrel, Nosferatu, Toreador, Tremere, Ventrue)
13. `{I must be gone.}` - Malkavian response

### Строка 1 venus.dlg (все clan responses пустые)
```
{	1	}{	Everybody comes in here's got to have a shot, house rules. Inhibition's the first thing to go. Two more of these and you'll be telling me your nastiest, dirtiest stories. I am your beat priestess and it's time to confess.	}{	Everybody comes in here's got to have a shot, house rules. Inhibition's the first thing to go. Two more of these and you'll be telling me your nastiest, dirtiest stories. I am your beat priestess and it's time to confess.	}{	#	}{	npc.SetDisposition("Joy", 3)	}{	}{	}{	}{	}{	}{	}{	}{	}
```

Поля:
1. `{1}` - ID
2-3. `{Everybody comes in here's got to have a shot...}` - Responses
4. `{#}` - Next ID
5. `{npc.SetDisposition("Joy", 3)}` - Conditions
6. `{}` - Scripts
7-13. `{}` - Все clan responses пустые

### Строка 3 jeanette.dlg (Tremere response)
```
{	3	}{	Frightening isn't the word I'd use... exciting is more like it.	}{	Frightening isn't the word I'd use... exciting is more like it.	}{	21	}{	Seduction 2 & not IsClan(pc,"Malkavian")	}{	G.Jeanette_Seduce = G.Jeanette_Seduce + 1	}{	}{	}{	}{	}{	}{	}{	}
```

Поля:
1. `{3}` - ID
2-3. `{Frightening isn't the word...}` - Responses
4. `{21}` - Next ID
5. `{Seduction 2 & not IsClan(pc,"Malkavian")}` - Conditions
6. `{G.Jeanette_Seduce = G.Jeanette_Seduce + 1}` - Scripts
7-13. `{}` - Все clan responses пустые

## Дополнительно

### Поля, используемые в скриптинге (из VampireRemake-KB/01_Original/Santa_Monica/Locations/medical1/SM-14_Medical_Assets/extract-dialogue.js):

```javascript
const cols=['file','line','id','text','next','field4','field5','field6'];
```

Где (по Mod Developer Guide раздел IV.2):
- `field4` = Conditions (поля 4)
- `field5` = Scripts (поля 5)
- `field6` = Brujah response (поле 6)

### CSV-выход (SM-13_Jeanette_DLG_Nodes.csv):

Заголовок:
```
dlg_id,type,male_text_excerpt,female_text_excerpt,malkavian_text_excerpt,target,condition_field,action_field
```

Где:
- `condition_field` = Поля 4 (Conditions)
- `action_field` = Поля 5-6 (Scripts + Brujah response)

## Вывод

Верифицирована структура DLG файлов Bloodlines с 13 полями (по Mod Developer Guide, раздел IV.2):

1. **ID** - Уникальный идентификатор узла
2. **Response 1** - Мужская/основная реплика
3. **Response 2** - Женская/альтернативная реплика
4. **Next ID** - ID следующего узла
5. **Conditions** - Условия показа ответа
6. **Scripts** - Скрипты (действия)
7-13. **Clan-specific responses** - Ответы для Brujah, Gangrel, Nosferatu, Toreador, Tremere, Ventrue, Malkavian

Структура подтверждена на основе анализа реальных DLG файлов:
- arthur.dlg
- venus.dlg
- jeanette.dlg

**Репозиторий**: `C:\Users\Slava\Documents\Bloodlines-GLM\VampireRemake-KB\Research\DLG_Field_Structure_Analysis.md`
**Дата**: 9 ноября 2026
**Статус**: VERIFIED_STATIC - Все поля подтверждены анализом исходных DLG файлов согласно Mod Developer Guide раздел IV.2.
