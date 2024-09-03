from project.module.exception_format import AppError


class WrongQuestion(AppError):
    description="this question is out of this topic"
    http_code=404