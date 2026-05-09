from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


class StudentTable:
    __scripts = {
        "select_by_user_id": text("SELECT * FROM student WHERE user_id = :user_id"),
        "insert": text(
            "INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:user_id, :level, :education_form, :subject_id)"
        ),
        "update": text(
            "UPDATE student SET level = :level, education_form = :education_form, subject_id = :subject_id WHERE user_id = :user_id"
        ),
        "delete": text("DELETE FROM student WHERE user_id = :user_id"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.__db)

    @contextmanager
    def get_session(self):
        """Контекстный менеджер для работы с сессией БД."""
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_student_by_id(self, user_id):
        """Получить студента по user_id."""
        with self.get_session() as session:
            result = session.execute(
                self.__scripts["select_by_user_id"], {"user_id": user_id}
            ).fetchone()
            return result

    def add_student(self, user_id, level, education_form, subject_id=None):
        """Добавить нового студента."""
        with self.get_session() as session:
            session.execute(
                self.__scripts["insert"],
                {
                    "user_id": user_id,
                    "level": level,
                    "education_form": education_form,
                    "subject_id": subject_id,
                },
            )
            return user_id

    def update_student(self, user_id, level, education_form, subject_id=None):
        """Обновить информацию о студенте."""
        with self.get_session() as session:
            session.execute(
                self.__scripts["update"],
                {
                    "user_id": user_id,
                    "level": level,
                    "education_form": education_form,
                    "subject_id": subject_id,
                },
            )

    def delete_student(self, user_id):
        """Удалить студента по user_id."""
        with self.get_session() as session:
            session.execute(self.__scripts["delete"], {"user_id": user_id})


class SubjectTable:
    __scripts = {
        "select_all": text("SELECT * FROM subject"),
        "select_by_id": text("SELECT * FROM subject WHERE subject_id = :subject_id"),
        # Мы не используем RETURNING id. Вместо этого будем сами генерировать ID.
        "insert_new": text(
            "INSERT INTO subject (subject_id, subject_title) VALUES (:subject_id, :subject_title)"
        ),
        "update": text(
            "UPDATE subject SET subject_title = :subject_title WHERE subject_id = :subject_id"
        ),
        "delete": text("DELETE FROM subject WHERE subject_id = :subject_id"),
        # Скрипт для получения максимального ID
        "get_max_subject_id": text("SELECT MAX(subject_id) FROM subject"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.__db)

    @contextmanager
    def get_session(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_subjects(self):
        with self.get_session() as session:
            return session.execute(self.__scripts["select_all"]).fetchall()

    def get_subject_by_id(self, subject_id):
        with self.get_session() as session:
            result = session.execute(
                self.__scripts["select_by_id"], {"subject_id": subject_id}
            ).fetchone()
            return result

    def add_subject(self, subject_title):
        """
        Добавляет предмет и возвращает его subject_id.
        Самостоятельно генерирует уникальный ID перед вставкой.
        """
        with self.get_session() as session:
            # 1. Получаем текущий максимальный ID из таблицы
            max_result = session.execute(
                self.__scripts["get_max_subject_id"]
            ).fetchone()

            # 2. Если таблица пуста (max_result[0] is None), начинаем с ID 1.
            #    Иначе берем следующий за максимальным.
            next_subject_id = 1 if max_result[0] is None else max_result[0] + 1

            # 3. Вставляем новую запись с нашим сгенерированным ID.
            #    Используем новый скрипт 'insert_new', который принимает subject_id.
            session.execute(
                self.__scripts["insert_new"],
                {"subject_title": subject_title, "subject_id": next_subject_id},
            )

            return next_subject_id

    def update_subject(self, subject_id, subject_title):
        with self.get_session() as session:
            session.execute(
                self.__scripts["update"],
                {"subject_title": subject_title, "subject_id": subject_id},
            )

    def delete_subject(self, subject_id):
        with self.get_session() as session:
            session.execute(self.__scripts["delete"], {"subject_id": subject_id})
