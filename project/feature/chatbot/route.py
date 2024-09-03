from .request_validator import request_validtor
from .controller import ChatBotController
from .blueprint import chatbot_bp

@chatbot_bp.route("/QA", methods=["POST"])
@request_validtor.Validate_Qa()
def create_qa(validate_data):
    controller = ChatBotController()
    response = controller.create_qa(validate_data)
    return response, 201