# i-agent

1.	Заходим на курс «Конструирование интеллектуальных агентов», раздел «Практикум». Переходим по ссылке «Игра Лабиринт».
 

2.	Нажимаем на кнопку добавить игру
 	
3.	Вводим название вашего агента, выбираем тип агента – API агент
4.	Выбор типовой тестовой задачи – «Найти золото (карта неизвестна)».
5.	Нажимаем на кнопку «Сохранить»
 
6.	Идентификатор сгенерированной игры отобразится в левом столбце
 
7.	Далее обращаемся по адресу mooped.net/local/its?module=game&action=agentaction&gameid=1&act=noAct noAct
Возможные действия:
Первый параметр (пассивные действия):
onAct – ничего не делать;
onLeft – поворот налево на 90 градусов;
onRight – поворот направо на 90 градусов;
UpSideDn – разворот на 180 градусов.

Через пробел второй параметр (активные действия)
onAct – ничего не делать;
Go – идти вперед в следующую клетку в текущем направлении движения агента;
Take – взять клад в текущей пещере;
Shoot – выстрел стрелой в текущем направлении движения агента

Примеры:
act=noAct noAct – ничего не делать, получить текущее восприятие пещеры.
act=onLeft noAct – повернуть налево (изменение направления движения агента). Движения нет.
act=upSideDn Go – развернуться и идти вперед.
act=noAct Go – идти вперед в текущем направлении движения агента
act=noAct Take – взять клад
и другие комбинации параметров.

Пример ответа от сервера (JSON):
{
    "text": {
        "currentcave": {
            "cNum": "0_0",
            "rowN": 0,
            "colN": 0,
            "isGold": 0,
            "isMonster": 0,
            "isHole": 0,
            "isWind": false,
            "isBones": false,
            "isVisiable": true,
            "dirList": {
                "Right": 1,
                "Down": 2
            }
        },
        "worldinfo": {
            "newcaveopened": 0,
            "isgoldfinded": 0,
            "ismonsteralive": 1,
            "tiktak": 0
        },
        "iagent": {
            "arrowcount": 1,
            "actsCostList": {
                "Go": 1,
                "Shoot": 10,
                "Take": 1,
                "onLeft": 0.1,
                "onRight": 0.1,
                "upSideDn": 0.1,
                "noAct": 0,
                "RockSlide": 50,
                "KilledByMonster": 100
            },
            "passivMoves": [
                "onLeft",
                "onRight",
                "upSideDn",
                "noAct"
            ],
            "activMoves": [
                "Go",
                "Shoot",
                "Take",
                "noAct"
            ],
            "dirList": {
                "Right": 1,
                "Down": 2
            },
            "WStateUtilities": {
                "isgoldfinded": 100,
                "ismonsteralive": 35,
                "newcaveopened": 5
            },
            "IAStateUtilities": {
                "isagentalive": 100,
                "legsQ": 50,
                "arrowsQ": 5,
                "havegold": 100
            },
            "worldInfo": null,
            "allDirs": {
                "Up": 0,
                "Right": 1,
                "Down": 2,
                "Left": 3
            },
            "aname": "\u0410\u0433\u0435\u043d\u0442 007",
            "cavenum": "0_0",
            "dir": "Down",
            "legscount": 2, 
            "choosenact": "noAct noAct",
            "isagentalive": 1,
            "havegold": 0,
            "guid": "1"
        },
         "userid": 2
    },
    "error": null, 
    "url": null
}

