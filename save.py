from utils.time import Time
from models.course import Course
from models.task import Task, TaskStatus
from models.event import Event
from storage import storage


def get_courses():
    courses = storage().get("courses").as_dict()
    return [Course(k, v.get("name")) for k, v in courses.items()]


def get_course(course_id: str):
    course = storage().get("courses").get(course_id).as_dict()
    return Course(course_id, course.get("name"))


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
    return [Task(k, v.get("name"), course_id, TaskStatus(v.get("status"))) for k, v in tasks.items()]


def get_all_tasks():
    courses = get_courses()
    return [task for course in courses for task in get_tasks(course.id)]


def set_task_status(course_id: str, task_id: str, status: TaskStatus):
    return storage().get("courses").get(course_id).get("tasks").get(task_id).edit("status", status.value)


def start_timer(time: float, course_id: str):
    return storage().get("timer").add("temp", {
        "start": time,
        "course_id": course_id,
    })


def end_timer():
    return storage().get("timer").remove("temp")


def get_current_timer():
    return storage().get("timer").get("temp").as_dict()


def add_current_study(date: str, start_timer: Time, end_timer: Time, course_id: str):
    events = storage().get("timer").get("events").get(date).as_dict()
    return storage().get("timer").get("events").get(date).add(len(events) + 1, {
        "start": start_timer.timestamp,
        "end": end_timer.timestamp,
        "course_id": course_id,
    })


def get_events(date: Time):
    date = date.get_date()
    events = storage().get("timer").get("events").get(date).as_dict()
    return [Event(
        k,
        Time(v.get("start")),
        Time(v.get("end")),
        get_course(v.get("course_id")).name)
        for k, v in events.items()]
