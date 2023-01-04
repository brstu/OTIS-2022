```                    
                                          МИНИСТЕРСТВО ОБРАЗОВАНИЯ РЕСПУБЛИКИ БЕЛАРУСЬ
                                                      УЧРЕЖДЕНИЕ ОБРАЗОВАНИЯ
                                      “БРЕСТСКИЙ ГОСУДАРСТВЕННЫЙ ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ”
                                            ИНТЕЛЕКТУАЛЬНЫЕ ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ
                                            
                                                              ОТЧЁТ
                                                    По лабораторной работе № 4
                                                    
                                                    
                                                                          Выполнил:
                                                                          Студент группы ИИ-22
                                                                          Копанчук Евгений Романович 
                                                                          Проверил: Иванюк Д. С.
                                                                          
                                                                          
                                                          Брест - 2022
```
## Задача :trophy:
Изучить репозиторий проекта Nika и запустить её на своей машине.

## Ход работы :pencil:

#### 1. Изучил readme репозитория :heavy_check_mark:

#### 2.0 Попробовал запустить приложение на Windows 10 :x:
* Установил Docker Desktop.
* Ввёл следующие команды. 
``` shell 
git clone -c core.longpaths=true -c core.autocrlf=true https://github.com/ostis-apps/nika
cd nika
git submodule update --init --recursive
```
> Получил следующие ошибки, которые не получилось исправить:
![error_win10](https://github.com/Corowka/OTIS-2022/blob/Lab4/trunk/ii02209/task_04/doc/img/error_win10.png?raw=true)

#### 2.1 Установка прилодения на Linux Ubuntu 22.04.1 LTS (Jammy Jellyfish) :heavy_check_mark:
* Установил Docker по инструкции с оффициального сайта.
* Снова ввёл команды:
``` shell 
git clone -c core.longpaths=true -c core.autocrlf=true https://github.com/ostis-apps/nika
cd nika
git submodule update --init --recursive
```
* Запустил Docker и ввёд остальные команды:
``` shell 
docker compose pull
docker compose up --no-build
```
* Перешёл по полученной ссылке в веб-интерфейс.

#### 3. Тестирование приложения :heavy_check_mark:
* Попробовал повторить пример из документации:
![example_1](https://github.com/Corowka/OTIS-2022/blob/Lab4/trunk/ii02209/task_04/doc/img/example_1.png?raw=true)
![example_2](https://github.com/Corowka/OTIS-2022/blob/Lab4/trunk/ii02209/task_04/doc/img/example_2.png?raw=true)

#### 4. Запуск документации :heavy_check_mark:
* Ввел команды из репозитория:
``` shell 
pip3 install mkdocs markdown-include mkdocs-material
mkdocs serve
```
* И перешёл по [ссылке](http://127.0.0.1:8000/) в консоли. 
![example_doc](https://github.com/Corowka/OTIS-2022/blob/Lab4/trunk/ii02209/task_04/doc/img/example_doc.png?raw=true)
