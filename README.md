
# Python ELT Project

Този проект е примерна **ELT (Extract, Load, Transform)** архитектура, реализирана на Python.  
Основната цел е да извлече данни от S3, да ги зареди в Snowflake, да ги трансформира в аналитични и почистени таблици, и накрая да валидира резултатите.

## 📂 Структура на проекта



PYTHON\_ELT\_PROJECT/
│
├── python\_ELT\_project/       # Основни конфигурации
│  
│   └── setting.py            # Настройки и константи
│
├── extract/                  # Извличане на данни
│   
│   └── extract\_from\_s3.py    # Скрипт за четене на данни от S3
│
├── load/                     # Зареждане на данни
│   └── load\_to\_snowsflake.py # Скрипт за писане на данни в Snowflake
│
├── transform/                # Трансформация на данните
│   
│   ├── analytics\_tables.py   # Създаване на аналитични таблици
│   └── cleaned\_tables.py     # Почистване на суровите данни
│
├── validations/              # Валидация на данните
│   
│   ├── analytics\_table\_validations.py # Проверки за аналитичните таблици
│   └── cleaned\_table\_validations.py   # Проверки за почистените таблици
│
├── etl\_pipeline.log          # Лог файл на изпълненията
└── run\_etl\_pipeline.py       # Основен скрипт за стартиране на ELT процеса



## ⚙️ Функционалности

1. **Extract**  
   - Извличане на данни от S3 (`extract_from_s3.py`).

2. **Load**  
   - Зареждане на данните в Snowflake (`load_to_snowflake.py`).

3. **Transform**  
   - Почистване на сурови данни (`cleaned_tables.py`).
   - Подготовка на аналитични таблици (`analytics_tables.py`).

4. **Validation**  
   - Проверки на почистените данни (`cleaned_table_validations.py`).
   - Проверки на аналитичните данни (`analytics_table_validations.py`).

## 🚀 Как да стартираме проекта

1. **Клониране на репото**
   ```bash
   git clone https://github.com/your-username/python-elt-project.git
   cd python-elt-project
````

2. **Инсталиране на зависимостите**

   ```bash
   pip install -r requirements.txt
   ```

3. **Конфигуриране**

   * Редактирайте `python_ELT_project/setting.py` с вашите S3 и Snowflake креденшъли.

4. **Стартиране на целия ELT процес**

   ```bash
   python run_etl_pipeline.py
   ```

## 📝 Логове

* Всички логове се записват в `etl_pipeline.log`.

## 📌 Бележки

* Проектът е модулно структуриран, така че всяка стъпка от ELT процеса може да се стартира отделно.
* Лесно може да се адаптира към други източници на данни и дестинации.

---



