# test_db.py

import pytest
from db_table import StudentTable, SubjectTable

# ВАЖНО: Убедись, что строка верная. В прошлый раз там была опечатка.
DATABASE_URL = "postgresql://postgres:7187@localhost:5432/QA-Y"


@pytest.fixture
def student_table():
    return StudentTable(DATABASE_URL)


@pytest.fixture
def subject_table():
    return SubjectTable(DATABASE_URL)


# --- ТЕСТЫ ДЛЯ СТУДЕНТОВ ---

def test_add_student(student_table):
    user_id = 12345  # Используем user_id как ID
    level = "Bachelor"
    education_form = "Full-time"

    # Добавляем студента и получаем его user_id
    returned_user_id = student_table.add_student(user_id, level, education_form)

    # Проверяем, что вернули тот же ID
    assert returned_user_id == user_id

    # Проверяем через БД, что студент добавлен
    student = student_table.get_student_by_id(user_id)
    assert student is not None
    assert student['level'] == level
    assert student['education_form'] == education_form

    # Удаляем созданного студента (очистка)
    student_table.delete_student(user_id)

    # Проверяем, что удалили
    assert student_table.get_student_by_id(user_id) is None


def test_update_student(student_table):
    user_id = 67890
    initial_level = "Bachelor"
    new_level = "Master"

    # Создаем студента
    student_table.add_student(user_id, initial_level, "Full-time")

    # Обновляем данные
    student_table.update_student(user_id, new_level, "Part-time")

    # Проверяем обновление
    student = student_table.get_student_by_id(user_id)
    assert student['level'] == new_level

    # Очистка
    student_table.delete_student(user_id)


def test_delete_student(student_table):
    user_id = 55555

    # Создаем и сразу удаляем
    student_table.add_student(user_id, "Bachelor", "Full-time")
    student_table.delete_student(user_id)

    # Проверяем отсутствие записи
    assert student_table.get_student_by_id(user_id) is None


# --- ТЕСТЫ ДЛЯ ПРЕДМЕТОВ ---
# Логика похожа: мы добавляем предмет и пытаемся получить его ID,
# который генерируется базой данных (SERIAL).

def test_add_subject(subject_table):
    title = "Mathematics"

    # Добавляем предмет. Метод теперь возвращает ID из БД.
    subject_db_id = subject_table.add_subject(title)

    assert subject_db_id is not None

    # Проверяем через БД
    subject = subject_table.get_subject_by_id(subject_db_id)
    assert subject is not None
    assert subject['subject_title'] == title

    # Очистка
    subject_table.delete_subject(subject_db_id)


def test_update_subject(subject_table):
    title_old = "Physics"
    title_new = "Advanced Physics"

    # Добавляем предмет
    subj_id = subject_table.add_subject(title_old)

    # Обновляем название
    subject_table.update_subject(subj_id, title_new)

    # Проверяем обновление
    updated_subject = subject_table.get_subject_by_id(subj_id)
    assert updated_subject['subject_title'] == title_new

    # Очистка
    subject_table.delete_subject(subj_id)


def test_delete_subject(subject_table):
    title = "Chemistry"

    # Добавляем предмет
    subj_to_delete = subject_table.add_subject(title)

    # Удаляем его
    subject_table.delete_subject(subj_to_delete)

    # Проверяем отсутствие записи по ID
    assert subject_table.get_subject_by_id(subj_to_delete) is None