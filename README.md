# Assignment 01 [Basics]

---

**Далее внизу расположена основная необходимая информация по использованию репозитория и сдаче ДЗ.**

Если у вас остались вопросы по установке каких-то программ, советуем заглянуть в файл [PROGRAMS.md](PROGRAMS.md).

## Основные правила

1. Задания расположены в папке [`tasks/`](tasks)
    * в [`tasks/a`](tasks/a/) расположены задания _advanced_ версии для тех,
      кто относительно уверенно пользуется языком
    * в [`tasks/b`](tasks/b/) расположены задания _basic_ версии для закрепления
      умения пользоваться базовыми конструкциями языка
    * достаточно выполнить только одну из версий, чтобы набрать полный балл
2. Не обращайте внимание на файлы `__init__.py` &ndash; они вам не понадобятся
3. **Нельзя редактировать** файлы, лежащие в папке [`test/`](test),
   *если в явном виде не указано обратное*, а также файлы, расположенные в папке [`.github`](.github)
   (которой пока нет, не беспокойтесь)

## Репозиторий

**Если этот репозиторий имеет имя `assignment-01-basics`**, вы, скорее всего, не там, где вам нужно.

Вам понадобится работать с репозиторием с именем `assignment-01-basics-ваш-ник`. Если у вас нет такого репозитория:

