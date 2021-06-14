from dataclasses import dataclass
import json
from models.task import Task, TaskStatus
from models.course import Course


def load():
    with open("save.json", "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    return data


def save(data):
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_courses():
    courses = load().get("courses")
    if courses is None:
        return

    return [Course(k, v.get("name")) for k, v in courses.items()]


def add_course(course: Course):
    data = load()
    courses = data.get("courses")

    if courses is None:
        data["courses"] = {}
        courses = data["courses"]

    courses[course.id] = {"name": course.name}
    save(data)

    return 0


def remove_course(id: str):
    data = load()
    courses: dict = data.get("courses")

    if courses is None:
        return 1

    courses.pop(id)
    save(data)

    return 0


def add_tasks(course_id: str, tasks: list[Task]):
    data = load()
    courses: dict = data.get("courses")
    if courses is None:
        return 1

    course: dict = courses.get(course_id)
    if (course is None):
        return 1

    tasks_save: dict = course.get("tasks")
    if tasks_save is None:
        course["tasks"] = {}
        tasks_save = course["tasks"]

    for task in tasks:
        tasks_save[task.id] = {
            "name": task.name,
            "status": task.status.value
        }

    save(data)

    return 0


def remove_tasks(course_id: str, task: str):
    data = load()
    courses: dict = data.get("courses")
    if courses is None:
        return 1

    course: dict = courses.get(course_id)
    if (course is None):
        return 1

    tasks_save: dict = course.get("tasks")
    if tasks_save is None:
        course["tasks"] = {}
        tasks_save = course["tasks"]

    tasks_save.pop(task)

    save(data)

    return 0


def get_tasks(course_id: str):
    data = load()
    courses: dict = data.get("courses")
    if courses is None:
        return 1

    course: dict = courses.get(course_id)
    if (course is None):
        return 1

    tasks_save: dict = course.get("tasks")
    if tasks_save is None:
        return []

    return [Task(k, v.get("name"), TaskStatus(v.get("status"))) for k, v in tasks_save.items()]


def set_task_status(course_id: str, task_id: str, status: TaskStatus):
    data = load()
    courses: dict = data.get("courses")
    if courses is None:
        return 1

    course: dict = courses.get(course_id)
    if (course is None):
        return 1

    tasks: dict = course.get("tasks")
    if tasks is None:
        return 1

    task = tasks.get(task_id)
    if task is None:
        return 0

    task["status"] = status.value

    save(data)
