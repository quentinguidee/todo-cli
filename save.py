from storage import storage

from models.task import Task, TaskStatus
from models.course import Course


def get_courses():
    courses = storage().get("courses").as_dict()
    return [Course(k, v.get("name")) for k, v in courses.items()]


def add_course(course: Course):
    return storage().get("courses").add(course.id, {"name": course.name})


def remove_course(id: str):
    return storage().get("courses").remove(id)


def add_tasks(course_id: str, new_tasks: list[Task]):
    new_tasks = [(task.id, {
        "name": task.name,
        "status": task.status.value
    }) for task in new_tasks]
    return storage().get("courses").get(course_id).get("tasks").add_all(new_tasks)


def remove_task(course_id: str, task: str):
    return storage().get("courses").get(course_id).get("tasks").remove(task)


def get_tasks(course_id: str):
    tasks = storage().get("courses").get(course_id).get("tasks").as_dict()
    return [Task(k, v.get("name"), TaskStatus(v.get("status"))) for k, v in tasks.items()]


def set_task_status(course_id: str, task_id: str, status: TaskStatus):
    return storage().get("courses").get(course_id).get("tasks").get(task_id).edit("status", status.value)