* в канале есть [инвайт-ссылка](https://classroom.github.com/a/RY3XgrvI) для принятия первого задания &ndash; пройдите
  по ней
* для начала GitHub предложит присоединиться к Classroom, далее нажмите `Accept assignment`, и дождитесь (пару секунд),
  когда ваш репозиторий автоматически создастся
* как только сообщение по этой ссылке изменится на информацию об успешном создании вашего репозитория (он будет иметь
  название `assignment-01-basics-ваш-логин`), нужно перейти по предлагаемой ссылке

## План выполнения домашнего задания

### 1. Клонирование репозитория

Склонируйте **ваш** репозиторий:

<details>
<summary>Через консоль по SSH (только если настроен SSH-ключ)</summary>

1. Откройте консоль/терминал
2. Перейдите в папку, в которую хотите склонировать репозиторий, командой `cd`
3. Запустите команду

```shell
git clone git@github.com:ITMO-PhysTech-2022/assignment-01-basics-ваш-ник
```

4. В текущей директории должна появиться папка `assignment-01-basics-ваш-ник`
5. Откройте эту папку как проект в PyCharm

</details>

<details>
<summary>Через интерфейс PyCharm</summary>

1. Откройте PyCharm
2. Выберите меню 'Git' &rightarrow; 'Clone' или 'VCS' &rightarrow; 'Get from Version Control'
3. Вставьте ссылку `https://github.com/ITMO-PhysTech-2022/assignment-01-basics-ваш-ник.git`
    * ссылку можно скопировать на странице репозитория на GitHub
4. Нажмите Clone, Trust project (если понадобится), Open

</details>

### 2. Синхронизация истории

**Это важный пункт, не пропускайте его!**

#### Лирическое отступление

В репозитории [`assignment-01-basics`](https://github.com/ITMO-PhysTech-2022/assignment-01-basics) будут
периодически выкладываться обновления (например, появятся тесты к заданиям). Вам необходимо настроить возможность
подгружать эти изменения в ваш репозиторий.

По умолчанию это невозможно, так как исходный общий репозиторий создан @doreshnikov, а ваши репозитории автоматически
создаются github-classroom[bot]'ом, и в них совершенно несвязанные друг с другом истории, которые не получится
перемешивать.

**Eсли вы уже сделали какие-то задания, не синхронизовав историю**, вам в любом случае будет больно, независимо
от того, какой способ вы выбрали, так что просто напишите своему преподавателю практики за помощью (либо научитесь
использовать `git cherry-pick`)

#### Инструкция

<details>
<summary>Для ленивых, но бесстрашных (рекомендовано)</summary>

Вы можете воспользоваться скриптом, который все сделает за вас.

**Предупреждение**:

* скрипт еще не тестировался во всех возможных сценариях
* вся ваша ветка `main` потеряется (хотя в теории данные можно будет восстановить, если вы не удалите
  с концами папку с проектом
* если у вас нет SSH-ключа, вам придется проделать некоторые действия руками, но основную работу скрипт сделает для вас

Для запуска скрипта:

1. Откройте Git Bash (найдите приложение поиском Windows) или Bash (если у вас Unix-подобная система)
2. Перейдите в папку текущего проекта с помощью команды `cd`. Если вы используете Windows и стандартную папку для
   проектов,
   команда будет выглядеть примерно так:

```shell
cd /c/Users/.../PycharmProjects/.../assignment-01-basics-ваш-ник
```

3. Запустите скрипт и следуйте инструкциям

```shell
./sync-history.sh
```

При возникновении любых проблем и ошибок пишите в телеграм [@doreshnikov](https://t.me/doreshnikov).

При невозникновении любых ошибок радуйтесь жизни и тому, что эта сомнительная штука работает... -_-
</details>

<details>
<summary>Для любителей тыкать в кнопочки в PyCharm</summary>

1. В открытом в PyCharm проекте выбираем меню 'Git' &rightarrow; 'Manage Remotes'
2. В появившемся окне нужно кликнуть на `+`, чтобы добавить удаленный (в смысле не локальный) репозиторий,
   в поле `Name:` написать `upstream`, а в `URL:` вставить ссылку на главный репозиторий (в нашем
   случае `https://github.com/ITMO-PhysTech-2022/assignment-01-basics.git`)
3. После того, как кликнете 'OK', должна быть такая ситуация:

![Git Remotes](https://i.ibb.co/QpK87XQ/2022-09-28-11-37-14.png)

4. Подгружаем все изменения с помощью 'Git' &rightarrow; 'Fetch'
5. Далее выбираем **на нижней панели** Git наш созданный `upstream`, там ветку `main`
6. Кликаем на последний commit сбоку правой
   кнопкой мыши и выбираем 'Reset Current Branch to Here...'
   * в появившемся окне поставить галочку напротив 'Hard' (не 'Soft' и не 'Mixed')

![Reset upstream](https://i.ibb.co/QCWhWf0/2022-09-28-11-43-34.png)

6. Пушим все благодаря всё той же вкладке 'Git' сверху на панели: 'Git' &rightarrow; 'Push'
    * в появившемся окне вместо 'Push' в выпадающем меню выбираем 'Force Push'

</details>

Если все сработает, история коммитов в вашем репозитории на гитхабе должна начать совпадать с историей гравного
репозитория.
В таком случае радуемся и выполняем задания :)

Иначе пишите преподавателям практики &ndash; они (возможно) помогут.

### 3. Выполнение ДЗ

**Перед выполнением заданий перейдите на другую ветку, не выполняйте задания в ветке `main`!**

Рекомендуется выполнять все на ветке `dev`.

Для перехода на ветку `dev` можно воспользоваться одним из двух способов:

* `git checkout -b dev`
* меню 'Git' &rightarrow; 'Branches' &rightarrow; 'New Branch'

#### Собственно, про сами задания (повторение)...

В репозитории есть папка [`tasks/`](tasks), внутри которой задания, поделенные на два уровня:

* [`a`](tasks/a) (_advanced_) &ndash; для тех, кому скучно делать совсем базовые вещи, если вы их уже знаете
* [`b`](tasks/b) (_basic_) &ndash; для тех, кто с питоном не знаком

Вы можете пока что сами выбрать более комфортный вам уровень. Все инструкции по выполнению заданий расположены в
комментариях, собственно, в файлах с этими заданиями.

### 4. Загрузка обновлений из главного репозитория

Здесь чуть позже появится более подробный гайд, а пока что одно из двух:

* `git pull --rebase upstream main`
* меню 'Git' &rightarrow; 'Branches', там кликнуть по `upstream/main` и выбрать 'Pull into \'текущая ветка\' Using
  Rebase'

### 5. Сдача ДЗ

**Пусть это вас пока не беспокоит, дедлайн еще не скоро, тестов еще нет**

А вообще надо будет сделать Pull Request из ветки `dev` в ветку `main` вашего репозитория.